## pip3 install paramiko
import paramiko

ip = '192.168.205.6'

try:
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,
                    username='sabado',
                    password='sabado',
                    port='22'
                    )
except Exception as e:
    print('Erro:{}'.format(e))
    exit()

stdin, stdout, stderr = client.exec_command('ls -la')

if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))
