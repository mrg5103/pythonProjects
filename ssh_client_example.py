

import paramiko

hostname = 'localhost'
port = 22
username = 'example'
password = 'password'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')  #prints ifconfig and exits, can be cusotmised
    print stdout.read()
    s.close()
