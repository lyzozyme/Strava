import requests
import json
import time
import subprocess

ngrok_url = 'http://localhost:4040/api/tunnels'

ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'])

# Attendre jusqu'à ce que ngrok ait établi une connexion et créé un tunnel
while True:
    try:
        response = requests.get(ngrok_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            if len(data['tunnels']) > 0:
                public_url = data['tunnels'][0]['public_url']
                break
    except:
        print("Pas d'url trouvée...")
    time.sleep(1)

print('URL publique :', public_url)
