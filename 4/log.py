
import re

with open("auth.log") as f:
    logs = f.readlines()

ip_count = {}

for line in logs:
    if "Failed password" in line:
        ip = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        if ip:
            ip_count[ip[0]] = ip_count.get(ip[0], 0) + 1

print("Failed Login Attempts:")

for ip, count in ip_count.items():
    print(ip, ":", count)

    if count >= 3:
        print("Suspicious IP:", ip)
