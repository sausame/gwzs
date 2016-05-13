import os, random, sys, time

from ware import WareItem
from js import PriceInfo
from source import SeckillInfo
from network import saveHttpData
from parser import parsePriceHistory

class WareManager:

    def __init__(self):
        self.wareList = []
        os.mkdir('data')

    def initWareList(self):

        # Update from Jd
        self.updateJdWareList()

    def updateJdWareList(self):

        start = 26
        size = 1
        gids = [x for x in range(start, start + size)]

        for gid in gids:
            path = 'data/%d.json' % gid

            ret = saveHttpData(path, 'http://coupon.m.jd.com/seckill/seckillList.json?gid=%d' % gid)

            if ret < 0: continue

            seckillInfo = SeckillInfo(path)

            for item in seckillInfo.itemList:

                wItem = WareItem()
                wItem.setSeckillItem(item)

                self.wareList.append(wItem)

            # os.remove(path)

    def updatePriceHistories(self):

        for ware in self.wareList:

            # Get URL for price history
            url = ""

            with PriceInfo('0.js') as priceInfo: 
                url = priceInfo.execute(ware.name, ware.url);

            # Get price histories
            path = 'data/{}.js'.format(ware.wid)
            ret = saveHttpData(path, url)

            # Parse
            historyData = parsePriceHistory(path)

            if historyData:
                ware.setHistories(historyData.histories)

            # os.remove(path)

            print ware

            # Sleep for a while
            time.sleep(random.random())


'''
Main entrance
'''

reload(sys)
sys.setdefaultencoding('utf8')

manager = WareManager()
manager.initWareList()
manager.updatePriceHistories()

