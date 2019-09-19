from multiprocessing import Process
import os


def run_test(name):
    print('run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('parent process is (%s)' % os.getpid())
    c = Process(target=run_test, args=('test',))
    print('Child process will start')
    c.start()
    c.join()
    print('Child process end')
