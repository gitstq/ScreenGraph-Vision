# 🌐 語言切換 / Language Selector

[![简体中文](https://img.shields.io/badge/-简体中文-000000?style=flat-square)](README.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-000000?style=flat-square)](README_TC.md)
[![English](https://img.shields.io/badge/-English-000000?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/-日本語-000000?style=flat-square)](README_JA.md)
[![한국어](https://img.shields.io/badge/-한국어-000000?style=flat-square)](README_KO.md)
[![Español](https://img.shields.io/badge/-Español-000000?style=flat-square)](README_ES.md)

---

# 📸 ScreenGraph-Vision

### 輕量級終端螢幕截圖智能分析引擎 | 基於 GLM-5.1 多模態能力

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![零依賴](https://img.shields.io/badge/依賴項-零-brightgreen.svg)](#快速開始)
[![星標](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)](https://github.com/gitstq/ScreenGraph-Vision/stargazers)

> 🎯 **讓 AI 擁有"眼睛"，一鍵分析任意截圖！**

---

## 🎉 專案介紹

**ScreenGraph-Vision** 是一款專為開發者打造的**輕量級終端螢幕截圖智能分析引擎**。它基於智譜 GLM-5.1 的強大多模態能力，讓用戶能夠在終端環境下快速完成截圖分析、UI 元素識別、可訪問性評估等任務。

### ✨ 核心價值

- 🔍 **智能截圖分析** - 自動識別截圖內容，生成詳細描述
- 🎨 **UI 元素識別** - 精準定位按鈕、輸入框、連結等可交互元素
- ♿ **可訪問性評估** - 分析色彩對比度、文本可讀性等無障礙指標
- 📊 **差異對比** - 智能對比兩張截圖的變化，追蹤 UI 迭代
- ⚡ **零依賴設計** - 純 Python 標準庫實現，開箱即用
- 🎮 **TUI 交互介面** - 優雅的終端用戶介面，操作便捷

### 🚀 自研差異化亮點

1. **GLM-5.1 原生支援** - 深度整合智譜最新多模態大模型
2. **終端原生體驗** - 專為 CLI 用戶優化的 TUI 交互設計
3. **智能緩存機制** - 避免重複分析，節省 Token 消耗
4. **跨平台兼容** - macOS / Linux / Windows 全平台支援
5. **批量處理能力** - 支援目錄批量截圖分析

---

## ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🖼️ **多模態分析** | 基於 GLM-5.1 強大視覺理解能力 |
| 🎯 **UI 元素識別** | 自動識別按鈕、表單、菜單等 UI 元件 |
| ♿ **可訪問性檢查** | WCAG 合規性自動評估 |
| 📊 **差異檢測** | 智能對比截圖變化 |
| 💾 **智能緩存** | 基於內容雜湊的本地緩存 |
| 🌐 **多語言支援** | 中文 / 英文 / 日語 / 韓語介面 |
| ⚡ **零依賴** | 僅使用 Python 標準庫 |
| 🔧 **多種輸入** | 檔案輸入 / 截圖 / 剪貼簿 |

---

## 🚀 快速開始

### 環境要求

- 🐍 Python 3.7+
- 🔑 GLM API 金鑰（[前往智譜AI平台獲取](https://open.bigmodel.cn/)）

### 📦 安裝方式

#### 方式一：直接運行（推薦）

```bash
# 克隆倉庫
git clone https://github.com/gitstq/ScreenGraph-Vision.git
cd ScreenGraph-Vision

# 直接運行
python screengraph.py
```

#### 方式二：安裝為命令列工具

```bash
# 安裝
pip install -e .

# 全域使用
screengraph interactive
```

#### 方式三：pip 安裝

```bash
pip install screengraph-vision
```

### 🔧 首次配置

```bash
# 運行配置嚮導
python screengraph.py config

# 或設定環境變數
export GLM_API_KEY="your_api_key_here"
```

### 🚀 基本使用

#### 交互式模式（推薦新手）

```bash
python screengraph.py
```

#### 截圖並分析

```bash
python screengraph.py capture
```

#### 分析圖片檔案

```bash
python screengraph.py analyze /path/to/screenshot.png
```

#### 指定分析類型

```bash
# 通用描述（預設）
python screengraph.py analyze screenshot.png --type general

# UI 元素分析
python screengraph.py analyze screenshot.png --type ui

# 可訪問性評估
python screengraph.py analyze screenshot.png --type accessibility

# 差異對比
python screengraph.py analyze screenshot.png --type diff
```

#### 批量分析

```bash
python screengraph.py batch /path/to/screenshots/ --pattern "*.png"
```

---

## 📖 詳細使用指南

### 🎯 分析模式詳解

#### 1. 通用描述模式 (general)

自動分析截圖內容，生成詳細文字描述：

```
輸入: 任意截圖
輸出:
- 主要內容概述
- 關鍵資訊提取
- 佈局結構描述
- 色調風格分析
```

#### 2. UI 元素分析模式 (ui)

精準識別介面中的可交互元素：

```
輸入: UI 截圖
輸出:
- 按鈕列表（位置 + 名稱）
- 輸入框列表
- 連結列表
- 菜單項列表
- 圖示按鈕說明
```

#### 3. 可訪問性評估模式 (accessibility)

檢查介面的無障礙特性：

```
輸入: 任意介面截圖
輸出:
- 主要功能說明
- 文字可讀性評分
- 色彩對比度分析
- 潛在問題列表
- 改進建議
```

#### 4. 差異對比模式 (diff)

對比兩張截圖的變化：

```
輸入: 目前截圖 + 歷史截圖
輸出:
- 新增元素
- 刪除元素
- 變化元素
- 佈局變更說明
```

### ⚙️ 配置文件位置

配置文件存儲在 `~/.screengraph/config.json`

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

### 🌐 環境變數

| 變數名 | 說明 | 必填 |
|--------|------|------|
| `GLM_API_KEY` | 智譜 API 金鑰 | ✅ |
| `GLM_API_BASE` | API 位址（可選） | ❌ |

---

## 💡 設計思路與迭代規劃

### 🏗️ 設計理念

1. **零依賴優先** - 最大限度減少外部依賴，降低使用門檻
2. **終端原生** - 尊重 CLI 用戶習慣，提供熟悉的交互體驗
3. **模組化架構** - 清晰的模組劃分，便於擴展和維護
4. **緩存為王** - 智能緩存機制，避免重複請求浪費資源

### 📋 技術選型

- **語言**: Python 3.7+
- **標準庫**: urllib.request, json, base64, subprocess
- **API**: GLM-5V（智譜多模態大模型）
- **緩存**: 本地 JSON 檔案（基於 MD5 雜湊）

### 🔮 後續迭代計劃

- [ ] **v1.1.0** - 支援螢幕區域選擇截圖
- [ ] **v1.2.0** - 增加批量任務佇列管理
- [ ] **v1.3.0** - 支援自定義分析 Prompt 模板
- [ ] **v2.0.0** - Web UI 介面版本
- [ ] **v2.1.0** - MCP Server 協定支援
- [ ] **v2.2.0** - IDE 插件整合

---

## 📦 打包與部署

### 🐳 Docker 部署

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install -e .

CMD ["python", "screengraph.py", "interactive"]
```

### ☁️ 雲端函數部署

支援部署至各大雲端函數平台：

```bash
# AWS Lambda 打包
pip install -e . -t ./package
cd package && zip -r ../lambda.zip .
```

### 📱 桌面快捷方式

創建系統快捷命令：

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

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request！

### 🐛 Bug 回饋

請在 [GitHub Issues](https://github.com/gitstq/ScreenGraph-Vision/issues) 中提交，包含以下資訊：

- 作業系統和 Python 版本
- 完整的錯誤日誌
- 重現步驟

### ✨ 功能建議

- 提交 Feature Request
- 描述使用場景
- 可能的實現方案

### 🔧 程式碼貢獻

1. Fork 本倉庫
2. 創建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 創建 Pull Request

---

## 📄 開源協定

本專案基於 [MIT License](LICENSE) 開源。

---

## 🙏 致謝

- [智譜 AI](https://www.zhipuai.cn/) - 提供強大的 GLM 多模態大模型
- 所有貢獻者的辛勤付出

---

## 📊 專案統計

![Stars](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)
![Forks](https://img.shields.io/github/forks/gitstq/ScreenGraph-Vision?style=social)
![Issues](https://img.shields.io/badge/github/issues-ScreenGraph_Vision-green)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

<div align="center">

**如果對你有幫助，請給我們一個 ⭐️**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
