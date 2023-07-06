import psutil

def _parse_byte(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def process_data_usage(period):
    pass

def system_data_usage(period):
    nic = psutil.net_io_counters()
    return _parse_byte(nic.bytes_recv+nic.bytes_sent), _parse_byte(nic.bytes_recv), _parse_byte(nic.bytes_sent)

def interface_data_usage(period, interface):
    data = []
    nic = psutil.net_io_counters(pernic=True)
    if nic.get(interface):
        data.append({
            "Interface": interface,
            "Total": _parse_byte(nic[interface].bytes_recv + nic[interface].bytes_sent),
            "Download": _parse_byte(nic[interface].bytes_recv),
            "Upload": _parse_byte(nic[interface].bytes_sent)
        })
        return data

    for iface, iface_io in nic.items():
        data.append({
            "Interface": iface,
            "Total": _parse_byte(nic[iface].bytes_recv + nic[iface].bytes_sent),
            "Download": _parse_byte(nic[iface].bytes_recv),
            "Upload": _parse_byte(nic[iface].bytes_sent)
        })
    return data
