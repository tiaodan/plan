from concurrent.futures import ThreadPoolExecutor, as_completed  # 线程池， 系统自带
import time

# 初始化
MAX_THREADS = 3  # 最大并发线程数
THREADPOOL = ThreadPoolExecutor(max_workers=MAX_THREADS)  # 线程池

# task1 = THREADPOOL.submit(spider, 1)  # 线程池添加任务,submit(方法名, (方法参数))
# task1.done()  # 是否结束
# task.result()  # 任务的返回值,即任务调用方法的返回值
# print(f'是否完成 {as_completed(task1)}')



