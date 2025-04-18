import random

class LamportClock:
    def __init__(self, pid):
        self.time = 0
        self.pid = pid

    def tick(self):
        self.time += 1

    def send_event(self):
        self.tick()
        return self.time

    def receive_event(self, received_time):
        self.time = max(self.time, received_time) + 1

    def get_time(self):
        return self.time

num_processes = int(input("Enter the number of processes: "))
num_events = int(input("Enter the number of events: "))

processes = [LamportClock(i) for i in range(num_processes)]
events = []

print("\nInitial Clocks:")
for p in processes:
    print(f"Process {p.pid}: {p.get_time()}")

for _ in range(num_events):
    p = random.choice(processes)
    action = random.choice(["send", "receive"])

    if action == "send":
        send_time = p.send_event()
        print(f"\nProcess {p.pid} sends message at time {send_time}")
        receiver = random.choice([pr for pr in processes if pr != p])
        receiver.receive_event(send_time)
        print(f"Process {receiver.pid} receives message and updates clock to {receiver.get_time()}")
        events.append((p.pid, send_time, receiver.pid, receiver.get_time()))

print("\nFinal Clocks:")
for p in processes:
    print(f"Process {p.pid}: {p.get_time()}")
