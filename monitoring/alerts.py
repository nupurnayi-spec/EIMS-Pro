from config import *

def evaluate_alerts(m):
    alerts=[]
    for name,key,w,c in [('CPU','cpu',CPU_WARNING,CPU_CRITICAL),('Memory','memory',MEMORY_WARNING,MEMORY_CRITICAL),('Disk','disk',DISK_WARNING,DISK_CRITICAL)]:
        if m[key]>=c: alerts.append({'level':'critical','title':f'{name} Critical','message':f'{name} usage is {m[key]}%.'})
        elif m[key]>=w: alerts.append({'level':'warning','title':f'{name} Warning','message':f'{name} usage is {m[key]}%.'})
    return alerts or [{'level':'healthy','title':'All Systems Healthy','message':'No threshold violations detected.'}]
