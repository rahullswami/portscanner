import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format('PORT SCANNER')
print(ascii_banner)

target = input('Target IP: ')

# Banner
print('_' * 50)
print(f'Scanning Target: {target}')
print(f'Scanning Started at: {str(datetime.now())}')
print('_' * 50)

try:
    # Scan ports 1 to 65535
    for port in range(1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(0.5)  # Set timeout to 0.5 seconds
            result = s.connect_ex((target, port))  # Check connection
            if result == 0:
                print(f'[*] Port {port} is open')  # Port is open

except KeyboardInterrupt:
    print('\nExiting :(')
    sys.exit()

except socket.gaierror:
    print('\nInvalid target address.')
    sys.exit()

except socket.error as err:
    print(f'\nHost not responding: {err}')
    sys.exit()
