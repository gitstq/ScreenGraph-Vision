"""
ScreenGraph-Vision - 轻量级终端屏幕截图智能分析引擎
Lightweight Terminal Screen Screenshot Intelligent Analysis Engine

基于GLM-5.1多模态能力实现屏幕截图自动描述、UI元素识别、可访问性树分析等功能
"""

__version__ = "1.0.0"
__author__ = "gitstq"
__license__ = "MIT"

from .screengraph_vision import ScreenGraphVision
from .config import Config
from .api_client import GLMClient

__all__ = ["ScreenGraphVision", "Config", "GLMClient"]
