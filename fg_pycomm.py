#    Copyright 2015 Alexander Khoroshko

#    This file is part of fg-pycomm.
#    fg-pycomm is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    fg-pycomm is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with fg-pycomm.  If not, see <http://www.gnu.org/licenses/>.


print('hello')

if __name__ == '__main__':
    pass

import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 12345
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:"), data