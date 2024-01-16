import argparse
import socket
import threading
from colorama import Fore, Style, init

init(autoreset=True)

def get_service(port):
    try:
        service = socket.getservbyport(port)
        return service
    except (socket.error, OSError):
        return "Unknown"

def scan_port(ip, port):
    try:
        sock = socket.create_connection((ip, port), timeout=1)
        service = get_service(port)
        print(f"[+] Port {port} - {service} is {Fore.GREEN}open{Style.RESET_ALL}")
        sock.close()
    except (socket.timeout, socket.error):
        pass

def scan_ip(ip, ports):
    print(f"[~] Scanning ports for {ip}...")
    threads = []

    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def parse_ip_range(ip_range):
    try:
        start, end = ip_range.split('-')[0], ip_range.split('-')[1]

        start_parts = list(map(int, start.split('.')[-1].split('.')))
        end_parts = list(map(int, end.split('.')[-1].split('.')))

        ip_list = [f"{start.split('.')[0]}.{start.split('.')[1]}.{start.split('.')[2]}.{i}" for i in range(start_parts[0], end_parts[0] + 1)]
        return ip_list
    except ValueError as e:
        print(f"{Fore.RED}[!] Invalid IP address range. Error: {e}{Style.RESET_ALL}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner tool.")
    parser.add_argument("-ip", help="Single IP address to scan.")
    parser.add_argument("-iprange", help="IP address range to scan (e.g., 192.168.0.1-52).")
    args = parser.parse_args()

    if not args.ip and not args.iprange:
        print(f"{Fore.RED}[!] Please provide either -ip or -iprange parameter.{Style.RESET_ALL}")
        return

    if args.ip:
        ip_list = [args.ip]
    elif args.iprange:
        ip_list = parse_ip_range(args.iprange)

    # source: https://github.com/pha5matis/Pentesting-Guide/blob/master/list_of_common_ports.md
    ports = [21, 22, 23, 25, 69, 80, 88, 110, 111, 119, 135, 139, 143, 161, 162, 389, 443, 445, 587, 631, 636, 993, 1433, 1521, 2049, 3306, 3339, 3389, 8080, 8000, 8443]  # You can customize this list

    for ip in ip_list:
        scan_ip(ip, ports)

if __name__ == "__main__":
    main()
