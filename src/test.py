#!/usr/bin/python3
# coding=utf-8

from tools.index import ToolsClass

# 测试代码
if __name__ == "__main__":
    tools = ToolsClass()
    print(tools.call("readFile", {"filepath": "./example.txt"}))
    # tools.call("writeFile", {"filepath": "example7.txt", "content": "若干内容"})
