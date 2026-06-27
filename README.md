# 哥德巴赫猜想综述

## 项目结构

```
paper/
├── main.tex                 # 主LaTeX文件
├── sections/               # 章节文件
│   ├── introduction.tex    # 引言
│   ├── history.tex         # 历史发展
│   ├── methods.tex         # 研究方法
│   ├── results.tex         # 研究成果
│   ├── applications.tex    # 应用与推广
│   ├── open_problems.tex   # 开放问题
│   ├── conclusion.tex      # 结论
│   └── appendix.tex        # 附录
├── references/             # 参考文献
│   └── references.bib      # BibTeX文献库
├── figures/                # 图片目录
├── tables/                 # 表格目录
└── compile.bat             # Windows编译脚本
```

## 编译方法

### Windows
```bash
.\compile.bat
```

### Linux/macOS
```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

## 主要内容

1. **引言**：问题陈述与研究意义
2. **历史发展**：从1742年至今的研究历程
3. **研究方法**：圆法、筛法、指数和估计等
4. **重要成果**：维诺格拉多夫定理、陈氏定理等
5. **应用与推广**：加性数论、密码学等应用
6. **开放问题**：强哥德巴赫猜想及相关猜想
7. **结论**：总结与展望

## 参考文献

包含哥德巴赫猜想研究的经典文献和最新进展。
