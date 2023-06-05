import subprocess
import time

# Lancement de ngrok
ngrok_process = subprocess.Popen(['ngrok', 'http', '8000'])

time.sleep(5)

import subscribe
