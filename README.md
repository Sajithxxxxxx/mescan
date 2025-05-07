
![mescan](https://github.com/user-attachments/assets/7f191166-3f5d-4d72-8aba-e1df3464f663)







# MeScan Python Network IP and MAC Scanner

MeScan scans the local network using ARP requests and identifies active devices by displaying their IP addresses, MAC addresses, and hostnames — all in a clean, user-friendly terminal interface.

Unlike many existing network scanners, MeScan prioritizes accuracy, simplicity, and a modern terminal experience. It automatically detects the active interface and subnet, making it ideal for fast local discovery without manual setup.




 ## Features

   > Scans your local network using ARP

   > Displays IP address, MAC address, and hostname of connected devices

   > Uses Rich for a colorful and readable terminal output

   > Automatically detects your default network interface and subnet

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jaguar-00700/mescan.git
cd mescan
```
### 2. Install Dependencies

Make sure you have Python 3 installed, then run:
```bash
sudo apt install pyhton3
```
||

```bash
pip install -r requirements.txt
```
   Dependencies:

   scapy

   rich

   netifaces

You can also install them manually:
```bash
pip install scapy rich netifaces
```
### Run
Run the tool with root privileges 
```bash
sudo python3 me_scan.py
```
## Usage

By default, MeScan:

   Detects your active network interface

   Calculates your subnet range (e.g., 192.168.1.0/24)

   Scans for devices on that range


Customizing the Scan

To scan a custom network range, edit the line that generates ip_range:

ip_range = "192.168.0.0/24"

Or modify the script to accept command-line arguments for more flexibility.

## License

This project is licensed under the MIT License.
