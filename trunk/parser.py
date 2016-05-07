import json
import sys

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
        self.id = dictObj.pop("id")
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

class PriceHistory:

    def __init__(self, **kwargs):
        self.set(**kwargs)

    def set(self, **kwargs):
        for keyword in ["price", "time"]:
            setattr(self, keyword, kwargs[keyword])

    def __repr__(self):
        fields = ['    {}={!r}'.format(k, v)
            for k, v in self.__dict__.items() if not k.startswith("_")]

        return "  {}:\n{}".format(self.__class__.__name__, '\n'.join(fields))

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
            str = str + '{}\n'.format(history)

        return "{}:\n{}\n{}".format(self.__class__.__name__, '\n'.join(fields), str)

def parse(path):

    def getJsonString(path):

        fh = open(path)

        for line in fh.readlines(): 

            if len(line) > 1024:

                i = line.find('{')
                j = line.rfind('}')

                return line[i:j+1]

        return ""

    data = getJsonString(path)
    obj = json.loads(data)

    thisPrice = ThisPrice(obj['thisPrice'])
    print thisPrice

    thisItem = ThisItem(obj["thisItem"])
    print thisItem

    priceHistoryData = PriceHistoryData(obj["priceHistoryData"])
    print priceHistoryData


'''
Main entrance
'''

reload(sys)
sys.setdefaultencoding('utf8')

parse('../branch/data/toothbrush.js')

