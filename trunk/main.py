from source import SeckillInfo
import sys


def parse(path):
    seckillInfo = SeckillInfo(path)
    return seckillInfo

'''
Main entrance
'''

reload(sys)
sys.setdefaultencoding('utf8')

info = parse('30.json')
print info

