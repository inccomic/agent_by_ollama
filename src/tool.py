#!/usr/bin/python3
# coding=utf-8

from datetime import datetime


# 计算器工具
def calculate(params):
    try:
        expression = params.get("expression", "")
        result = eval(expression, {"__builtins__": {}}, {})
        return {"result": result, "expression": expression}
    except Exception as e:
        return {"error": str(e)}


calculate_info = "计算器(calculator)，使用例子：calculator({expression:'15 * 3 + 7'})"


# 天气查询工具（模拟）
def get_weather(params):
    location = params.get("location", "南京")
    return {"location": location, "weather": "晴朗", "temperature": "25°C"}


get_weather_info = "天气查询(weather)，使用例子：weather({location:'南京'})"


# 获取当前时间
def get_current_time():
    now = datetime.now()
    return {"time": now.strftime("%Y-%m-%d %H:%M:%S")}


get_current_time_info = "时间查询(time)，使用例子：time()"
