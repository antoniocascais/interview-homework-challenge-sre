#!/usr/bin/env python3

import argparse
import time
import psutil


def fmt_size(b):
    g = b / (1024**3)
    return f"{g:.1f}G" if g >= 1 else f"{b // (1024**2)}M"


def disk():
    for p in psutil.disk_partitions():
        u = psutil.disk_usage(p.mountpoint)
        print(f"{p.device} ({p.mountpoint}): total={fmt_size(u.total)} used={fmt_size(u.used)} free={fmt_size(u.free)} {u.percent}%")


def cpu():
    print(f"Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count()} logical")
    print(f"Usage: {psutil.cpu_percent(interval=1)}%")
    freq = psutil.cpu_freq()
    if freq:
        print(f"Frequency: {freq.current:.0f}MHz")


def ram():
    m = psutil.virtual_memory()
    print(f"Total: {fmt_size(m.total)}")
    print(f"Used: {fmt_size(m.used)}")
    print(f"Free: {fmt_size(m.available)}")
    print(f"Used: {m.percent}%")


def ports():
    try:
        conns = psutil.net_connections(kind="inet")
    except psutil.AccessDenied:
        print("Error: insufficient permissions (try running with sudo)")
        return
    seen = set()
    for c in conns:
        if c.status == "LISTEN":
            addr = f"{c.laddr.ip}:{c.laddr.port}"
            if addr not in seen:
                seen.add(addr)
                print(addr)


def overview():
    for p in psutil.process_iter(["cpu_percent"]):
        pass
    # The sleep is needed to warm-up Process.cpu_percent
    time.sleep(1)
    procs = []
    for p in psutil.process_iter(attrs=["pid", "name", "cpu_percent"], ad_value=0):
        procs.append(p.info)
    procs.sort(key=lambda x: x["cpu_percent"] or 0, reverse=True)
    print(f"{'PID':<8} {'CPU%':<8} {'NAME'}")
    for p in procs[:10]:
        print(f"{p['pid']:<8} {p['cpu_percent']:<8} {p['name']}")


parser = argparse.ArgumentParser(prog="myscript.py", description="Myscript description")
parser.add_argument("-d", "--disk", action="store_true", help="check disk stats")
parser.add_argument("-c", "--cpu", action="store_true", help="check cpu stats")
parser.add_argument("-p", "--ports", action="store_true", help="check listen ports")
parser.add_argument("-r", "--ram", action="store_true", help="check ram stats")
parser.add_argument("-o", "--overview", action="store_true", help="top 10 process with most CPU usage.")

args = parser.parse_args()

ran = False
if args.disk:
    disk(); ran = True
if args.cpu:
    cpu(); ran = True
if args.ram:
    ram(); ran = True
if args.ports:
    ports(); ran = True
if args.overview:
    overview(); ran = True
if not ran:
    parser.print_help()
