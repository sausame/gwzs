import spidermonkey

def loadfile(filename):
    return open(filename).read()

class PriceInfo:

    def __init__(self, filename):
        self.rt = spidermonkey.Runtime()
        self.cx = self.rt.new_context()
        self.cx.add_global("loadfile", loadfile)
        self.fname = filename

    def execute(self, title, url):
        command = 'var contents = loadfile("{}"); eval(contents); var content = requestPriceInfo("{}", "{}"); content;'.format(
            self.fname, title, url)
        return self.cx.execute(command)

    def __enter__(self):  
        return self

    def __exit__(self, type, value, trace):
        pass

with PriceInfo('0.js') as priceInfo: 
    content = priceInfo.execute("Lebond", "http://item.jd.com/962374.html");
    print content
