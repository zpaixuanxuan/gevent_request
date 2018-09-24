import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()

def downloader(img_name,img_url):
    req=urllib.request.urlopen(img_url)
    img_content=req.read()
    with open(img_name,"wb") as f:
        f.write(img_content)
def main():
    gevent.joinall([
        gevent.spawn(downloader,"1.jpg","https://rpic.douyucdn.cn/live-cover/appCovers/2018/08/26/5438345_20180826164935_small.jpg"),
        gevent.spawn(downloader,"2.jpg","https://rpic.douyucdn.cn/live-cover/appCovers/2018/08/06/1975380_20180806122319_small.jpg"),
        gevent.spawn(downloader,"3.jpg","https://rpic.douyucdn.cn/live-cover/appCovers/2018/07/03/2161686_20180703215739_small.jpg"),
        gevent.spawn(downloader,"4.jpg","https://rpic.douyucdn.cn/asrpic/180924/4427237_5573225_3a7f4_2_1631.jpg" )
        ])


if __name__=='__main__':
    main()