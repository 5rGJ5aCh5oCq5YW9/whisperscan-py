import re
import requests
from Queue import Queue
import threading
import sys
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}



class BaiduUrlSpider(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
            try:
                self.spider(url)
            except Exception,e:
                print e
                pass
    def spider(self,url):
        r = requests.get(url=url,headers=headers)
        soup = bs(r.content,'lxml')
        urls = soup.find_all(name='a',attrs={'data-click':re.compile('.'),'class':None})
        for url in urls:
            get_url = requests.get(url=url['href'],headers=headers,timeout=8)
            if get_url.status_code == 200:
                url_para = get_url.url
                url_index_tmp = url_para.split('/')
                url_index = url_index_tmp[0]+'//'+url_index_tmp[2]
                f1 = open('out_para.txt','a+')
                f1.write(url_para+'\n')
                f1.close()
                with open('out_index.txt') as f:
                    if url_index in f.read():
                        f2 =open('out_index','a+')
                        f2.write(url_index+'\n')
                        f2.close()




def main(keyword,thread_count):
    queue = Queue()
    for i in range(0,750,10):
        queue.put( 'https://www.baidu.com/s?wd=%s&pn=%s&rn=50'%(keyword,str(i)))
    threads = []
    thread_count = 10
    for i in range(thread_count):
        threads.append(BaiduUrlSpider(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    if len(sys.argv) !=3:
        print 'Enter:%s keyword thread_count'%sys.argv[0]
        sys.exit(-1)
    else:
        main(sys.argv[1],sys.argv[2])


