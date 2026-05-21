# ScreenGraph-Vision Tests

本目录包含 ScreenGraph-Vision 的单元测试和集成测试。

## 运行测试

```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试文件
python -m pytest tests/test_core.py -v

# 运行带覆盖率报告的测试
python -m pytest tests/ --cov=src --cov-report=html
```

## 测试结构

- `test_core.py`: 核心模块测试
- `test_integration.py`: 集成测试（需要API密钥）
