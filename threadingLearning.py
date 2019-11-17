import threading

def work():
    return sum(i for i in range(100))

thread = threading.Thread(target=work)
thread.start()
thread.join()

from concurrent.futures import ThreadPoolExecutor as Executor

urls = """google twitter facebook youtube pinterest tumblr
instagram reddit flickr meetup classmates microsoft apple
linkedin xing renren disqus snapchat twoo whatsapp""".split()

# urls = """baidu xunlei""".split()
def fetch(url):
    from urllib import request,error
    try:
        data = request.urlopen(url,timeout=5).read()
        return '{}:length {}'.format(url,len(data))
    except :
        return '{}: {}'.format(url,'not available')

with Executor(max_workers=4) as exe:
    template = 'http://www.{}.com'
    jobs = [exe.submit(fetch,template.format(u)) for u in urls]
    results = [job.result() for job in jobs]

print('\n'.join(results))