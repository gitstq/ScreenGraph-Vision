#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScreenGraph-Vision Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    with open(readme_file, 'r', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name="screengraph-vision",
    version="1.0.0",
    author="gitstq",
    author_email="",
    description="Lightweight Terminal Screen Screenshot Intelligent Analysis Engine based on GLM-5.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitstq/ScreenGraph-Vision",
    license="MIT",
    packages=find_packages(),
    package_dir={"": "."},
    package_data={
        "src": ["*.py"],
    },
    include_package_data=True,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "screengraph=src.screengraph_vision:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords=[
        "screenshot",
        "screen-capture",
        "vision",
        "GLM",
        "multimodal",
        "AI",
        "terminal",
        "TUI",
        "image-analysis",
        "UI-analysis"
    ],
)
