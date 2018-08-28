#!/usr/bin/env python
# coding: utf-8


from time import sleep
import os
import paramiko
client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname="192.168.58.133", port=22, username="root", password="xia_2366", timeout=10)

# stdin, stdout, stderr = client.exec_command('date')
# 块数据
# stdin, stdout, stderr = client.exec_command('echo `date` > /tmp/time_range.txt; cat /tmp/test.txt; echo `date` >> /tmp/time_range.txt;')
# 不死进程
# stdin, stdout, stderr = client.exec_command('bash /tmp/interval.sh; cat /tmp/interval.txt')
# 到点即挂进程
# stdin, stdout, stderr = client.exec_command('bash /tmp/sent_n_msg.sh')
# 持续运行进程
stdin, stdout, stderr = client.exec_command('bash /tmp/run.sh')

data = stdout.read() + stderr.read()

f = open(r'D:\test.txt', 'w')
f.write(data)
f.close()

print(len(data))
print(type(data))


# sleep(4)


print(data)

client.close()

os.system('pause')
