import httplib  

def saveHttpData(filename, url, host=None):

    if None == host:
        start = url.find('//') + 2
        end = url[start:].find('/')

        host = url[start:start+end]
        url = url[start+end:]

    print host, url, filename

    conn = httplib.HTTPConnection(host)  
    conn.request("GET", url)
    res = conn.getresponse()

    if 200 != res.status:
        print res.status, res.reason
        conn.close()
        return -1

    data = res.read()
    conn.close()

    fp = open(filename, 'w')
    fp.write(data)
    fp.close()

    return 0 

start = 26
size = 5
gids = [x for x in range(start, start + size)]

for gid in gids:
    '''
    ret = saveHttpData('%d.json' % gid, '/seckill/seckillList.json?gid=%d' % gid, 'coupon.m.jd.com')
    '''
    ret = saveHttpData('%d.json' % gid, 'http://coupon.m.jd.com/seckill/seckillList.json?gid=%d' % gid)
    print gid, ret

