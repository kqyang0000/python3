import os

print('Process (%s) start...' % os.getpid())
pid = os.fork()
# 调用fork时会返回两个id，其中子进程永远返回0，父进程则返回子进程的id
if pid == 0:
    print('I\'m child process (%s), my parent process is (%s)' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process (%s)' % (os.getpid(), pid))
