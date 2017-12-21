from PyQt4 import QtCore

import paramiko


class SSHConnection(QtCore.QThread):
    def __init__(self, ip, port, user, password):
        super(SSHConnection, self).__init__()
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.sshClient = paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def open(self):
        self.sshClient.connect(self.ip, self.port, self.user, self.password)
        return self

    def close(self):
        self.sshClient.close()

    def exec_cmd(self, cmd):
        self.sshClient.exec_command(cmd)

    def is_open(self):
        pass
        # self.sshClient.