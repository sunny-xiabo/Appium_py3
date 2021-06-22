"""
 # coding: utf-8
 # @Author：xiabo
 # @File : py_kill_process.py
 # @Date ：2021/6/18 下午3:47
 
"""

'''
清理appium进程
'''


import os
import signal
from untils.log import LOG, logger


@logger("清理appium进程")
class AppiumProcess(object):

    def __init__(self, cmd):
        self._cmd = cmd
        self._l = self._check_process()
        LOG.info(self._cmd)

    def _check_process(self):
        try:
            out = os.popen(self._cmd, 'r').read()
            return [tuple(line.split()) for line in out.splitlines()]
        except KeyboardInterrupt as e:
            pass
        except Exception as e:
            LOG.info(str(e))

    def kill_process(self):
        if self._l:
            command_dict = dict(zip(self._l[0], self._l[1]))
            pid = int(command_dict.get("PID"))
            try:
                os.kill(pid, signal.SIGKILL)
                LOG.info('已杀死pid为{}的进程'.format(pid))
                return True
            except OSError:
                LOG.info('没有appium此进程！！！')
        else:
            return None

    @property  #将一个方法当作属性使用
    def is_node_process(self):
        return self._l
