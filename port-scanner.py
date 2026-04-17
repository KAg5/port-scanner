import socket
import concurrent.futures

def scan_port(ip, port):
    """
    Attempts to connect to a target IP and port.
    Returns the port number if open, otherwise None.
    """
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Time Complexity Optimization: 
        # A short timeout ensures we don't wait indefinitely for unresponsive ports.
        s.settimeout(0.5) 
        
        # connect_ex returns 0 if successful, an error code otherwise.
        # It is more efficient than a standard try/except block for connect()
        if s.connect_ex((ip, port)) == 0:
            return port
    return None

def run_scanner(ip):
    open_ports = []
    print(f"Scanning target: {ip} (Ports 1-1000)...\n")

    # Space Complexity Optimization: 
    # ThreadPoolExecutor reuses a fixed number of threads (max_workers=100).
    # This prevents memory exhaustion compared to spawning 1000 individual threads at once.
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # Submit tasks to the thread pool
        futures = {executor.submit(scan_port, ip, port): port for port in range(1, 1001)}
        
        # as_completed yields futures as soon as they finish, rather than waiting for all
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                print(f"[+] Port {result} is OPEN")
                open_ports.append(result)
                
    print("\nScan complete.")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    run_scanner(target_ip)