# MeScan Python Network IP and MAC Scanner

MeScan is a lightweight and stylish Python tool that scans your local network to identify active devices using ARP requests. Built with Scapy and Rich, it not only displays IP and MAC addresses but also attempts to resolve hostnames, all with a clean terminal UI.

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
OR

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
