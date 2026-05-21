#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScreenGraph-Vision - 轻量级终端屏幕截图智能分析引擎
Lightweight Terminal Screen Screenshot Intelligent Analysis Engine

基于GLM-5.1多模态能力实现屏幕截图自动描述、UI元素识别、可访问性树分析等功能

Author: gitstq
License: MIT
Version: 1.0.0
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional

from .config import Config
from .api_client import GLMClient
from .tui import TUI, ScreenshotTool


class ScreenGraphVision:
    """ScreenGraph-Vision 主类"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.client: Optional[GLMClient] = None
        
        if self.config.is_configured():
            self._init_client()
    
    def _init_client(self):
        """初始化API客户端"""
        self.client = GLMClient(
            api_key=self.config.api_key,
            base_url=self.config.get("api_base_url"),
            model=self.config.get("model", "glm-4v-plus")
        )
    
    def configure(self):
        """配置向导"""
        TUI.clear_screen()
        TUI.print_header("ScreenGraph-Vision 配置向导")
        
        print("\n📝 请配置您的GLM API密钥")
        print("   (可前往 https://open.bigmodel.cn/ 注册获取)\n")
        
        api_key = input("请输入API密钥: ").strip()
        
        if not api_key:
            TUI.print_error("API密钥不能为空")
            return False
        
        self.config.api_key = api_key
        self.config.save()
        
        TUI.print_success("配置已保存!")
        
        # 验证配置
        self._init_client()
        if self.client:
            TUI.print_info("API连接测试...")
            TUI.print_success("配置完成!")
        
        return True
    
    def analyze_file(self, image_path: str, analysis_type: str = "general") -> bool:
        """
        分析图片文件
        
        Args:
            image_path: 图片路径
            analysis_type: 分析类型
        
        Returns:
            是否成功
        """
        if not self.client:
            TUI.print_error("请先配置API密钥")
            return False
        
        if not os.path.exists(image_path):
            TUI.print_error(f"文件不存在: {image_path}")
            return False
        
        # 确定分析类型
        type_map = {
            "1": "general",
            "2": "ui",
            "3": "accessibility",
            "4": "diff"
        }
        
        if analysis_type not in type_map.values():
            analysis_type = type_map.get(analysis_type, "general")
        
        # 显示分析类型
        type_names = {
            "general": "通用描述",
            "ui": "UI元素分析",
            "accessibility": "可访问性分析",
            "diff": "差异对比"
        }
        
        TUI.print_info(f"正在使用 [{type_names.get(analysis_type, '通用描述')}] 模式分析...")
        
        # 执行分析
        print("🔄 正在分析截图，请稍候...")
        
        result = self.client.analyze_screenshot(
            image_path=image_path,
            analysis_type=analysis_type
        )
        
        if result.get("success"):
            TUI.print_result("分析结果", result.get("content", ""), success=True)
            return True
        else:
            TUI.print_error(result.get("error", "未知错误"))
            return False
    
    def capture_and_analyze(self, analysis_type: str = "general") -> bool:
        """
        截图并分析
        
        Args:
            analysis_type: 分析类型
        
        Returns:
            是否成功
        """
        TUI.print_info("正在截图...")
        
        # 生成截图文件路径
        temp_path = "/tmp/screengraph_vision_screenshot.png"
        
        # 执行截图
        screenshot_path = ScreenshotTool.take_screenshot(temp_path)
        
        if not screenshot_path or not os.path.exists(screenshot_path):
            TUI.print_error("截图失败，请手动提供图片文件")
            return False
        
        TUI.print_success(f"截图已保存: {screenshot_path}")
        
        # 分析截图
        return self.analyze_file(screenshot_path, analysis_type)
    
    def interactive_mode(self):
        """交互式模式"""
        while True:
            TUI.clear_screen()
            TUI.print_banner()
            
            options = [
                ("1", "📷 截图并分析 (Capture & Analyze)"),
                ("2", "📁 分析图片文件 (Analyze Image File)"),
                ("3", "⚙️  配置设置 (Configuration)"),
                ("4", "ℹ️  显示配置 (Show Config)"),
                ("5", "🚪 退出 (Exit)")
            ]
            
            TUI.print_menu(options)
            
            choice = TUI.get_input("\n请选择操作", "1")
            
            if choice == "1":
                self._interactive_capture()
            elif choice == "2":
                self._interactive_file()
            elif choice == "3":
                self.configure()
                input("\n按Enter键继续...")
            elif choice == "4":
                self.config.print_config()
                input("\n按Enter键继续...")
            elif choice == "5":
                TUI.print_success("感谢使用 ScreenGraph-Vision!")
                break
            else:
                TUI.print_warning("无效选择，请重新输入")
                input("\n按Enter键继续...")
    
    def _interactive_capture(self):
        """交互式截图分析"""
        print("\n📷 截图分析模式")
        print("-" * 50)
        
        type_options = [
            ("1", "通用描述 (General Description)"),
            ("2", "UI元素分析 (UI Elements Analysis)"),
            ("3", "可访问性分析 (Accessibility Analysis)"),
            ("4", "差异对比 (Difference Comparison)")
        ]
        
        TUI.print_menu(type_options, "分析类型")
        choice = TUI.get_choice(type_options)
        
        type_map = {1: "general", 2: "ui", 3: "accessibility", 4: "diff"}
        analysis_type = type_map.get(choice, "general")
        
        self.capture_and_analyze(analysis_type)
        input("\n按Enter键继续...")
    
    def _interactive_file(self):
        """交互式文件分析"""
        print("\n📁 图片文件分析模式")
        print("-" * 50)
        
        image_path = TUI.get_input("请输入图片文件路径")
        
        if not os.path.exists(image_path):
            TUI.print_error("文件不存在")
            input("\n按Enter键继续...")
            return
        
        type_options = [
            ("1", "通用描述 (General Description)"),
            ("2", "UI元素分析 (UI Elements Analysis)"),
            ("3", "可访问性分析 (Accessibility Analysis)"),
            ("4", "差异对比 (Difference Comparison)")
        ]
        
        TUI.print_menu(type_options, "分析类型")
        choice = TUI.get_choice(type_options)
        
        type_map = {1: "general", 2: "ui", 3: "accessibility", 4: "diff"}
        analysis_type = type_map.get(choice, "general")
        
        self.analyze_file(image_path, analysis_type)
        input("\n按Enter键继续...")
    
    def batch_analyze(self, image_dir: str, pattern: str = "*.png") -> bool:
        """
        批量分析目录中的图片
        
        Args:
            image_dir: 图片目录
            pattern: 文件匹配模式
        
        Returns:
            是否成功
        """
        if not self.client:
            TUI.print_error("请先配置API密钥")
            return False
        
        if not os.path.exists(image_dir):
            TUI.print_error(f"目录不存在: {image_dir}")
            return False
        
        # 获取所有图片文件
        from pathlib import Path
        images = list(Path(image_dir).glob(pattern))
        
        if not images:
            TUI.print_warning(f"目录中没有找到匹配 {pattern} 的图片")
            return False
        
        TUI.print_info(f"找到 {len(images)} 张图片，开始批量分析...")
        
        success_count = 0
        for i, image_path in enumerate(images, 1):
            TUI.print_progress(i, len(images), "批量分析")
            
            result = self.client.analyze_screenshot(
                image_path=str(image_path),
                analysis_type="general"
            )
            
            if result.get("success"):
                success_count += 1
                
                # 保存结果
                output_path = image_path.with_suffix('.txt')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"图片: {image_path.name}\n")
                    f.write("=" * 60 + "\n")
                    f.write(result.get("content", ""))
                
                TUI.print_result(f"分析完成", f"结果已保存: {output_path}", success=True)
        
        TUI.print_success(f"批量分析完成: {success_count}/{len(images)} 成功")
        return success_count > 0


def main():
    """主入口函数"""
    parser = argparse.ArgumentParser(
        description="ScreenGraph-Vision - 轻量级终端屏幕截图智能分析引擎",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  screengraph analyze <image_path>          # 分析图片文件
  screengraph capture                        # 截图并分析
  screengraph config                        # 配置API密钥
  screengraph batch <directory>             # 批量分析目录
  screengraph interactive                   # 交互式模式
        """
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='ScreenGraph-Vision 1.0.0'
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        default='interactive',
        choices=['analyze', 'capture', 'config', 'batch', 'interactive'],
        help='执行命令'
    )
    
    parser.add_argument(
        'path',
        nargs='?',
        help='图片路径或目录'
    )
    
    parser.add_argument(
        '--type', '-t',
        choices=['general', 'ui', 'accessibility', 'diff'],
        default='general',
        help='分析类型'
    )
    
    parser.add_argument(
        '--pattern', '-p',
        default='*.png',
        help='批量分析时的文件模式'
    )
    
    args = parser.parse_args()
    
    # 创建实例
    app = ScreenGraphVision()
    
    # 执行命令
    if args.command == 'interactive' or (not args.command and not args.path):
        app.interactive_mode()
    
    elif args.command == 'config':
        app.configure()
    
    elif args.command == 'analyze':
        if not args.path:
            print("错误: 请提供图片文件路径")
            sys.exit(1)
        app.analyze_file(args.path, args.type)
    
    elif args.command == 'capture':
        app.capture_and_analyze(args.type)
    
    elif args.command == 'batch':
        if not args.path:
            print("错误: 请提供目录路径")
            sys.exit(1)
        app.batch_analyze(args.path, args.pattern)


if __name__ == '__main__':
    main()
