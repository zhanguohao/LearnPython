# -*- coding: utf-8 -*-

import logging
import getpass
import sys
import os

class MyLog(object):
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        logfilename = sys.argv[0][0:-3] + '.log'
        if not os.path.isfile(logfilename):
            os.system('touch %s' %logfilename)
        fommarter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        logHand = logging.FileHandler(logfilename)
        logHand.setFormatter(fommarter)
        logHand.setLevel(logging.ERROR)
        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(fommarter)
        self.logger.addHandler(logHand)
        self.logger.addHandler(logHandSt)


    def debug(self,msg):
       self.logger.debug(msg)

    def info(self,msg):
       self.logger.info(msg)

    def warn(self,msg):
       self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)

if __name__ == "__main__":
    mylog = MyLog()
    mylog.debug('I am a debuger')
    mylog.info('This is a info')
    mylog.warn('It\'s warning!')
    mylog.error("ERROR ERROR ERROR!!!")
    mylog.critical('DISASTER!!!!!!!!!!!!!!')