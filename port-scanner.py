import socket
import concurrent.futures

def scan_port(ip, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5) 
        
        
        if s.connect_ex((ip, port)) == 0:
            return port
    return None

def run_scanner(ip):
    open_ports = []
    print(f"Scanning target: {ip} (Ports 1-1000)...\n")
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)
        # Submit tasks to the thread pool
    futures = {executor.submit(scan_port, ip, port): port for port in range(1, 1001)}
        
        # as_completed yields futures as soon as they finish, rather than waiting for all
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result is not None:
            print(f"[+] Port {result} is OPEN")
            open_ports.append(result)
    executor.shutdown(wait=True)            
    print("\nScan complete.")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    run_scanner(target_ip)
