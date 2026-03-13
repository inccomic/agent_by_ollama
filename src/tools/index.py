#!/usr/bin/python3
# coding=utf-8

from .voiceIt import voiceIt
from .readFile import readFile
from .writeFile import writeFile


# 可用工具箱
class ToolsClass:
    def __init__(self):
        pass

    # 注册当前可用工具
    # https://docs.ollama.com/api/chat#body-tools
    def valueOf(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "readFile",  # 方法名称
                    "description": "读取文件中的内容",  # 描述这个方法有什么功能
                    "parameters": {  # 调用这个方法需要的参数
                        "type": "object",
                        "properties": {
                            "filepath": {  # 参数一
                                "type": "string",  # 参数类型
                                "description": "需要读取文件的全路径",  # 参数描述
                            }
                        },
                        "required": ["filepath"],  # 哪些是必须参数
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "writeFile",
                    "description": "在指定文件中写入内容",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "filepath": {
                                "type": "string",
                                "description": "需要写入文件的全路径",
                            },
                            "content": {
                                "type": "string",
                                "description": "需要写入的内容",
                            },
                            "mode": {
                                "type": "string",
                                "description": "写入模式",
                                "enum": ["w", "a"],  # 写入模式 (w)、追加模式 (a)
                            },
                        },
                        "required": ["filepath", "content"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "voiceIt",
                    "description": "语音朗读文本内容",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "content": {
                                "type": "string",
                                "description": "需要朗读的内容",
                            },
                        },
                        "required": ["content"],
                    },
                },
            },
        ]

    # 执行具体工具
    def call(self, toolName, toolArguments):
        if toolName == "voiceIt":
            return voiceIt(**toolArguments)
        elif toolName == "readFile":
            return readFile(**toolArguments)
        elif toolName == "writeFile":
            return writeFile(**toolArguments)
        else:
            return "Unknown tool"
