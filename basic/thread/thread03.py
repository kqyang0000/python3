from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s run %2f seconds' % (name, end - start))


if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    # Pool()默认参数为系统cpu核数
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('wait for all subProcess done...')
    # 当调用close()方法时就不能继续添加你的进程了
    p.close()
    # Pool()的join()方法会等待所有子进程执行结束，并且调用join()之前必须调用close()方法
    p.join()
    print('All subProcess done...')
