#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScreenGraph-Vision GLM API 客户端
GLM API Client Module
"""

import os
import json
import base64
import urllib.request
import urllib.error
import hashlib
from typing import Optional, Dict, Any


class GLMClient:
    """GLM API 客户端"""
    
    def __init__(self, api_key: str, base_url: str = None, model: str = "glm-4v-plus"):
        self.api_key = api_key
        self.base_url = base_url or "https://open.bigmodel.cn/api/paas/v4"
        self.model = model
        
        if not self.api_key:
            raise ValueError("❌ API密钥未设置，请先配置 GLM_API_KEY 或运行 'screengraph config'")
    
    def _encode_image_to_base64(self, image_path: str) -> str:
        """将图片编码为Base64"""
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def _get_cache_path(self, image_path: str, prompt: str) -> str:
        """获取缓存文件路径"""
        cache_key = hashlib.md5(f"{image_path}{prompt}".encode()).hexdigest()
        cache_dir = ".screengraph_cache"
        os.makedirs(cache_dir, exist_ok=True)
        return os.path.join(cache_dir, f"{cache_key}.json")
    
    def analyze_image(
        self,
        image_path: str,
        prompt: str,
        system_prompt: str = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        use_cache: bool = True
    ) -> Dict[str, Any]:
        """
        分析图片
        
        Args:
            image_path: 图片路径
            prompt: 分析提示词
            system_prompt: 系统提示词
            max_tokens: 最大token数
            temperature: 温度参数
            use_cache: 是否使用缓存
        
        Returns:
            分析结果字典
        """
        # 检查缓存
        if use_cache:
            cache_path = self._get_cache_path(image_path, prompt)
            if os.path.exists(cache_path):
                try:
                    with open(cache_path, 'r', encoding='utf-8') as f:
                        cached = json.load(f)
                        print("📦 使用缓存结果")
                        return cached
                except Exception:
                    pass
        
        # 编码图片
        image_base64 = self._encode_image_to_base64(image_path)
        
        # 构建消息
        messages = []
        
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                },
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        })
        
        # 构建请求
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        # 发送请求
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode('utf-8'),
                headers=headers,
                method='POST'
            )
            
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                
                # 提取响应内容
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                
                response_data = {
                    "success": True,
                    "content": content,
                    "model": self.model,
                    "usage": result.get("usage", {}),
                    "image_path": image_path,
                    "prompt": prompt
                }
                
                # 保存缓存
                if use_cache:
                    try:
                        with open(cache_path, 'w', encoding='utf-8') as f:
                            json.dump(response_data, f, ensure_ascii=False, indent=2)
                    except Exception:
                        pass
                
                return response_data
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else ""
            try:
                error_json = json.loads(error_body)
                error_msg = error_json.get("error", {}).get("message", error_body)
            except Exception:
                error_msg = error_body
            
            return {
                "success": False,
                "error": f"HTTP Error {e.code}: {error_msg}",
                "content": None
            }
            
        except urllib.error.URLError as e:
            return {
                "success": False,
                "error": f"网络错误: {str(e)}",
                "content": None
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"请求失败: {str(e)}",
                "content": None
            }
    
    def analyze_screenshot(
        self,
        image_path: str,
        analysis_type: str = "general"
    ) -> Dict[str, Any]:
        """
        分析截图（快捷方法）
        
        Args:
            image_path: 截图路径
            analysis_type: 分析类型 (general|ui|accessibility|diff)
        
        Returns:
            分析结果
        """
        prompts = {
            "general": "请详细描述这张截图的内容，包括主要元素、文字信息和整体布局。",
            "ui": """请分析这张UI截图，识别并列出所有可交互的UI元素，包括：
1. 按钮（Buttons）
2. 输入框（Input fields）
3. 链接（Links）
4. 菜单项（Menu items）
5. 图标按钮（Icon buttons）
请按位置从上到下、从左到右列出。""",
            "accessibility": """请分析这张截图的可访问性特征：
1. 主要内容和功能
2. 文本内容的可读性评估
3. 色彩对比度评估
4. 潜在的可访问性问题
5. 改进建议""",
            "diff": """请比较这张截图与之前的版本，描述：
1. 新增的元素
2. 删除的元素
3. 变化的元素
4. 整体布局变化"""
        }
        
        system_prompts = {
            "general": "你是一个专业的图片描述助手，能够准确、详细地描述图片内容。",
            "ui": "你是一个专业的UI分析师，擅长识别和分析用户界面元素。",
            "accessibility": "你是一个专业的可访问性专家，评估界面的可访问性特征。",
            "diff": "你是一个专业的UI对比分析师，擅长发现界面变化。"
        }
        
        prompt = prompts.get(analysis_type, prompts["general"])
        system_prompt = system_prompts.get(analysis_type, system_prompts["general"])
        
        return self.analyze_image(
            image_path=image_path,
            prompt=prompt,
            system_prompt=system_prompt
        )
