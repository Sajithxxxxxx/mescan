# Mescan: Python Network IP Scanner

Mescan is a simple and lightweight Python tool for scanning a local network to detect active devices using ARP requests. It's built with **Scapy** and doesn't require `arp-scan` or any other external scanning tools.

## Features
- No dependencies on `arp-scan`
- Scans for devices on your local network
- Displays both IP and MAC addresses of connected devices

---

## **Installation Instructions**

1. **Clone the Repository**:
   First, clone this repository to your local machine using Git.

   ```bash
   git clone https://github.com/Sajithxxxxxx/mescan.git

    Install Dependencies: Mescan requires Python 3 and a couple of Python libraries to run. You can install the dependencies using pip.

pip install -r requirements.txt

Running the Tool: You need root (administrator) privileges to scan the network, so run the tool using sudo or as an administrator.

    sudo python3 MESCAN.py

Usage

    Once the tool starts, it will scan the entire local network (192.168.1.0/24 by default).

    It will display a list of devices found, showing both IP MAC addresses and services.

    The tool will run multiple scans automatically to ensure accuracy.

Customizing the Scan

    If you want to scan a different network range, you can modify the network variable in the script, or you can add a command-line argument for dynamic input.

Example:

sudo python3 MESCAN.py --network 192.168.0.0/24

Dependencies

    Scapy

    netifaces

License

This project is licensed under the MIT License - see the LICENSE file for details.


---

This will give users a clear guide on how to **clone**, **install**, and **run** your tool.
