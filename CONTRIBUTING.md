# Contributing to ScreenGraph-Vision

感谢您对 ScreenGraph-Vision 项目的兴趣！我们欢迎各种形式的贡献。

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/gitstq/ScreenGraph-Vision.git
cd ScreenGraph-Vision

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e .

# 运行测试
python -m pytest tests/ -v
```

## 代码规范

- 使用 Python 3.7+
- 遵循 PEP 8 代码规范
- 所有函数和类需要文档字符串
- 使用 type hints 提高代码可读性

## 分支管理

- `main` - 主分支，稳定版本
- `develop` - 开发分支
- `feature/*` - 功能分支
- `fix/*` - 修复分支

## 提交规范

使用 Angular 提交规范：

```
feat: 新功能
fix: 修复问题
docs: 文档更新
style: 代码格式（不影响功能）
refactor: 重构（不影响功能）
test: 测试
chore: 构建/工具
```

示例：
```
feat: 添加UI元素识别模式
fix: 修复缓存清理问题
docs: 更新README文档
```

## Pull Request 流程

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request
6. 等待代码审查

## Issue 报告

请在 [GitHub Issues](https://github.com/gitstq/ScreenGraph-Vision/issues) 中报告，包含：

- 清晰的标题和描述
- 复现步骤
- 预期行为 vs 实际行为
- 环境信息（OS、Python版本等）
- 错误日志和截图

## 许可

通过贡献代码，您同意您的代码将根据 MIT 许可证许可。
