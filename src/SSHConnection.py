from PyQt4 import QtCore

import paramiko


class Connection:
    def __init__(self, ip, port, user, password):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.sshClient = paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def save(self):
        pass

    def open(self, setMsg):
        # self.sshClient.connect(self.ip, self.port, self.user, self.password)
        # return self
        connectThread = Connect(self)
        # connectThread.msgSignal.connect(setMsg)
        connectThread.start()

    def close(self):
        self.sshClient.close()

    def exec_cmd(self, cmd):
        self.sshClient.exec_command(cmd)

    def is_open(self):
        pass
        # self.sshClient.


class Connect(QtCore.QThread):
    msgSignal = QtCore.pyqtSignal(str)
    def __init__(self, _connection):
        super(Connect, self).__init__()
        self._connection = _connection

    def run(self):
        self.msgSignal.emit("Connecting...")
        try:
            self._connection.sshClient.connect(self._connection.ip, self._connection.port, self._connection.user, self._connection.password)
            self.msgSignal.emit("Connected.")
        except Exception, e:
            self.msgSignal.emit(str(e))
