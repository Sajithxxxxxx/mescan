from scapy.all import ARP, Ether, srp, conf
import socket
from rich.console import Console
from rich.table import Table
import netifaces
import ipaddress

console = Console()

def get_default_interface():
    gws = netifaces.gateways()
    default_iface = gws['default'][netifaces.AF_INET][1]
    return default_iface

def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def arp_scan(ip_range, interface):
    conf.verb = 0  # Silence scapy
    conf.iface = interface
    console.print(f"[bold yellow]Scanning {ip_range} on interface {interface}...[/bold yellow]\n")
    
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=4, inter=0.1)[0]

    devices = []
    seen_ips = set()
    for sent, received in result:
        if received.psrc not in seen_ips:
            seen_ips.add(received.psrc)
            devices.append({
                "ip": received.psrc,
                "mac": received.hwsrc,
                "hostname": resolve_hostname(received.psrc)
            })
    return devices

def display_results(devices):
    if not devices:
        console.print("[red]No devices found.[/red]")
        return

    table = Table(title="Scan Results", show_lines=True)
    table.add_column("IP Address", style="cyan")
    table.add_column("MAC Address", style="magenta")
    table.add_column("Hostname", style="green")

    for dev in devices:
        table.add_row(dev["ip"], dev["mac"], dev["hostname"])

    console.print(table)

if __name__ == "__main__":
    interface = get_default_interface()

    # Get IP and subnet mask
    iface_data = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
    ip = iface_data['addr']
    netmask = iface_data['netmask']

    # Convert to CIDR range (e.g., 192.168.1.0/24)
    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
    ip_range = str(network)

    devices = arp_scan(ip_range, interface)
    display_results(devices)
