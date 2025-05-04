from scapy.all import ARP, Ether, srp, conf
import socket
from rich.console import Console
from rich.table import Table
import netifaces

console = Console()

def get_default_interface():
    # Auto-detect default interface (like wlan0 or eth0)
    gws = netifaces.gateways()
    default_iface = gws['default'][netifaces.AF_INET][1]
    return default_iface

def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def arp_scan(ip_range, interface):
    conf.verb = 0  # Turn off Scapy output
    conf.iface = interface
    console.print(f"[bold yellow]Scanning {ip_range} on interface {interface}...[/bold yellow]\n")
   
    # Create ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send and receive packets
    result = srp(packet, timeout=4, inter=0.1)[0]

    # Deduplicate and store results
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

    table = Table(title="Results", show_lines=True)
    table.add_column("IP Address", style="cyan")
    table.add_column("MAC Address", style="magenta")
    table.add_column("Hostname", style="green")

    for dev in devices:
        table.add_row(dev["ip"], dev["mac"], dev["hostname"])

    console.print(table)

if __name__ == "__main__":
    ip_range = "192.168.29.0/24"
    interface = get_default_interface()  # or manually set: "wlan0", "eth0", etc.
    devices = arp_scan(ip_range, interface)
    display_results(devices)
