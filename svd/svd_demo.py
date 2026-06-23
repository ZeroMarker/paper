"""
SVD (Singular Value Decomposition) 图像压缩演示
=================================================
本脚本演示SVD的几何意义及其在图像压缩中的应用。

SVD定理: A = UΣV^T
- U: 左奇异向量矩阵 (m×m 正交矩阵)
- Σ: 奇异值对角矩阵 (m×n 对角矩阵)
- V^T: 右奇异向量转置矩阵 (n×n 正交矩阵)

几何意义: 任意线性变换可分解为 旋转 → 缩放 → 旋转
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
rcParams['axes.unicode_minus'] = False


def create_sample_image(size=32):
    """创建一个示例32×32灰度图像（包含几何图形）"""
    img = np.zeros((size, size))
    
    # 绘制一个简单的图案：圆形 + 十字
    center = size // 2
    y, x = np.ogrid[:size, :size]
    
    # 圆形
    radius = size // 3
    circle_mask = (x - center) ** 2 + (y - center) ** 2 <= radius ** 2
    img[circle_mask] = 200
    
    # 十字
    img[center-2:center+2, :] = 150
    img[:, center-2:center+2] = 150
    
    # 添加一些噪声使其更真实
    np.random.seed(42)
    noise = np.random.normal(0, 10, img.shape)
    img = np.clip(img + noise, 0, 255)
    
    return img.astype(np.float64)


def explain_svd_geometry():
    """解释SVD的几何意义"""
    print("=" * 60)
    print("SVD 几何意义解释")
    print("=" * 60)
    print()
    print("对于任意矩阵 A (m×n)，SVD将其分解为:")
    print("    A = U × Σ × V^T")
    print()
    print("几何解释:")
    print("    1. V^T: 第一次旋转（在输入空间中）")
    print("    2. Σ:   缩放变换（沿坐标轴方向）")
    print("    3. U:   第二次旋转（在输出空间中）")
    print()
    print("这意味着任意线性变换都可以分解为:")
    print("    旋转 → 缩放 → 旋转")
    print()
    
    # 创建一个简单的2x2示例
    A = np.array([[2, 1], [1, 3]])
    U, S, Vt = np.linalg.svd(A)
    
    print("示例矩阵 A:")
    print(A)
    print()
    print("SVD分解结果:")
    print(f"U = \n{U}")
    print(f"Σ = {S}")
    print(f"V^T = \n{Vt}")
    print()
    print(f"验证: U × diag(Σ) × V^T = \n{U @ np.diag(S) @ Vt}")


def svd_compress(image, k):
    """使用SVD对图像进行压缩，保留前k个奇异值"""
    U, S, Vt = np.linalg.svd(image, full_matrices=False)
    
    # 只保留前k个奇异值
    U_k = U[:, :k]
    S_k = S[:k]
    Vt_k = Vt[:k, :]
    
    # 重构图像
    compressed = U_k @ np.diag(S_k) @ Vt_k
    
    return compressed, S


def calculate_error(original, compressed, k):
    """计算压缩误差"""
    mse = np.mean((original - compressed) ** 2)
    rmse = np.sqrt(mse)
    
    # 计算PSNR (峰值信噪比)
    if mse > 0:
        psnr = 10 * np.log10(255**2 / mse)
    else:
        psnr = float('inf')
    
    # 计算压缩比
    m, n = original.shape
    original_size = m * n
    compressed_size = k * (m + n + 1)
    compression_ratio = original_size / compressed_size
    
    return mse, rmse, psnr, compression_ratio


def demonstrate_compression(image, k_values):
    """演示不同k值的压缩效果"""
    print("\n" + "=" * 60)
    print("SVD 图像压缩演示")
    print("=" * 60)
    print(f"原始图像大小: {image.shape[0]}×{image.shape[1]} = {image.size} 个像素值")
    print()
    
    # 创建子图
    n_plots = len(k_values) + 1
    fig, axes = plt.subplots(1, n_plots, figsize=(4*n_plots, 4))
    
    # 显示原图
    axes[0].imshow(image, cmap='gray', vmin=0, vmax=255)
    axes[0].set_title('原始图像')
    axes[0].axis('off')
    
    results = []
    
    for i, k in enumerate(k_values):
        compressed, singular_values = svd_compress(image, k)
        mse, rmse, psnr, compression_ratio = calculate_error(image, compressed, k)
        
        # 显示压缩后的图像
        axes[i+1].imshow(compressed, cmap='gray', vmin=0, vmax=255)
        axes[i+1].set_title(f'k={k}')
        axes[i+1].axis('off')
        
        results.append({
            'k': k,
            'mse': mse,
            'rmse': rmse,
            'psnr': psnr,
            'compression_ratio': compression_ratio
        })
        
        print(f"k = {k:2d}: MSE = {mse:.2f}, RMSE = {rmse:.2f}, "
              f"PSNR = {psnr:.2f} dB, 压缩比 = {compression_ratio:.2f}x")
    
    plt.tight_layout()
    plt.savefig('compression_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return results, singular_values


def plot_singular_values(singular_values):
    """绘制奇异值分布图"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # 奇异值分布
    ax1.bar(range(1, len(singular_values)+1), singular_values)
    ax1.set_xlabel('奇异值索引')
    ax1.set_ylabel('奇异值大小')
    ax1.set_title('奇异值分布')
    
    # 累积能量百分比
    total_energy = np.sum(singular_values ** 2)
    cumulative_energy = np.cumsum(singular_values ** 2) / total_energy * 100
    
    ax2.plot(range(1, len(singular_values)+1), cumulative_energy, 'b-o', markersize=3)
    ax2.set_xlabel('保留的奇异值数量 (k)')
    ax2.set_ylabel('累积能量百分比 (%)')
    ax2.set_title('累积能量分布')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=95, color='r', linestyle='--', label='95%能量')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('singular_values.png', dpi=150, bbox_inches='tight')
    plt.close()


def plot_error_analysis(results):
    """绘制误差分析图"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    k_values = [r['k'] for r in results]
    mse_values = [r['mse'] for r in results]
    psnr_values = [r['psnr'] for r in results]
    cr_values = [r['compression_ratio'] for r in results]
    
    # MSE vs k
    axes[0, 0].plot(k_values, mse_values, 'b-o')
    axes[0, 0].set_xlabel('k (保留的奇异值数量)')
    axes[0, 0].set_ylabel('MSE')
    axes[0, 0].set_title('均方误差 vs k')
    axes[0, 0].grid(True, alpha=0.3)
    
    # PSNR vs k
    axes[0, 1].plot(k_values, psnr_values, 'r-o')
    axes[0, 1].set_xlabel('k (保留的奇异值数量)')
    axes[0, 1].set_ylabel('PSNR (dB)')
    axes[0, 1].set_title('峰值信噪比 vs k')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 压缩比 vs k
    axes[1, 0].plot(k_values, cr_values, 'g-o')
    axes[1, 0].set_xlabel('k (保留的奇异值数量)')
    axes[1, 0].set_ylabel('压缩比')
    axes[1, 0].set_title('压缩比 vs k')
    axes[1, 0].grid(True, alpha=0.3)
    
    # PSNR vs 压缩比
    axes[1, 1].plot(cr_values, psnr_values, 'm-o')
    axes[1, 1].set_xlabel('压缩比')
    axes[1, 1].set_ylabel('PSNR (dB)')
    axes[1, 1].set_title('质量-压缩比权衡')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('error_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    # 1. 解释SVD几何意义
    explain_svd_geometry()
    
    # 2. 创建示例图像
    image = create_sample_image(32)
    
    # 3. 保存原始图像
    plt.imsave('original_image.png', image, cmap='gray')
    
    # 4. 测试不同的k值
    k_values = [1, 2, 4, 8, 16]
    
    # 5. 演示压缩效果
    results, singular_values = demonstrate_compression(image, k_values)
    
    # 6. 绘制奇异值分布
    plot_singular_values(singular_values)
    
    # 7. 绘制误差分析
    plot_error_analysis(results)
    
    print("\n" + "=" * 60)
    print("输出文件:")
    print("  - original_image.png: 原始图像")
    print("  - compression_comparison.png: 压缩效果对比")
    print("  - singular_values.png: 奇异值分布图")
    print("  - error_analysis.png: 误差分析图")
    print("=" * 60)