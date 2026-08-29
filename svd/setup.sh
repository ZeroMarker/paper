#!/usr/bin/env bash
# svd 项目构建前置脚本（CI 编译前运行）
# 生成论文插图等中间产物（不入库，见根目录 .gitignore）

set -e
pip install --quiet numpy matplotlib
python3 svd_demo.py
