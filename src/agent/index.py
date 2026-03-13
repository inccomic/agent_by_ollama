#!/usr/bin/python3
# coding=utf-8

from ollama import chat, ChatResponse
from memory.index import MemoryClass
from tools.index import ToolsClass


# 智能体对象
class AgentClass:
    def __init__(self, model):
        self.model = model
        self.memory = MemoryClass()  # 记忆
        self.tools = ToolsClass()  # 工具

    def run(self):
        message = input("用户说：")
        if message == "exit":
            print("退出程序...")
        else:
            self.chat(message)

    # 与模型进行对话
    def chat(self, message):
        self.memory.addMessage({"role": "user", "content": message})
        while True:
            response: ChatResponse = chat(
                model=self.model,
                messages=self.memory.valueOf(),
                tools=self.tools.valueOf(),
                think=True,
            )
            self.memory.addMessage(response.message)

            print("\n", response.message.thinking, "\n")
            print("智能体: ", response.message.content, "\n")

            if response.message.tool_calls:
                for tc in response.message.tool_calls:
                    tc_result = self.tools.call(tc.function.name, tc.function.arguments)
                    self.memory.addMessage(
                        {
                            "role": "tool",
                            "tool_name": tc.function.name,
                            "content": tc_result,
                        }
                    )

            else:
                break
        self.run()
