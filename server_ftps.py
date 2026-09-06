from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Virtual User Database Initialization
authorizer = DummyAuthorizer()

path_client1 = "/data/data/com.termux/files/home/storage/shared/ClientStorage1"
path_client2 = "/data/data/com.termux/files/home/storage/shared/ClientStorage2"

# perm="elradfmwMT" means the client has full access (Read, Write, Delete, etc.)
authorizer.add_user("username1", "password1", path_client1, perm="elradfmwMT")
authorizer.add_user("username2", "password2", path_client2, perm="elradfmwMT")

# TLS/SSL Configuration (FTPS)
handler = TLS_FTPHandler
handler.certfile = "/data/data/com.termux/files/home/tls.crt"
handler.keyfile = "/data/data/com.termux/files/home/tls.key"
handler.authorizer = authorizer

handler.tls_control_required = True
handler.tls_data_required = True

handler.passive_ports = range(60000, 60100)

handler.masquerade_address = "192.168.1.10"

server = FTPServer(("0.0.0.0", 8021), handler)
print("Success! The FTPS server is running on Port 8021")
server.serve_forever()