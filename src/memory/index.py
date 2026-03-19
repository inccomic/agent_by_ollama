#!/usr/bin/python3
# coding=utf-8

from skills.loadSummary import loadSummary


# 记忆功能
class MemoryClass:
    def __init__(self):
        # 先不考虑长期记忆
        # 前置加载skills概述
        self.messages = [loadSummary()]

    def valueOf(self):
        return self.messages

    def addMessage(self, message):
        return self.messages.append(message)
