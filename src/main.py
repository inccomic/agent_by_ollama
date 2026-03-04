#!/usr/bin/python3
# coding=utf-8

import ollama


# 智能体对象
class AgentClass:
    def __init__(self, model="llama3.2"):
        self.model = model

    # 与模型进行对话
    def chat(self, message):
        result = ollama.generate(
            model=self.model, prompt=message  # 模型名称  # 提示文本
        )
        return result.response


# 回答对象
def doAsk(agent):
    task = input("请输入任务：")

    if task == "exit":
        print("再见")
    else:
        result = agent.chat(task)
        print(result)
        doAsk(agent)


# 运行
if __name__ == "__main__":
    agent = AgentClass()
    doAsk(agent)
