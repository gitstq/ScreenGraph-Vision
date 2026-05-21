#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScreenGraph-Vision 配置管理模块
Configuration Management Module
"""

import os
import json
from pathlib import Path


class Config:
    """配置管理类"""
    
    DEFAULT_CONFIG = {
        "api_base_url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4v-plus",
        "api_key": "",
        "screenshot_tool": "auto",  # auto, macos, linux, windows
        "image_format": "png",
        "max_tokens": 2048,
        "temperature": 0.7,
        "cache_enabled": True,
        "cache_dir": ".screengraph_cache",
    }
    
    def __init__(self, config_path: str = None):
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()
    
    def _get_default_config_path(self) -> str:
        """获取默认配置路径"""
        home = Path.home()
        config_dir = home / ".screengraph"
        config_dir.mkdir(exist_ok=True)
        return str(config_dir / "config.json")
    
    def _load_config(self) -> dict:
        """加载配置"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    # 合并默认配置和用户配置
                    config = self.DEFAULT_CONFIG.copy()
                    config.update(user_config)
                    return config
            except Exception as e:
                print(f"⚠️ 配置文件加载失败: {e}, 使用默认配置")
                return self.DEFAULT_CONFIG.copy()
        return self.DEFAULT_CONFIG.copy()
    
    def save(self):
        """保存配置"""
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get(self, key: str, default=None):
        """获取配置项"""
        return self.config.get(key, default)
    
    def set(self, key: str, value):
        """设置配置项"""
        self.config[key] = value
    
    @property
    def api_key(self) -> str:
        """获取API密钥"""
        # 优先使用环境变量
        api_key = os.environ.get("GLM_API_KEY", "")
        if api_key:
            return api_key
        # 其次使用配置文件
        return self.config.get("api_key", "")
    
    @api_key.setter
    def api_key(self, value: str):
        """设置API密钥"""
        self.config["api_key"] = value
    
    def is_configured(self) -> bool:
        """检查是否已配置"""
        return bool(self.api_key)
    
    def print_config(self):
        """打印当前配置"""
        print("=" * 60)
        print("📋 ScreenGraph-Vision 当前配置")
        print("=" * 60)
        print(f"API Base URL: {self.config.get('api_base_url')}")
        print(f"Model: {self.config.get('model')}")
        print(f"Screenshot Tool: {self.config.get('screenshot_tool')}")
        print(f"Image Format: {self.config.get('image_format')}")
        print(f"Max Tokens: {self.config.get('max_tokens')}")
        print(f"Cache Enabled: {self.config.get('cache_enabled')}")
        print(f"API Key: {'*' * 20 if self.api_key else '❌ 未设置'}")
        print("=" * 60)
