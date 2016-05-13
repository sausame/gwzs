import json
import sys

from ware import PriceHistory

class ThisPrice:

    def __init__(self, dictObj):
        self.set(dictObj)

    def set(self, dictObj):
        self.price = dictObj.pop("price")
        self.priceunit = dictObj.pop("priceunit")
        self.priceunitSymbol = dictObj.pop("priceunitSymbol")
        self.available = dictObj.pop("available")
        self.updateTime = dictObj.pop("updateTime")

    def __repr__(self):
        fields = ['  {}={}'.format(k, v)
            for k, v in self.__dict__.items() if not k.startswith("_")]

        return "{}:\n{}".format(self.__class__.__name__, '\n'.join(fields))

        '''
        return 'ThisPrice: %d, %s, %s, %d, %d' % (self.price,
            self.priceunit,
            self.priceunitSymbol,
            self.available,
            self.updateTime)
        '''

class ThisItem:

    def __init__(self, dictObj):
        self.set(dictObj)

    def set(self, dictObj):
        self.itemId = dictObj.pop("id")
        self.price = dictObj.pop("price")
        self.updateTime = dictObj.pop("updateTime")
        self.cpsUrl = dictObj.pop("cpsUrl")
        self.categoryId = dictObj.pop("categoryId")
        self.name = dictObj.pop("name")
        self.rebate = dictObj.pop("rebate")
        self.available = dictObj.pop("available")
        self.shortName = dictObj.pop("shortName")
        self.url = dictObj.pop("url")
        self.priceImageUrl = dictObj.pop("priceImageUrl")

    def __repr__(self):
        fields = ['  {}={}'.format(k, v)
            for k, v in self.__dict__.items() if not k.startswith("_")]

        return "{}:\n{}".format(self.__class__.__name__, '\n'.join(fields))

class PriceHistoryData:

    def __init__(self, dictObj):
        self.set(dictObj)

    def set(self, dictObj):
        self.curTime = dictObj.pop("curTime")
        self.startTime = dictObj.pop("startTime")
        self.histories = [PriceHistory(**history) for history in dictObj["list"]]

    def __repr__(self):

        fields = ['  {}={!r}'.format(k, v)
            for k, v in self.__dict__.items() if not k.startswith("_") and 'histories' != k]

        str = ''
        for history in self.histories:
            str += '{}\n'.format(history)

        return "{}:\n{}\n{}".format(self.__class__.__name__, '\n'.join(fields), str)


def parsePriceHistory(path):

    def getJsonString(path):

        try:
            with open(path) as fh:

                for line in fh.readlines(): 

                    if len(line) > 1024:

                        start = line.find('{')
                        end = line.rfind('}')

                        return 0, line[start:end+1]

        except IOError:
            pass

        return -1, ""

    ret, data = getJsonString(path)

    if ret < 0:
        print 'Wrong format: {}'.format(path)
        return None

    obj = json.loads(data)

    '''
    thisPrice = ThisPrice(obj['thisPrice'])
    print thisPrice

    thisItem = ThisItem(obj["thisItem"])
    print thisItem
    '''

    try:
        return PriceHistoryData(obj["priceHistoryData"])
    except KeyError:
        pass

    return None


'''
Main entrance

reload(sys)
sys.setdefaultencoding('utf8')

parsePriceHistory('../branch/data/toothbrush.js')
'''

