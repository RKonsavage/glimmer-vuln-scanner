import socket
import ipaddress
import threading

# Ports to scan (common ports)
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = sock.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "No banner"
            print(f"[+] {ip}:{port} open - {banner}")
        sock.close()
    except Exception as e:
        print(f"Error scanning {ip}:{port} - {e}")

def scan_host(ip):
    for port in COMMON_PORTS:
        threading.Thread(target=scan_port, args=(ip, port)).start()

def main():
    target_network = input("Enter network to scan (e.g. 192.168.1.0/24): ")
    try:
        network = ipaddress.IPv4Network(target_network, strict=False)
        print(f"Scanning network: {network}")
        for ip in network.hosts():
            threading.Thread(target=scan_host, args=(str(ip),)).start()
    except ValueError:
        print("Invalid CIDR. Please enter a valid network like 192.168.0.0/24.")

if __name__ == "__main__":
    main()
