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

def parse_settings():

    return

def parse_input_xml( ):
    "this function parses xml with data settings"
    from xml.dom import minidom
    xmldoc = minidom.parse('../fg2comm.xml')
    print (xmldoc.toxml())
    return

if __name__ == '__main__':
    pass

import json, sys
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-s", "--settings", dest="settings_path", help="set path to settings files folder")
(options, args) = parser.parse_args()
print (options)
print (args)
try:
    print (options.settings_path)
except:
    print('No settings path given. Exiting')
    sys.exit(0)

import os.path
if not os.path.isdir(options.settings_path):
    print('Specified settings folder doesn\'t exist. Exiting')
    sys.exit(0)
settings_file_path = options.settings_path + 'settings.json'
from pprint import pprint
with open(settings_file_path) as settings_file:    
    data = json.load(settings_file)
pprint(data)

import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 12345
parse_input_xml();
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))



while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:"), data
    
