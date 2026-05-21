# 🌐 Language Selector / 语言切换

[![简体中文](https://img.shields.io/badge/-简体中文-000000?style=flat-square)](README.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-000000?style=flat-square)](README_TC.md)
[![English](https://img.shields.io/badge/-English-000000?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/-日本語-000000?style=flat-square)](README_JA.md)
[![한국어](https://img.shields.io/badge/-한국어-000000?style=flat-square)](README_KO.md)
[![Español](https://img.shields.io/badge/-Español-000000?style=flat-square)](README_ES.md)

---

# 📸 ScreenGraph-Vision

### 轻量级终端屏幕截图智能分析引擎 | 基于 GLM-5.1 多模态能力

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)](#快速开始)
[![Stars](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)](https://github.com/gitstq/ScreenGraph-Vision/stargazers)

> 🎯 **让 AI 拥有"眼睛"，一键分析任意截图！** 

---

## 🎉 项目介绍

**ScreenGraph-Vision** 是一款专为开发者打造的**轻量级终端屏幕截图智能分析引擎**。它基于智谱 GLM-5.1 的强大多模态能力，让用户能够在终端环境下快速完成截图分析、UI 元素识别、可访问性评估等任务。

### ✨ 核心价值

- 🔍 **智能截图分析** - 自动识别截图内容，生成详细描述
- 🎨 **UI 元素识别** - 精准定位按钮、输入框、链接等可交互元素
- ♿ **可访问性评估** - 分析色彩对比度、文本可读性等无障碍指标
- 📊 **差异对比** - 智能对比两张截图的变化，追踪 UI 迭代
- ⚡ **零依赖设计** - 纯 Python 标准库实现，开箱即用
- 🎮 **TUI 交互界面** - 优雅的终端用户界面，操作便捷

### 🚀 自研差异化亮点

1. **GLM-5.1 原生支持** - 深度集成智谱最新多模态大模型
2. **终端原生体验** - 专为 CLI 用户优化的 TUI 交互设计
3. **智能缓存机制** - 避免重复分析，节省 Token 消耗
4. **跨平台兼容** - macOS / Linux / Windows 全平台支持
5. **批量处理能力** - 支持目录批量截图分析

---

## ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🖼️ **多模态分析** | 基于 GLM-5.1 强大视觉理解能力 |
| 🎯 **UI 元素识别** | 自动识别按钮、表单、菜单等 UI 组件 |
| ♿ **可访问性检查** | WCAG 合规性自动评估 |
| 📊 **差异检测** | 智能对比截图变化 |
| 💾 **智能缓存** | 基于内容哈希的本地缓存 |
| 🌐 **多语言支持** | 中文 / 英文 / 日语 / 韩语界面 |
| ⚡ **零依赖** | 仅使用 Python 标准库 |
| 🔧 **多种输入** | 文件输入 / 截图 / 剪贴板 |

---

## 🚀 快速开始

### 环境要求

- 🐍 Python 3.7+
- 🔑 GLM API 密钥（[前往智谱AI平台获取](https://open.bigmodel.cn/)）

### 📦 安装方式

#### 方式一：直接运行（推荐）

```bash
# 克隆仓库
git clone https://github.com/gitstq/ScreenGraph-Vision.git
cd ScreenGraph-Vision

# 直接运行
python screengraph.py
```

#### 方式二：安装为命令行工具

```bash
# 安装
pip install -e .

# 全局使用
screengraph interactive
```

#### 方式三：pip 安装

```bash
pip install screengraph-vision
```

### 🔧 首次配置

```bash
# 运行配置向导
python screengraph.py config

# 或设置环境变量
export GLM_API_KEY="your_api_key_here"
```

### 🚀 基本使用

#### 交互式模式（推荐新手）

```bash
python screengraph.py
```

#### 截图并分析

```bash
python screengraph.py capture
```

#### 分析图片文件

```bash
python screengraph.py analyze /path/to/screenshot.png
```

#### 指定分析类型

```bash
# 通用描述（默认）
python screengraph.py analyze screenshot.png --type general

# UI 元素分析
python screengraph.py analyze screenshot.png --type ui

# 可访问性评估
python screengraph.py analyze screenshot.png --type accessibility

# 差异对比
python screengraph.py analyze screenshot.png --type diff
```

#### 批量分析

```bash
python screengraph.py batch /path/to/screenshots/ --pattern "*.png"
```

---

## 📖 详细使用指南

### 🎯 分析模式详解

#### 1. 通用描述模式 (general)

自动分析截图内容，生成详细文字描述：

```
输入: 任意截图
输出: 
- 主要内容概述
- 关键信息提取
- 布局结构描述
- 色彩风格分析
```

#### 2. UI 元素分析模式 (ui)

精准识别界面中的可交互元素：

```
输入: UI 截图
输出:
- 按钮列表（位置 + 名称）
- 输入框列表
- 链接列表
- 菜单项列表
- 图标按钮说明
```

#### 3. 可访问性评估模式 (accessibility)

检查界面的无障碍特性：

```
输入: 任意界面截图
输出:
- 主要功能说明
- 文本可读性评分
- 色彩对比度分析
- 潜在问题列表
- 改进建议
```

#### 4. 差异对比模式 (diff)

对比两张截图的变化：

```
输入: 当前截图 + 历史截图
输出:
- 新增元素
- 删除元素
- 变化元素
- 布局变更说明
```

### ⚙️ 配置文件位置

配置文件存储在 `~/.screengraph/config.json`

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

### 🌐 环境变量

| 变量名 | 说明 | 必填 |
|--------|------|------|
| `GLM_API_KEY` | 智谱 API 密钥 | ✅ |
| `GLM_API_BASE` | API 地址（可选） | ❌ |

---

## 💡 设计思路与迭代规划

### 🏗️ 设计理念

1. **零依赖优先** - 最大限度减少外部依赖，降低使用门槛
2. **终端原生** - 尊重 CLI 用户习惯，提供熟悉的交互体验
3. **模块化架构** - 清晰的模块划分，便于扩展和维护
4. **缓存为王** - 智能缓存机制，避免重复请求浪费资源

### 📋 技术选型

- **语言**: Python 3.7+
- **标准库**: urllib.request, json, base64, subprocess
- **API**: GLM-5V (智谱多模态大模型)
- **缓存**: 本地 JSON 文件（基于 MD5 哈希）

### 🔮 后续迭代计划

- [ ] **v1.1.0** - 支持屏幕区域选择截图
- [ ] **v1.2.0** - 增加批量任务队列管理
- [ ] **v1.3.0** - 支持自定义分析 Prompt 模板
- [ ] **v2.0.0** - Web UI 界面版本
- [ ] **v2.1.0** - MCP Server 协议支持
- [ ] **v2.2.0** - IDE 插件集成

---

## 📦 打包与部署

### 🐳 Docker 部署

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install -e .

CMD ["python", "screengraph.py", "interactive"]
```

### ☁️ 云函数部署

支持部署至各大云函数平台：

```bash
# AWS Lambda 打包
pip install -e . -t ./package
cd package && zip -r ../lambda.zip .
```

### 📱 桌面快捷方式

创建系统快捷命令：

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

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 🐛 Bug 反馈

请在 [GitHub Issues](https://github.com/gitstq/ScreenGraph-Vision/issues) 中提交，包含以下信息：

- 操作系统和 Python 版本
- 完整的错误日志
- 复现步骤

### ✨ 功能建议

- 提交 Feature Request
- 描述使用场景
- 可能的实现方案

### 🔧 代码贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

## 🙏 致谢

- [智谱 AI](https://www.zhipuai.cn/) - 提供强大的 GLM 多模态大模型
- 所有贡献者的辛勤付出

---

## 📊 项目统计

![Stars](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)
![Forks](https://img.shields.io/github/forks/gitstq/ScreenGraph-Vision?style=social)
![Issues](https://img.shields.io/github/issues/gitstq/ScreenGraph-Vision)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

<div align="center">

**如果对你有帮助，请给我们一个 ⭐️**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
