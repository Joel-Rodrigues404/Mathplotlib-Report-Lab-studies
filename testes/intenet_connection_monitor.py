import os
import time
import csv
import datetime
import matplotlib.pyplot as plt

LOG_FILE = "connection_log.csv"
PING_TARGET = "8.8.8.8"
INTERVAL = 5

def ping(host):
    response = os.system(f"ping -n 1 {host} > nul" if os.name == "nt" else f"ping -c 1 {host} > /dev/null 2>&1")
    return response == 0

def log_connection():
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["timestamp", "status"])
        while True:
            status = "OK" if ping(PING_TARGET) else "FALHA"
            writer.writerow([datetime.datetime.now(), status])
            file.flush()
            print(f"{datetime.datetime.now()} - {status}")
            time.sleep(INTERVAL)

def plot_graph():
    times, statuses = [], []
    with open(LOG_FILE) as file:
        reader = csv.DictReader(file)
        for row in reader:
            times.append(datetime.datetime.fromisoformat(row["timestamp"]))
            statuses.append(1 if row["status"] == "OK" else 0)
    plt.figure(figsize=(12, 4))
    plt.plot(times, statuses, drawstyle="steps-post")
    plt.ylim(-0.1, 1.1)
    plt.yticks([0, 1], ["FALHA", "OK"])
    plt.title("Estabilidade da Conexão")
    plt.xlabel("Tempo")
    plt.ylabel("Status")
    plt.grid(True)
    plt.show()

# log_connection()
plot_graph()
