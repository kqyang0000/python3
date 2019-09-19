import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code %s' % r)

print('\n')
print('\n')
print('\n')

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'setq=mx\npython.org\nexit\n')
print(output.decode('UTF-8'))
print('Exit code:', p.returncode)
