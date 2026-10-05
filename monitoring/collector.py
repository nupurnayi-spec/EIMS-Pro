import platform, psutil
from datetime import datetime

def get_system_metrics():
    mem=psutil.virtual_memory(); disk=psutil.disk_usage('/'); net=psutil.net_io_counters()
    return {'hostname':platform.node(),'os':platform.platform(),'cpu':round(psutil.cpu_percent(interval=.5),1),'memory':round(mem.percent,1),'memory_used_gb':round(mem.used/1024**3,2),'memory_total_gb':round(mem.total/1024**3,2),'disk':round(disk.percent,1),'disk_used_gb':round(disk.used/1024**3,2),'disk_total_gb':round(disk.total/1024**3,2),'network_sent_mb':round(net.bytes_sent/1024**2,2),'network_recv_mb':round(net.bytes_recv/1024**2,2),'processes':len(psutil.pids()),'boot_time':datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
