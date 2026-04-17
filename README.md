# TCP Port Scanner (Multithreaded)

A lightweight, high-performance Python script designed to scan the first 1000 TCP ports of a target IP address. This tool utilizes concurrent execution and optimized socket handling to deliver results in seconds.

## 🚀 Features
- **Multithreading:** Uses `ThreadPoolExecutor` to scan multiple ports simultaneously.
- **Optimized Performance:** Implements `connect_ex` for faster socket handshakes compared to standard exception-based handling.
- **Resource Efficient:** Employs a fixed worker pool to maintain a low memory footprint.

## 🛠️ Efficiency Breakdown
- **Time Complexity:** $O(\frac{P \times T}{N})$
  - $P$ = Number of ports (1000)
  - $T$ = Timeout (0.5s)
  - $N$ = Threads (100)
  - By distributing tasks, the scan time is reduced by approximately 90% compared to a sequential scan.
- **Space Complexity:** $O(N)$
  - Memory usage is capped by the number of threads ($N$), ensuring the script remains stable even on low-resource systems.

## 📋 Requirements
- Python 3.x
- Standard libraries (`socket`, `concurrent.futures`) — no external installations required.

## 📖 Usage
1. Run the script:
   ```bash
   python scanner.py
   ```
2. Enter the target IP (e.g., `127.0.0.1` or `192.168.1.1`).
3. View the list of open ports in real-time.

## ⚠️ Disclaimer
This tool is for educational and authorized security testing purposes only. Scanning targets without prior permission is illegal and unethical.
