# 数学论文文库

## 项目结构

```
paper/
├── goldbach/               # 哥德巴赫猜想综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
├── svd/                    # SVD 论文
│   ├── svd_paper.tex       # 主LaTeX文件
│   └── svd_demo.py         # 演示脚本
├── riemann/                # 黎曼猜想综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
├── twin_primes/            # 孪生素数猜想综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
├── fermat/                 # 费马大定理综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
├── kakeya/                 # 挂谷猜想综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
├── langlands/              # 朗兰兹纲领综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
└── paper.yaml              # Zotero 文库分类
```

## 论文列表

| 论文 | 目录 | 构建 tag |
|------|------|----------|
| 哥德巴赫猜想：历史、进展与展望 | `goldbach/` | `goldbach-1.0.0` |
| SVD 论文 | `svd/` | `svd-1.0.0` |
| 黎曼猜想：历史、进展与展望 | `riemann/` | `riemann-1.0.0` |
| 孪生素数猜想：历史、进展与展望 | `twin_primes/` | `twin_primes-1.0.0` |
| 费马大定理：历史、进展与展望 | `fermat/` | `fermat-1.0.0` |
| 挂谷猜想：历史、进展与展望 | `kakeya/` | `kakeya-1.0.0` |
| 朗兰兹纲领：历史、进展与展望 | `langlands/` | `langlands-1.0.0` |

## 编译方法

### Windows
```bash
cd goldbach && .\compile.bat
cd riemann  && .\compile.bat
```

### Linux/macOS
```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

## CI 构建

统一使用通用工作流 `.github/workflows/build-paper.yml`：推送形如 `<paper_name>-<version>` 的 tag（例如 `riemann-1.0.0`）即触发，编译 PDF 并上传到 GitHub Release。

目录解析规则：tag `<paper_name>-<version>` 对应顶层目录 `<paper_name>/`；根文件优先 `main.tex`，否则取目录中唯一的含 `\documentclass` 的 `.tex`。新增论文时无需修改工作流，建好顶层目录并打 tag 即可。

若论文目录中存在 `setup.sh`，CI 会在编译前运行它（如 `svd/` 用它安装 Python 依赖并运行 `svd_demo.py` 生成插图）；没有 `setup.sh` 则跳过。生成的图片等中间产物不入库（见 `.gitignore`），每次构建现场生成。

## 黎曼猜想综述主要内容

1. **引言**：问题陈述与研究意义
2. **历史发展**：从1859年至今的研究历程
3. **研究方法**：显式公式、硬性定理、随机矩阵理论、代数几何类比等
4. **重要成果**：零点数值验证、临界线零点比例、等价命题等
5. **应用与推广**：素数分布、计算复杂度、密码学、数学物理等应用
6. **开放问题**：GRH、林德勒夫假设、零点精细统计等
7. **结论**：总结与展望

## 孪生素数猜想综述主要内容

1. **引言**：猜想陈述与 Hardy--Littlewood 猜想 B
2. **历史发展**：布伦筛法、陈氏定理、GPY 方法、张益唐突破、Polymath8
3. **研究方法**：筛法理论、奇偶性壁垒、多维筛法、计算验证
4. **重要成果**：有界间隔纪录（$7\times10^7 \to 246$）、陈氏定理、布朗常数
5. **应用与推广**：素数间隔理论、概率模型、$k$ 元组理论
6. **开放问题**：孪生素数主猜想、Elliott--Halberstam 猜想、Dickson 猜想
7. **结论**：总结与展望

## 费马大定理综述主要内容

1. **引言**：定理陈述与研究意义
2. **历史发展**：费马、欧拉、库默尔、弗雷曲线、里贝特定理、怀尔斯1995
3. **研究方法**：无穷下降法、分圆域与理想论、模形式、模性提升（$R=T$）
4. **重要成果**：部分结果时间线、怀尔斯--泰勒定理、模性定理、广义费马方程
5. **应用与推广**：算术几何标准技术、朗兰兹纲领、模方法
6. **开放问题**：Beal 猜想、广义费马方程、模性定理的推广
7. **结论**：总结与展望

## 挂谷猜想综述主要内容

1. **引言**：Besicovitch 集与挂谷猜想的陈述、研究意义
2. **历史发展**：挂谷转针问题（1917）、Pál 正三角形、Besicovitch 零测集、Davies 平面满维数
3. **研究方法**：Kakeya 极大算子、Córdoba 灌木丛论证、Wolff 毛刷论证、多线性方法与多项式分划、有限域多项式方法（Dvir 定理）、Wang--Zahl 凸集体积估计
4. **重要成果**：维数下界时间线、Davies 定理、Wolff $(n+2)/2$、Dvir 定理、多线性 Kakeya 估计、Wang--Zahl 三维证明（2025）
5. **应用与联系**：限制性估计、Bochner--Riesz 求和、局部光滑化、色散方程解耦、组合几何与数论、多项式方法的辐射效应
6. **开放问题**：高维（$n \ge 4$）挂谷猜想、Kakeya 极大算子、局部光滑化与限制性、Furstenberg 集与算术挂谷
7. **结论**：总结与展望

## 朗兰兹纲领综述主要内容

1. **引言**：互反律与函子性两大支柱、完备性猜想、研究意义
2. **历史发展**：高斯与阿廷互反律、自守形式的算术化、1967 年朗兰兹致韦伊信件、局部/整体/几何三个层次
3. **研究方法**：adèle 语言与自守表示、$L$ 函数与欧拉积、Arthur--Selberg 迹公式与内窥理论、形变理论与 $R=T$、势自守性、Shtuka 与几何朗兰兹、逆定理
4. **重要成果**：进展时间线、Langlands--Tunnell 二维互反律、模性定理与 Serre 猜想、局部朗兰兹（$\operatorname{GL}_n$）、函数域完全解决（Drinfeld、L. Lafforgue、V. Lafforgue）、Ng\^o 基本引理、Arthur 分类、Kim--Shahidi 对称幂、Gaitsgory--Raskin 几何朗兰兹（2024）
5. **应用与联系**：费马大定理与 Sato--Tate、解析数论红利、表示论与代数几何、数学物理（S-对偶）
6. **开放问题**：广义 Artin 猜想、一般函子性与广义 Ramanujan、Selberg 特征值、$p$-adic 朗兰兹、带分歧几何朗兰兹与韦伊纲领 II
7. **结论**：总结与展望
