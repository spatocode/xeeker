import pandas as pd
import psutil

def _parse_byte(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def system_data_usage(period):
    nic = psutil.net_io_counters(pernic=True)
    data = []
    for iface, iface_io in nic.items():
        data.append({
            "Interface": iface,
            "Total": _parse_byte(nic[iface].bytes_recv + nic[iface].bytes_sent),
            "Download": _parse_byte(nic[iface].bytes_recv),
            "Upload": _parse_byte(nic[iface].bytes_sent)
        })
        df = pd.DataFrame(data)
    return df.to_string()
