import socket

# Target IP (use your own machine)
target = "127.0.0.1"

# Ports to scan
ports = range(1, 1025)

print(f"Scanning {target}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

print("Scan complete!")