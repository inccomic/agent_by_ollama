#!/usr/bin/python3
# coding=utf-8

from os import getcwd, path


def writeFile(filepath, content, mode="w"):
    filepath_full = path.join(getcwd(), "data", filepath)
    with open(filepath_full, mode) as file:
        file.write(content)
    return "写入成功"
