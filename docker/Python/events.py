import docker 
import datetime
import requests

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
webhook_url = "https://discordapp.com/api/webhooks/1385645129016283136/IsB0NxL3c719lHIpkjo_c77WM26O6_uczmEuiYhjh9aa7bsCj2Y1lvq1GEksMCycdtsm"

for event in client.events(decode=True, filters={"event": "die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]
    date_time = datetime.datetime.fromtimestamp(epoch_time)

    payload = {"content": ("O container %s (%s) foi finalizado às %s" % (container_name, container_id, date_time))}

    print (payload)
    requests.post(webhook_url, data=payload)