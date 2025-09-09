#!/usr/bin/env python3
import psutil
import datetime

print(f"[{datetime.datetime.now()}] CPU: {psutil.cpu_percent()}%")



