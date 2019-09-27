import psutil

count = psutil.cpu_count()
print('logical count:', count)
count = psutil.cpu_count(logical=False)
print('physic count:', count)
times = psutil.cpu_times()
print('free times:', times)

for i in range(10):
    print('cpu free:', psutil.cpu_percent(interval=1, percpu=True))

