# [Agent 智能体](https://github.com/NN-Studio/agent_by_ollama)
基于Ollama搭建本地Agent（使用Python3开发）

<p>
    <a href="https://github.com/NN-Studio/agent_by_ollama" target='_blank'>
        <img alt="GitHub repo stars" src="https://img.shields.io/github/stars/NN-Studio/agent_by_ollama">
    </a>
    <a href="https://github.com/NN-Studio/agent_by_ollama">
        <img src="https://img.shields.io/github/forks/NN-Studio/agent_by_ollama" alt="forks">
    </a>
    <a href="https://github.com/NN-Studio/agent_by_ollama/issues">
        <img src="https://img.shields.io/github/issues/NN-Studio/agent_by_ollama" alt="issue">
    </a>
    <a href="https://gitee.com/NN-Studio/agent_by_ollama" target='_blank'>
        <img alt="Gitee repo stars" src="https://gitee.com/NN-Studio/agent_by_ollama/badge/star.svg">
    </a>
    <a href="https://gitee.com/NN-Studio/agent_by_ollama">
        <img src="https://gitee.com/NN-Studio/agent_by_ollama/badge/fork.svg" alt="forks">
    </a>
</p>

> 请确保完成了Ollama的安装，并完成了qwen3模型本地安装（ 相关内容可以查看 <a href="https://zxl20070701.github.io/notebook/index.html#/program/ai/ollama/install" target="_blank">《Ollama使用入门教程》</a> 进行学习）。

## 如何使用？

首先，进行依赖安装：

```
pip3 install -r requirements.txt
```

然后运行即可：

```
python3 ./src/main.py
```

## 目录结构

下面是主要文件说明：

```md
- data/ # 需要用到的数据
- skills/ # 若干skill技能
- src/
    - agent/ # 智能体对象
    - memory/ # 记忆功能
    - skills/ # 解析”skills技能“文件夹相关工具
    - tools/ # 工具
    - main.py # 代码入口
    - test.py # 若干测试代码
- requirements.txt 需要安装的依赖
```
## 版权

MIT License

Copyright (c) [zxl20070701](https://zxl20070701.github.io/notebook/home.html) 走一步，再走一步