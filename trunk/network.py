import httplib  

def saveHttpData(host, url, filename):
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
    ret = saveHttpData('coupon.m.jd.com', '/seckill/seckillList.json?gid=%d' % gid, '%d.json' % gid)
    print gid, ret

