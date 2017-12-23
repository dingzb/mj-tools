from PyQt4 import QtCore

import paramiko


class Connection:
    def __init__(self, hostname, port, username, password):
        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password
        self.__ssh_client = paramiko.SSHClient()
        self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__connectThread = Connect(self)

    def save(self):
        pass

    def open(self, set_msg):
        self.__connectThread.msg_signal.connect(set_msg)
        self.__connectThread.start()

    def close(self):
        self.__ssh_client.close()

    def exec_cmd(self, cmd):
        self.__ssh_client.exec_command(cmd)

    def is_open(self):
        pass
        # self.sshClient.

    def get_ssh_client(self):
        return self.__ssh_client

    def get_hostname(self):
        return self.__hostname

    def get_port(self):
        return self.__port

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_connection_tuple(self):
        return {
            "hostname": self.__hostname,
            "port": self.__port,
            "username": self.__username,
            "password": self.__password
        }


class BaseToolsThread(QtCore.QThread):
    msg_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def emit_msg_signal(self, o):
        self.msg_signal.emit(str(o))


class Connect(BaseToolsThread):

    def __init__(self, connection):
        QtCore.QThread.__init__(self)
        self._connection = connection

    def run(self):
        self.emit_msg_signal(str.format("Connecting [{:s}:{:d}] ...", self._connection.get_hostname(), self._connection.get_port()))
        try:
            self._connection.get_ssh_client().connect(**self._connection.get_connection_tuple())
            self.emit_msg_signal("Connected.")
        except Exception, e:
            self.emit_msg_signal(e)