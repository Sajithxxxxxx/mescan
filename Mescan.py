from scapy.all import ARP, Ether, srp
import ipaddress
import netifaces
import time

def get_network_and_iface():
    gateways = netifaces.gateways()
    iface = gateways['default'][netifaces.AF_INET][1]
    ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    ip = ip_info['addr']
    netmask = ip_info['netmask']
    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
    return str(network), iface

def scan_once(network, iface):
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=network)
    packet = ether / arp
    answered, _ = srp(packet, timeout=2, iface=iface, verbose=0)
    result = {}
    for sent, received in answered:
        result[received.psrc] = received.hwsrc
    return result

def scan_multiple_times(network, iface, attempts=3, delay=1):
    all_results = {}
    for i in range(attempts):
        print(f"[*] Scan attempt {i+1}/{attempts}...")
        result = scan_once(network, iface)
        all_results.update(result)
        time.sleep(delay)
    return all_results

if __name__ == "__main__":
    try:
        network, iface = get_network_and_iface()
        print(f"[*] Scanning {network} on {iface}...\n")
        devices = scan_multiple_times(network, iface)

        print("=== Devices Found ===")
        print("IP Address\t\tMAC Address")
        print("----------------------------------------")
        for ip, mac in sorted(devices.items()):
            print(f"{ip}\t\t{mac}")

    except Exception as e:
        print(f"[!] Error: {e}")
