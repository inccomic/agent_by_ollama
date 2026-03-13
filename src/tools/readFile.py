#!/usr/bin/python3
# coding=utf-8

from os import getcwd, path


def readFile(filepath):
    filepath_full = path.join(getcwd(), "data", filepath)

    # 如果文件不存在
    if not path.exists(filepath_full):
        return "文件不存在"

    with open(filepath_full, "r") as file:
        return file.read()
