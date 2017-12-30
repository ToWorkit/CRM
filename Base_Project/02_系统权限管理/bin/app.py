# -*- coding:utf-8 -*-

import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEDIR)
sys.path.append(BASEDIR)

from src import service

if __name__ == '__main__':
  service.execute()
