import re
from email import message_from_string
header= """From: abc@gmail.com
To: xyz@gmail.com
Subject: Hello
Date: Sun, 15 Nov 2026 10:00:00
Message-ID: <123@gmail.com>
Received: from 192.168.1.10 by mail.server.com
"""

email=message_from_string(header)

print("From:", email['From'])

ip = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', header)
print("IP Addresses:", ip)