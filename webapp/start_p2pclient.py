import os
import subprocess

import requests
current_dir = os.path.dirname(os.path.abspath(__file__))

log_path = os.path.join(current_dir, "test.log")

ip = requests.get('https://api.ipify.org').text

#cmd = f'./app/Cli start accept --token Y6guAsxkoh8M1sPbbQ9Ue45jmP5JtcjO6OtjYBnU2tI= >> {log_path} 2>&1 &'
cmd = f'cd /app && ls >> {log_path} 2>&1 &'
# run cmd and wait for it to finish
out, err = subprocess.Popen(
    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print(out.decode('utf-8'))
print(err.decode('utf-8'))
