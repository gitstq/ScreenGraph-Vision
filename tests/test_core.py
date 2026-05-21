#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScreenGraph-Vision 测试模块
Test Module
"""

import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

# 添加src到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestConfig(unittest.TestCase):
    """配置模块测试"""
    
    def test_default_config(self):
        """测试默认配置"""
        from src.config import Config
        
        config = Config()
        
        self.assertEqual(config.get("model"), "glm-4v-plus")
        self.assertTrue(config.get("cache_enabled"))
        self.assertEqual(config.get("max_tokens"), 2048)
    
    def test_config_set_get(self):
        """测试配置设置和获取"""
        from src.config import Config
        
        config = Config()
        config.set("test_key", "test_value")
        
        self.assertEqual(config.get("test_key"), "test_value")
    
    def test_is_configured(self):
        """测试配置检查"""
        from src.config import Config
        
        config = Config()
        
        # 未设置API密钥时
        self.assertFalse(config.is_configured())


class TestAPIClient(unittest.TestCase):
    """API客户端测试"""
    
    def test_client_init_without_api_key(self):
        """测试无API密钥初始化"""
        from src.api_client import GLMClient
        
        with self.assertRaises(ValueError):
            GLMClient(api_key="")
    
    def test_client_init_with_api_key(self):
        """测试有API密钥初始化"""
        from src.api_client import GLMClient
        
        client = GLMClient(api_key="test_key_123")
        
        self.assertEqual(client.api_key, "test_key_123")
        self.assertEqual(client.model, "glm-4v-plus")
    
    def test_encode_image_to_base64(self):
        """测试图片编码"""
        from src.api_client import GLMClient
        
        client = GLMClient(api_key="test")
        
        # 创建一个临时测试图片
        test_image_path = "/tmp/test_image.png"
        with open(test_image_path, 'wb') as f:
            # 写入一个最小的PNG文件头
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00\x05\x18\xd8N\x00\x00\x00\x00IEND\xaeB`\x82')
        
        encoded = client._encode_image_to_base64(test_image_path)
        
        self.assertIsInstance(encoded, str)
        self.assertTrue(len(encoded) > 0)
        
        # 清理
        os.remove(test_image_path)


class TestTUI(unittest.TestCase):
    """TUI模块测试"""
    
    def test_colored_text(self):
        """测试彩色文本"""
        from src.tui import TUI
        
        colored = TUI._colored("test", "red")
        
        self.assertIn("test", colored)
    
    def test_bold_text(self):
        """测试加粗文本"""
        from src.tui import TUI
        
        bold = TUI._bold("test")
        
        self.assertIn("test", bold)
    
    def test_detect_platform(self):
        """测试平台检测"""
        from src.tui import ScreenshotTool
        
        platform = ScreenshotTool.detect_platform()
        
        self.assertIn(platform, ['macos', 'windows', 'linux', 'linux_scrot'])


class TestScreenshotTool(unittest.TestCase):
    """截图工具测试"""
    
    def test_get_screenshot_command_macos(self):
        """测试macOS截图命令"""
        from src.tui import ScreenshotTool
        
        cmd, desc = ScreenshotTool.get_screenshot_command('macos')
        
        self.assertEqual(cmd[0], 'screencapture')
        self.assertIn('macOS', desc)
    
    def test_get_screenshot_command_linux(self):
        """测试Linux截图命令"""
        from src.tui import ScreenshotTool
        
        cmd, desc = ScreenshotTool.get_screenshot_command('linux')
        
        self.assertEqual(cmd[0], 'gnome-screenshot')


class TestScreenGraphVision(unittest.TestCase):
    """主类测试"""
    
    def test_init_without_config(self):
        """测试无配置初始化"""
        from src.screengraph_vision import ScreenGraphVision
        
        app = ScreenGraphVision()
        
        self.assertIsNotNone(app.config)
        self.assertIsNone(app.client)
    
    def test_init_with_config(self):
        """测试有配置初始化"""
        from src.screengraph_vision import ScreenGraphVision
        from src.config import Config
        
        config = Config()
        config.api_key = "test_key"
        
        app = ScreenGraphVision(config)
        
        self.assertIsNotNone(app.client)


if __name__ == '__main__':
    unittest.main()
