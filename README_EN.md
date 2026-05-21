# 🌐 Language Selector / 语言切换

[![简体中文](https://img.shields.io/badge/-简体中文-000000?style=flat-square)](README.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-000000?style=flat-square)](README_TC.md)
[![English](https://img.shields.io/badge/-English-000000?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/-日本語-000000?style=flat-square)](README_JA.md)
[![한국어](https://img.shields.io/badge/-한국어-000000?style=flat-square)](README_KO.md)
[![Español](https://img.shields.io/badge/-Español-000000?style=flat-square)](README_ES.md)

---

# 📸 ScreenGraph-Vision

### Lightweight Terminal Screen Screenshot Intelligent Analysis Engine | Powered by GLM-5.1 Multimodal AI

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)](#quick-start)
[![Stars](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)](https://github.com/gitstq/ScreenGraph-Vision/stargazers)

> 🎯 **Give AI a pair of "eyes" - Analyze any screenshot with one click!**

---

## 🎉 Project Introduction

**ScreenGraph-Vision** is a **lightweight terminal-based screen screenshot intelligent analysis engine** designed specifically for developers. Powered by Zhipu AI's GLM-5.1 multimodal capabilities, it enables users to quickly perform screenshot analysis, UI element recognition, accessibility evaluation, and more directly in the terminal environment.

### ✨ Core Values

- 🔍 **Intelligent Screenshot Analysis** - Automatically identify screenshot content with detailed descriptions
- 🎨 **UI Element Recognition** - Precisely locate buttons, input fields, links, and other interactive elements
- ♿ **Accessibility Evaluation** - Analyze color contrast, text readability, and other accessibility metrics
- 📊 **Difference Comparison** - Smart comparison of changes between two screenshots
- ⚡ **Zero-Dependency Design** - Built with pure Python standard library, ready to use
- 🎮 **TUI Interactive Interface** - Elegant terminal user interface with smooth operation

### 🚀 Self-Developed Differentiated Highlights

1. **Native GLM-5.1 Support** - Deep integration with Zhipu's latest multimodal LLM
2. **Terminal-Native Experience** - TUI design optimized for CLI users
3. **Smart Caching Mechanism** - Avoid duplicate analysis, save Token consumption
4. **Cross-Platform Compatibility** - Full support for macOS / Linux / Windows
5. **Batch Processing** - Support for directory-based batch screenshot analysis

---

## ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🖼️ **Multimodal Analysis** | Powered by GLM-5.1's powerful visual understanding |
| 🎯 **UI Element Recognition** | Automatic identification of buttons, forms, menus, etc. |
| ♿ **Accessibility Check** | WCAG compliance automatic evaluation |
| 📊 **Difference Detection** | Smart screenshot change comparison |
| 💾 **Smart Caching** | Local cache based on content hash |
| 🌐 **Multi-Language Support** | Chinese / English / Japanese / Korean interface |
| ⚡ **Zero Dependencies** | Python standard library only |
| 🔧 **Multiple Inputs** | File input / Screenshot / Clipboard |

---

## 🚀 Quick Start

### Requirements

- 🐍 Python 3.7+
- 🔑 GLM API Key ([Get from Zhipu AI Platform](https://open.bigmodel.cn/))

### 📦 Installation

#### Method 1: Direct Run (Recommended)

```bash
# Clone the repository
git clone https://github.com/gitstq/ScreenGraph-Vision.git
cd ScreenGraph-Vision

# Run directly
python screengraph.py
```

#### Method 2: Install as CLI Tool

```bash
# Install
pip install -e .

# Use globally
screengraph interactive
```

#### Method 3: pip Install

```bash
pip install screengraph-vision
```

### 🔧 Initial Configuration

```bash
# Run configuration wizard
python screengraph.py config

# Or set environment variable
export GLM_API_KEY="your_api_key_here"
```

### 🚀 Basic Usage

#### Interactive Mode (Recommended for Beginners)

```bash
python screengraph.py
```

#### Capture and Analyze

```bash
python screengraph.py capture
```

#### Analyze Image File

```bash
python screengraph.py analyze /path/to/screenshot.png
```

#### Specify Analysis Type

```bash
# General description (default)
python screengraph.py analyze screenshot.png --type general

# UI element analysis
python screengraph.py analyze screenshot.png --type ui

# Accessibility evaluation
python screengraph.py analyze screenshot.png --type accessibility

# Difference comparison
python screengraph.py analyze screenshot.png --type diff
```

#### Batch Analysis

```bash
python screengraph.py batch /path/to/screenshots/ --pattern "*.png"
```

---

## 📖 Detailed Usage Guide

### 🎯 Analysis Mode Details

#### 1. General Description Mode (general)

Automatically analyze screenshot content and generate detailed text descriptions:

```
Input: Any screenshot
Output:
- Main content overview
- Key information extraction
- Layout structure description
- Color style analysis
```

#### 2. UI Element Analysis Mode (ui)

Precisely identify interactive elements in the interface:

```
Input: UI screenshot
Output:
- Button list (position + name)
- Input field list
- Link list
- Menu item list
- Icon button description
```

#### 3. Accessibility Evaluation Mode (accessibility)

Check the accessibility features of the interface:

```
Input: Any interface screenshot
Output:
- Main function description
- Text readability score
- Color contrast analysis
- Potential issues list
- Improvement suggestions
```

#### 4. Difference Comparison Mode (diff)

Compare changes between two screenshots:

```
Input: Current screenshot + Historical screenshot
Output:
- New elements
- Removed elements
- Changed elements
- Layout change description
```

### ⚙️ Configuration File Location

Configuration is stored at `~/.screengraph/config.json`

```json
{
    "api_base_url": "https://open.bigmodel.cn/api/paas/v4",
    "model": "glm-4v-plus",
    "api_key": "your_key_here",
    "screenshot_tool": "auto",
    "max_tokens": 2048,
    "temperature": 0.7,
    "cache_enabled": true
}
```

### 🌐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GLM_API_KEY` | Zhipu API Key | ✅ |
| `GLM_API_BASE` | API URL (Optional) | ❌ |

---

## 💡 Design Philosophy & Iteration Plan

### 🏗️ Design Principles

1. **Zero-Dependency First** - Minimize external dependencies, lower usage barriers
2. **Terminal-Native** - Respect CLI user habits, provide familiar interactive experience
3. **Modular Architecture** - Clear module division for easy extension and maintenance
4. **Cache is King** - Smart caching mechanism to avoid redundant requests

### 📋 Technology Stack

- **Language**: Python 3.7+
- **Standard Library**: urllib.request, json, base64, subprocess
- **API**: GLM-5V (Zhipu Multimodal LLM)
- **Cache**: Local JSON files (Based on MD5 hash)

### 🔮 Future Iteration Plan

- [ ] **v1.1.0** - Support screen region selection for screenshots
- [ ] **v1.2.0** - Add batch task queue management
- [ ] **v1.3.0** - Support custom analysis Prompt templates
- [ ] **v2.0.0** - Web UI version
- [ ] **v2.1.0** - MCP Server protocol support
- [ ] **v2.2.0** - IDE plugin integration

---

## 📦 Packaging & Deployment

### 🐳 Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install -e .

CMD ["python", "screengraph.py", "interactive"]
```

### ☁️ Cloud Function Deployment

Supports deployment to major cloud function platforms:

```bash
# AWS Lambda packaging
pip install -e . -t ./package
cd package && zip -r ../lambda.zip .
```

### 📱 Desktop Shortcuts

Create system shortcuts:

```bash
# macOS
echo 'alias sg="/path/to/screengraph.py"' >> ~/.zshrc
source ~/.zshrc

# Linux
echo 'alias sg="/path/to/screengraph.py"' >> ~/.bashrc
source ~/.bashrc

# Windows (PowerShell)
Set-Alias -Name sg -Value "C:\path\screengraph.py"
```

---

## 🤝 Contributing

We welcome Issue and Pull Request submissions!

### 🐛 Bug Reports

Please submit at [GitHub Issues](https://github.com/gitstq/ScreenGraph-Vision/issues) with:

- OS and Python version
- Complete error logs
- Reproduction steps

### ✨ Feature Requests

- Submit Feature Request
- Describe use case
- Possible implementation approach

### 🔧 Code Contribution

1. Fork this repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Create Pull Request

---

## 📄 Open Source License

This project is open source under [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [Zhipu AI](https://www.zhipuai.cn/) - Providing powerful GLM multimodal LLM
- All contributors for their hard work

---

## 📊 Project Stats

![Stars](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)
![Forks](https://img.shields.io/github/forks/gitstq/ScreenGraph-Vision?style=social)
![Issues](https://img.shields.io/github/issues/gitstq/ScreenGraph-Vision)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

<div align="center">

**If this helps you, please give us a ⭐️**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
