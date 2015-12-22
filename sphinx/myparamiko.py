
import paramiko

def myExec(ip,indexerbin,conf):
    from .models import sshinfo
    r = sshinfo.objects.get(pk=1)
    username = r.name
    password = r.password
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,username,password)
    stdin, stdout, stderr = ssh.exec_command("sudo "+indexerbin+" --config "+conf+" --all  --rotate")
    result = stdout.readlines()
    ssh.close()
    return result
