from django.shortcuts import render_to_response
from django.http import HttpResponse
import urllib
import json as simplejson
from models import WeiboData
import time
from sae.ext.storage import monkey
monkey.patch_all()
import sae.kvdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.core.mail import send_mail

def control(request):
    return render_to_response('fetchcontrol.html')

# def start(request):
#     access_token = "access_token=2.00rY3lkB0KHHdn87d63b219e0zgBmr"
#     resultHtml = urllib.urlopen("https://api.weibo.com/2/statuses/public_timeline.json?"
#                              + access_token + "&count=20")
#     result = simplejson.loads(resultHtml.read())
#     print len(result['statuses'])
#     for i in range(0, len(result['statuses'])):
#         c_statuses = result['statuses'][i]
#         statuses = WeiboData(reposts_count = c_statuses['reposts_count'],
#                 truncated = c_statuses['truncated'],
#                 text = c_statuses['text'],
#                 mid = c_statuses['mid'],
#                 attitudes_count = c_statuses['attitudes_count'],
#                 favorited = c_statuses['favorited'],
#                 idstr = c_statuses['idstr'],
#                 created_at = c_statuses['created_at'],
#                 comments_count = c_statuses['comments_count'],
#         )
#         statuses.save()
#     return HttpResponse(filter(c_statuses['text']))

def filter(r_str):
    return repr(r_str)

def startfetchtofile(request):
    kv = sae.kvdb.KVClient()
    weibofilename =  (time.strftime("%Y-%m-%d-%H-%M")) + '-weibo.txt'
    weibofile = open('/s/weibodata/'+weibofilename,'w')
    access_token = "access_token=2.00rY3lkB0KHHdn87d63b219e0zgBmr"
    resultHtml = urllib.urlopen("https://api.weibo.com/2/statuses/public_timeline.json?"
                             + access_token + "&count=200")
    if (resultHtml == ''):
        pass
    else:
        data = ''
        result = simplejson.loads(resultHtml.read())
        weibocount = len(result['statuses'])
        for i in range(0, len(result['statuses'])):
            data += result['statuses'][i]['text']+'\n'
        try:
            weibofile.write(data.encode('utf8'))
        except Exception ,e:
            pass
        finally:
            if (kv.get('TotalCount')!=None):
                total = kv.get('TotalCount') + weibocount
                kv.set('TotalCount',total)
            else:
                kv.set('TotalCount',weibocount)
            weibofile.close()
    return HttpResponse('success')

def test(request):
    f = open('/s/weibodata/2014-06-28-weibo.txt').read()
    return HttpResponse(f)

def mailtest(request):
    from sae.mail import send_mail

    return HttpResponse(send_mail("86464875@qq.com", "invite", "to tonight's party",
          ("smtp.163.com", 25, "tyanmain@163.com", "a294458", False)))



