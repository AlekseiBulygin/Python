import socket
import psutils

def get_ip_addresses():
    return [snic.address
            for snics in psutil.net_if_addrs().values()
            for snic in snics
            if snic.family == socket.AF_INET]
