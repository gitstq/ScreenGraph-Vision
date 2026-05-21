#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScreenGraph-Vision 命令行入口
Command Line Entry Point
"""

import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.screengraph_vision import main

if __name__ == '__main__':
    main()
