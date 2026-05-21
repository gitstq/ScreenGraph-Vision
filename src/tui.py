#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScreenGraph-Vision TUI 界面模块
Terminal User Interface Module
"""

import os
import sys
import subprocess
from typing import Optional, Callable


class TUI:
    """终端UI渲染器"""
    
    # ANSI 颜色代码
    COLORS = {
        'reset': '\033[0m',
        'bold': '\033[1m',
        'dim': '\033[2m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    
    # 进度条字符
    PROGRESS_CHARS = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    @classmethod
    def clear_screen(cls):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @classmethod
    def print_header(cls, title: str, subtitle: str = None):
        """打印标题"""
        width = 70
        print()
        print(cls._colored("═" * width, 'cyan'))
        print(cls._colored(f"  {cls._bold(title)}", 'cyan'))
        if subtitle:
            print(cls._colored(f"  {subtitle}", 'dim'))
        print(cls._colored("═" * width, 'cyan'))
        print()
    
    @classmethod
    def print_banner(cls):
        """打印Banner"""
        banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║   ███████╗██╗███╗   ██╗██╗  ██╗██╗  ██╗            ║
    ║   ██╔════╝██║████╗  ██║██║ ██╔╝╚██╗██╔╝            ║
    ║   ███████╗██║██╔██╗ ██║█████╔╝  ╚███╔╝             ║
    ║   ╚════██║██║██║╚██╗██║██╔═██╗  ██╔██╗             ║
    ║   ███████║██║██║ ╚████║██║  ██╗██╔╝ ██╗            ║
    ║   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝            ║
    ║                                                       ║
    ║   Vision - 屏幕截图智能分析引擎                       ║
    ║   Screen Screenshot Intelligent Analysis Engine       ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
        """
        print(cls._colored(banner, 'cyan'))
    
    @classmethod
    def print_menu(cls, options: list, title: str = "功能菜单"):
        """打印菜单"""
        print(f"\n📋 {cls._bold(title)}")
        print("-" * 50)
        for i, (key, desc) in enumerate(options, 1):
            print(f"  {cls._colored(f'[{i}]', 'yellow')} {desc}")
        print("-" * 50)
    
    @classmethod
    def print_result(cls, title: str, content: str, success: bool = True):
        """打印结果"""
        status = cls._colored("✅ 成功", 'green') if success else cls._colored("❌ 失败", 'red')
        print(f"\n{status} {cls._bold(title)}")
        print("-" * 60)
        
        # 格式化输出内容
        if isinstance(content, str):
            lines = content.split('\n')
            for line in lines:
                print(f"  {line}")
        else:
            print(f"  {content}")
        
        print("-" * 60)
    
    @classmethod
    def print_progress(cls, current: int, total: int, prefix: str = "处理中"):
        """打印进度条"""
        percent = current / total if total > 0 else 0
        filled = int(percent * 30)
        bar = '█' * filled + '░' * (30 - filled)
        char_idx = current % len(cls.PROGRESS_CHARS)
        
        sys.stdout.write(
            f'\r{cls.PROGRESS_CHARS[char_idx]} {prefix}: |{bar}| {int(percent * 100)}%'
        )
        sys.stdout.flush()
        
        if current >= total:
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.flush()
    
    @classmethod
    def print_error(cls, message: str):
        """打印错误信息"""
        print(f"\n{cls._colored('❌ 错误:', 'red')} {message}")
    
    @classmethod
    def print_warning(cls, message: str):
        """打印警告信息"""
        print(f"\n{cls._colored('⚠️  警告:', 'yellow')} {message}")
    
    @classmethod
    def print_info(cls, message: str):
        """打印信息"""
        print(f"\n{cls._colored('ℹ️  信息:', 'blue')} {message}")
    
    @classmethod
    def print_success(cls, message: str):
        """打印成功信息"""
        print(f"\n{cls._colored('✅ 成功:', 'green')} {message}")
    
    @classmethod
    def get_input(cls, prompt: str, default: str = None) -> str:
        """获取用户输入"""
        if default:
            value = input(f"{prompt} [{default}]: ").strip()
            return value if value else default
        return input(f"{prompt}: ").strip()
    
    @classmethod
    def get_choice(cls, options: list, prompt: str = "请选择") -> int:
        """获取用户选择"""
        while True:
            try:
                choice = int(cls.get_input(prompt, "1"))
                if 1 <= choice <= len(options):
                    return choice
                cls.print_warning(f"请输入 1-{len(options)} 之间的数字")
            except ValueError:
                cls.print_warning("请输入有效的数字")
    
    @classmethod
    def confirm(cls, message: str, default: bool = False) -> bool:
        """确认提示"""
        suffix = "[Y/n]" if default else "[y/N]"
        response = input(f"{message} {suffix}: ").strip().lower()
        
        if not response:
            return default
        return response in ['y', 'yes', '是']
    
    @classmethod
    def _colored(cls, text: str, color: str) -> str:
        """给文本添加颜色"""
        color_code = cls.COLORS.get(color, '')
        return f"{color_code}{text}{cls.COLORS['reset']}"
    
    @classmethod
    def _bold(cls, text: str) -> str:
        """加粗文本"""
        return f"{cls.COLORS['bold']}{text}{cls.COLORS['reset']}"


class ScreenshotTool:
    """跨平台截图工具"""
    
    @staticmethod
    def get_screenshot_command(platform: str = None) -> tuple:
        """
        获取截图命令
        
        Returns:
            (command_list, description)
        """
        if platform is None:
            platform = ScreenshotTool.detect_platform()
        
        commands = {
            'macos': {
                'cmd': ['screencapture', '-x', '-i', '-s', '-P'],
                'temp': '/tmp/screenshot.png',
                'desc': 'macOS截图工具'
            },
            'linux': {
                'cmd': ['gnome-screenshot', '-a', '-f'],
                'temp': '/tmp/screenshot.png',
                'desc': 'GNOME截图工具'
            },
            'linux_scrot': {
                'cmd': ['scrot', '-s'],
                'temp': '/tmp/screenshot.png',
                'desc': 'Scrot截图工具'
            },
            'windows': {
                'cmd': ['powershell', '-Command', 'Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Clipboard]::GetImage().Save("$env:TEMP\\screenshot.png")'],
                'temp': f'{os.environ.get("TEMP", "/tmp")}/screenshot.png',
                'desc': 'Windows截图工具'
            }
        }
        
        return commands.get(platform, commands['macos'])
    
    @staticmethod
    def detect_platform() -> str:
        """检测操作系统"""
        if sys.platform == 'darwin':
            return 'macos'
        elif sys.platform == 'win32':
            return 'windows'
        elif sys.platform == 'linux':
            # 进一步检测Linux桌面环境
            desktop = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
            if 'gnome' in desktop or 'gtk' in desktop:
                return 'linux'
            return 'linux_scrot'
        return 'macos'
    
    @staticmethod
    def take_screenshot(output_path: str = None) -> Optional[str]:
        """
        执行截图
        
        Args:
            output_path: 输出路径
        
        Returns:
            截图文件路径，失败返回None
        """
        platform = ScreenshotTool.detect_platform()
        cmd_info = ScreenshotTool.get_screenshot_command(platform)
        
        if output_path is None:
            output_path = cmd_info['temp']
        
        try:
            # macOS
            if platform == 'macos':
                cmd = cmd_info['cmd']
                cmd[-1] = output_path  # 替换为实际路径
                result = subprocess.run(cmd, capture_output=True, timeout=30)
                
            # Linux
            elif platform in ['linux', 'linux_scrot']:
                cmd = cmd_info['cmd']
                cmd.append(output_path)
                result = subprocess.run(cmd, capture_output=True, timeout=30)
                
            # Windows
            elif platform == 'windows':
                # Windows需要特殊处理
                ps_cmd = f'''
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen
$bitmap = New-Object System.Windows.Forms.Bitmap($screen.Bounds.Width, $screen.Bounds.Height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($screen.Bounds.Location, [System.Drawing.Point]::Empty, $screen.Bounds.Size)
$bitmap.Save("{output_path.replace('\\', '\\\\')}")
$graphics.Dispose()
$bitmap.Dispose()
'''
                result = subprocess.run(
                    ['powershell', '-Command', ps_cmd],
                    capture_output=True,
                    timeout=30
                )
            
            # 检查文件是否存在
            if os.path.exists(output_path):
                return output_path
            
            # 如果上面方法失败，尝试备选方案
            return ScreenshotTool._fallback_screenshot(output_path)
            
        except Exception as e:
            print(f"截图失败: {e}")
            return ScreenshotTool._fallback_screenshot(output_path)
    
    @staticmethod
    def _fallback_screenshot(output_path: str) -> Optional[str]:
        """备选截图方案 - 使用文件输入"""
        print("\n💡 提示: 请手动截图或提供图片文件路径")
        return None
