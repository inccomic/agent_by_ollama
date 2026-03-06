#!/usr/bin/python3
# coding=utf-8

import ollama
import json
import os
from datetime import datetime
import re

from tool import (
    calculate,
    calculate_info,
    get_weather,
    get_weather_info,
    get_current_time,
    get_current_time_info,
)


# 智能体对象
class AgentClass:
    def __init__(self, model="llama3.2", memory_file="memory.json"):
        self.model = model
        self.memory_file = memory_file

        self.history = []  # 短期记忆：当前对话的上下文
        self.long_term_memory = []  # 长期记忆：用户偏好、个人信息等重要数据

        self.load_memory()

        self.tools = {  # 工具
            "calculator": calculate,
            "weather": get_weather,
            "time": get_current_time,
        }

    # 对话入口
    def chat(self, message):

        # 首先分析用户意图
        intent = self.analyze_intent(message)

        if intent["tool_needed"] and intent["tool"] in self.tools:
            tool_result = self.tools[intent["tool"]](intent["parameters"])
            return self.generate_response(message, tool_result, intent["tool"])
        else:
            return self.direct_chat(message)

    # 分析用户意图，决定是否需要使用工具
    def analyze_intent(self, message):
        prompt = f"""
        分析用户的请求，判断是否需要使用工具来完成。
        可用工具有：
            {calculate_info}
            {get_weather_info}
            {get_current_time_info}
        
        用户请求：{message}
        
        请用JSON格式回复，包含以下字段：
        - tool_needed: 布尔值，是否需要使用工具
        - tool: 如果需要工具，指定工具名称
        - parameters: 工具需要的参数
        
        示例回复：
        {{"tool_needed": true, "tool": "calculator", "parameters": {{"expression": "2+3*4"}}}}
        """

        result = ollama.generate(model=self.model, prompt=prompt)
        response = result.response

        # 提取JSON部分
        json_match = re.search(r"\{.*\}", response, re.DOTALL)

        if json_match:
            return json.loads(json_match.group())
        else:
            return {"tool_needed": False, "tool": "", "parameters": {}}

    # 基于工具结果生成回复
    def generate_response(self, user_msg, tool_result, tool_name):
        prompt = f"""
        用户请求：{user_msg}
        使用工具：{tool_name}
        工具结果：{json.dumps(tool_result, ensure_ascii=False)}
        
        请基于工具结果，用自然语言回复用户。
        """

        result = ollama.generate(model=self.model, prompt=prompt)
        response = result.response

        return response

    # 与模型进行对话
    def direct_chat(self, message):

        # 搜索相关记忆
        relevant_memories = self.search_memory(message)

        # 构建提示词
        memory_context = ""
        if relevant_memories:
            memory_context = (
                "相关记忆：\n"
                + "\n".join([f"- {m['content']}" for m in relevant_memories[-3:]])
                + "\n\n"
            )

        # 添加短期记忆（对话历史）
        history_context = self.get_recent_history()

        prompt = f"""
        {memory_context}
        当前对话历史：
        {history_context}
        
        用户：{message}
        助手：
        """

        result = ollama.generate(
            model=self.model, prompt=prompt  # 模型名称  # 提示文本
        )
        response = result.response

        # 历史记录起来
        self.add_to_history(message, response)

        # 如果用户提到了个人信息，添加到长期记忆
        if any(
            word in message.lower()
            for word in ["我的名字是", "我喜欢", "我住在", "我的工作是", "我是"]
        ):
            self.add_to_long_term_memory(message, "user_info")

        return response

    # 添加到对话历史
    def add_to_history(self, user_msg, agent_msg):
        self.history.append({"user": user_msg, "agent": agent_msg})

    # 获取最近的对话历史
    def get_recent_history(self):
        return "\n".join(
            [f"用户：{h['user']}\n助手：{h['agent']}" for h in self.history[-3:]]
        )

    # 添加到长期记忆
    # 把数据添加到long_term_memory + 保存长期记忆
    def add_to_long_term_memory(self, key_info, memory_type):
        memory_item = {
            "content": key_info,
            "timestamp": datetime.now().isoformat(),
            "type": memory_type,
        }
        self.long_term_memory.append(memory_item)
        self.save_memory()

    # 保存长期记忆
    # 把long_term_memory写入到磁盘中
    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.long_term_memory, f, ensure_ascii=False, indent=2)

    # 加载长期记忆
    # 把磁盘中的数据加载到long_term_memory
    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    self.long_term_memory = json.load(f)
            except:
                self.long_term_memory = []

    # 搜索相关记忆
    def search_memory(self, query):
        relevant_memories = []
        for memory in self.long_term_memory:
            # if any(
            #     keyword in memory["content"].lower()
            #     for keyword in query.lower().split()
            # ):
            #     relevant_memories.append(memory)
            relevant_memories.append(memory)
        return relevant_memories


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
