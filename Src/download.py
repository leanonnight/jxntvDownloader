from concurrent.futures import ThreadPoolExecutor
from requests import get, head
import time


class downloader:
    def __init__(self, url, num, name):
        self.url = url
        self.num = num
        self.name = name
        self.getsize = 0
        r = head(self.url, allow_redirects=True)
        self.size = int(r.headers['Content-Length'])

        print(self.name + " 总大小为: " + f'{self.size/1024/1024:6.2f}MB')

    def down(self, start, end, chunk_size=10240):
        headers = {'range': f'bytes={start}-{end}'}
        r = get(self.url, headers=headers, stream=True)
        with open(self.name, "rb+") as f:
            f.seek(start)
            for chunk in r.iter_content(chunk_size):
                f.write(chunk)
                self.getsize += len(chunk)

    def start(self):
        start_time = time.time()
        f = open(self.name, 'wb')
        f.truncate(self.size)
        f.close()
        tp = ThreadPoolExecutor(max_workers=self.num)
        futures = []
        start = 0
        for i in range(self.num):
            end = int((i+1)/self.num*self.size)
            future = tp.submit(self.down, start, end)
            futures.append(future)
            start = end+1
        while True:
            process = self.getsize/self.size*100
            last = self.getsize
            time.sleep(1)
            curr = self.getsize
            down = (curr-last)/1024
            if down > 1024:
                speed = f'{down/1024:6.2f}MB/s'
            else:
                speed = f'{down:6.2f}KB/s'
            print(self.name + " is downloading! " + "process: " + f'{process:6.2f}%' + " | " + "speed: " + speed)
            if process >= 100:
                print(self.name + " has been downloaded! " + "process: " + f'{100.00:6}%' + " | " + "speed:  00.00KB/s")
                break
        tp.shutdown()
        end_time = time.time()
        total_time = end_time-start_time
        average_speed = self.size/total_time/1024/1024
        print(self.name + " has been downloaded! " + " 总大小为: " + f'{self.size/1024/1024:6.2f}MB  ' + f'total-time: {total_time:.0f}s | average-speed: {average_speed:.2f}MB/s')


if __name__ == '__main__':
    url = 'http://video.yun.jxntv.cn/fs/livecut/20210730/qQEHmlez.mp4'
    down = downloader(url, 64, '都市情缘20210730 一生的寻找.mp4')
    down.start()