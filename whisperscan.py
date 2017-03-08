import urllib2
import re

def get302URL(keyword,pagenumber):
    requesturl = "http://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=69C31E2567F24841&ie=utf-8&f=8&rsv_bp=1&tn=baiduadv&wd="+keyword+"&rn=50&pn="+pagenumber
    request = urllib2.Request(requesturl)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36')
    response = urllib2.urlopen(request)
    urltext= response.read()
    par = r'<div class="f13"><a target="_blank" href="(.+?)" class="c-showurl" style="text-decoration:none;">'
    pattern = re.compile(par)
    matchurl = re.findall(pattern,urltext,0)
    return matchurl

def getRealURL(url):
    opener = None
    try:
        opener = urllib2.urlopen(url,timeout=5)
        return opener.geturl()
    except:
        print "Request error url =" +url



if __name__ == '__main__':

    keyword = "inurl:php?id="
    pagenumber ="1"
    urllist = get302URL(keyword,pagenumber)
    realurllist = range(49)

    for i in range(len(urllist)):
        realurllist[i] = getRealURL(urllist[i])
    print  realurllist