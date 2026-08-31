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
├── law_of_large_numbers/   # 大数定律综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
├── poincare/               # 庞加莱猜想综述
│   ├── main.tex            # 主LaTeX文件
│   ├── sections/           # 章节文件
│   ├── references/         # BibTeX文献库
│   └── compile.bat         # Windows编译脚本
├── abc_conjecture/         # ABC 猜想综述
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
| 大数定律：历史、进展与展望 | `law_of_large_numbers/` | `law_of_large_numbers-1.0.0` |
| 庞加莱猜想：历史、进展与展望 | `poincare/` | `poincare-1.0.0` |
| ABC 猜想：历史、进展与展望 | `abc_conjecture/` | `abc_conjecture-1.0.0` |

## 编译方法

### Windows
```bash
cd goldbach    && .\compile.bat
cd riemann     && .\compile.bat
cd twin_primes && .\compile.bat
cd fermat      && .\compile.bat
cd kakeya      && .\compile.bat
cd langlands   && .\compile.bat
cd law_of_large_numbers && .\compile.bat
cd poincare    && .\compile.bat
cd abc_conjecture && .\compile.bat
```

SVD 论文无 `compile.bat`（根文件为 `svd_paper.tex`，需先运行 `setup.sh` 由 `svd_demo.py` 生成插图再编译）：
```bash
cd svd && bash setup.sh && pdflatex svd_paper.tex
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

## 哥德巴赫猜想综述主要内容

1. **引言**：问题陈述（强/弱哥德巴赫猜想）与研究意义
2. **历史发展**：1742 年哥德巴赫致欧拉信件、哈代--李特尔伍德圆法、布伦筛法到陈景润
3. **研究方法**：圆法（优弧与劣弧）、筛法（布伦筛法、塞尔伯格筛法）、指数和估计（华罗庚引理、外尔不等式）、大筛法
4. **重要成果**：维诺格拉多夫三素数定理（1937）、黑尔弗戈特对弱哥德巴赫的完全证明（2013）、布伦定理、陈氏定理（1966）、数值验证纪录
5. **相关应用与推广**：加性数论（华林问题）、密码学、计算数论、遍历理论
6. **开放问题**：强哥德巴赫猜想及其定量形式、波利尼亚克猜想、例外集最优指数
7. **结论**：总结与展望
8. **附录**：维诺格拉多夫定理与陈氏定理证明概要、历史文献

## SVD 论文主要内容

1. **引言**：研究背景与目的
2. **SVD 理论基础**：奇异值分解定理、奇异值性质、计算方法
3. **SVD 的几何意义**：线性变换的分解、单位圆的变换解释
4. **SVD 图像压缩方法**：截断 SVD 压缩原理
5. **实验结果与分析**：压缩效果对比、奇异值分布、误差分析（`svd_demo.py` 生成插图）
6. **结论**：主要贡献、局限性与未来方向

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

## 大数定律综述主要内容

1. **引言**：定律陈述（弱/强形式）、频率稳定性的精确化、研究意义
2. **历史发展**：伯努利《猜度术》（1713）、泊松命名、切比雪夫与马尔可夫、博雷尔（1909）与康泰利（1917）强大数定律、科尔莫哥洛夫的综合（1928--1933）、相依与无穷维推广
3. **研究方法**：切比雪夫不等式与方差控制、博雷尔--康泰利引理与子序列法、科尔莫哥洛夫极大值不等式与截断法、特征函数法、鞅方法、遍历论观点
4. **重要成果**：进展时间线、伯努利/切比雪夫/辛钦/科尔莫哥洛夫/Etemadi 定理、三级数定理、Marcinkiewicz--Zygmund 定理、Glivenko--Cantelli 定理、迭代对数定律、收敛速度（Hsu--Robbins、Baum--Katz、Hoeffding）
5. **应用与联系**：统计推断（相合性、MLE、一致大数定律与 VC 理论）、蒙特卡洛方法、信息论（AEP）、数论与动力系统（正规数、等分布）、随机过程与精算、与中心极限定理的尺度阶梯
6. **开放问题**：无穷均值与圣彼得堡悖论的规范化、强逼近（KMT）与最优速率、相依框架边界、巴拿赫空间值与算子水平推广、随机算法与非交换概率
7. **结论**：总结与展望
8. **附录**：科尔莫哥洛夫不等式与强大数定律证明梗概、伯努利原始证明思想、符号与术语表

## 庞加莱猜想综述主要内容

1. **引言**：猜想陈述（闭单连通三维流形同胚于 $S^3$）、各维数对比、研究意义
2. **历史发展**：庞加莱《位置分析》五补充篇与同调球面（1895--1904）、怀特海流形与 Dehn--Papakyriakopoulou--Haken--Waldhausen 积累、高维（斯梅尔 1961）与拓扑四维（弗里德曼 1982）的胜利、瑟斯顿几何化纲领与哈密顿里奇流（1982）
3. **研究方法**：里奇流方程与曲率夹挤（Hamilton--Ivey）、$\mathcal{W}$-熵单调性与非坍缩定理、$\kappa$-解与典范邻域、带手术的里奇流与手术一致性、有限熄灭定理与拓扑重建
4. **重要成果**：进展时间线、斯梅尔/弗里德曼定理、佩雷尔曼三篇预印本（2002--2003）、社区验证（曹--朱、摩根--田、克莱纳--洛特）、三维几何化定理
5. **应用与联系**：三维流形分类与算法可判定性、纽结理论、四维拓扑（怪异 $\mathbb{R}^4$ 与光滑 $S^4$）、群论刻画、宇宙拓扑与量子场论
6. **开放问题**：光滑四维庞加莱猜想与怪异 $S^4$、四维里奇流奇点分类与弱流穿越、高维非坍缩（Bamler 纲领）、四维几何化、证明的形式化
7. **结论**：总结与展望
8. **附录**：非坍缩定理与有限熄灭定理证明梗概、符号与术语表

## ABC 猜想综述主要内容

1. **引言**：猜想陈述（$c < K_\varepsilon\,\operatorname{rad}(abc)^{1+\varepsilon}$）、质量与加法--乘法不相容性、研究意义
2. **历史发展**：函数域原型 Mason--Stothers 定理（1981）、Masser--Oesterl\'e 提出（1985）、等价网络与无条件界（Szpiro、Elkies、Stewart--Tijdeman、Stewart--Yu）、Granville--Tucker 纲领化（2002）、望月新一 IUT（2012）与 Scholze--Stix 争议（2018）
3. **研究方法**：等价形式与 Frey 曲线桥、Wronskian 与函数域方法（特征 $p$ 例外）、Baker 对数线性型与显式下界、Belyi 映射构造优质三元组、IUT 纲领概览（霍奇剧场、$\theta$-函数异用等距、log-shell 与系 3.12）
4. **重要成果**：进展时间线、Stewart--Yu 型下界、等价网络（ABC $\Leftrightarrow$ Szpiro $\Rightarrow$ 渐近费马/有效 Mordell）、IUT 现状的中立纪事
5. **应用与联系**：渐近费马、广义费马（Darmon--Granville）、Catalan 型方程、Hall 弱形式、平方自由值、有效 Mordell、Szpiro 控制、算术动力系统、Vojta 纲领、实验数论（abc@home）
6. **开放问题**：IUT 缺口的解决或绕越、显式 $K_\varepsilon$ 与质量分布、特征 $p$ 类比、Vojta 型推广、大型证明的可传递性与形式化
7. **结论**：总结与展望
8. **附录**：Mason--Stothers 定理证明、从 ABC 到渐近费马的推导梗概、符号与术语表
