```markdown
# Python Port Scanner

A simple and efficient Python-based port scanner to identify open ports on a target system. Useful for network security audits and learning about network communication.

---

## Features
- Scans ports in the range of 1–65,535.
- Identifies open ports on the target machine.
- Displays real-time results for each open port.
- Customizable timeout settings for efficient scanning.

---

## Prerequisites
Make sure you have:
- Python 3.x installed.
- The following Python libraries:
  - `pyfiglet` (`pip install pyfiglet`)

---

## Installation
1. Clone the repository or download the script.
2. Install the required libraries:
   ```bash
   pip install pyfiglet
   ```

---

## Usage
1. Run the script:
   ```bash
   python port_scanner.py
   ```
2. Enter the target IP address or domain name when prompted.
3. View the results in real time as open ports are displayed.

---

## Example
```bash
Target IP: 192.168.1.1
Scanning Target: 192.168.1.1
Scanning Started at: 2024-12-22 14:45:30
--------------------------------------------------
[*] Port 22 is open
[*] Port 80 is open
```

---

## Disclaimer
This tool is intended for **educational purposes only**. Unauthorized use to scan systems without permission is illegal. Ensure you have explicit permission before using this tool.

---
