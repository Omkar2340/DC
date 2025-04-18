class Process:
    def __init__(self, pid):
        self.pid = pid
        self.waiting_for = []

def send_probe(processes, initiator, sender, receiver, visited):
    print(f"Probe: [{initiator}, {sender}, {receiver}]")
    if receiver == initiator:
        print(f"\n Deadlock detected involving Process {initiator}!\n")
        return True

    if receiver in visited:
        return False

    visited.add(receiver)
    for next_proc in processes[receiver].waiting_for:
        if send_probe(processes, initiator, receiver, next_proc, visited):
            return True
    return False

def chandy_misra_haas_from_initiator(processes, initiator):
    process = processes[initiator]
    if not process.waiting_for:
        print(f"\nProcess {initiator} is not waiting for any other process. No need to initiate probe.")
        return

    print(f"\nProcess {initiator} is waiting for {process.waiting_for}. Initiating probe.")
    visited = set()
    deadlock_found = False
    for waiting_on in process.waiting_for:
        if send_probe(processes, initiator, initiator, waiting_on, visited):
            deadlock_found = True
            break

    if not deadlock_found:
        print("\n No deadlock detected.")

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = {i: Process(i) for i in range(n)}

    print("Define wait relationships (e.g., if P1 waits for P2, enter: 1 2)")
    print("Enter -1 -1 to finish.")
    while True:
        pair = input("Waiting pair: ").strip()
        if pair == "-1 -1":
            break
        try:
            a, b = map(int, pair.split())
            if a in processes and b in processes:
                processes[a].waiting_for.append(b)
        except:
            print("Invalid input. Try again.")

    while True:
        try:
            initiator = int(input("Enter the initiator process ID: "))
            if initiator in processes:
                break
            else:
                print("Invalid process ID. Try again.")
        except:
            print("Invalid input. Try again.")

    chandy_misra_haas_from_initiator(processes, initiator)
