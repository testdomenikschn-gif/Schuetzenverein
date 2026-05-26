from pyngrok import ngrok
import time

print("Starte Tunnel...")

public_url = ngrok.connect(5000)

print("🌍 ONLINE:")
print(public_url)

while True:
    time.sleep(10)
