"""
 # coding: utf-8
 # @Author：xiabo
 # @File : subprocess_popen.py
 # @Date ：2021/6/17 上午10:44
 
"""

'''
允许启动一个新进程，并连接到它们的输入/输出/错误管道，从而获取返回值
'''


import subprocess

def subprocess_popen(cmd):
    return subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).stdout.readlines()