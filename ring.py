import random

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.leader = False

    def send_election_message(self, election_message):
        """ Send election message with updated process IDs to next process """
        election_message.append(self.pid)  # Add own ID to the list
        return election_message

    def receive_election_message(self, election_message):
        """ Receive election message and send to the next process with updated message """
        election_message.append(self.pid)  # Add own ID to the list
        return election_message

def ring_election(num_processes):
    processes = [Process(i) for i in range(num_processes)]  # Create processes
    election_message = []  # This will store the array of process IDs

    # Randomly select a process to fail (exclude it from the election)
    failed_process_pid = random.randint(0, num_processes - 1)
    print(f"Process {failed_process_pid} has failed and will not participate in the election.")
    
    # Exclude the failed process from the election
    processes = [p for p in processes if p.pid != failed_process_pid]
    num_processes -= 1  # Update the number of processes after failure

    # Start election with a random process (other than the failed process)
    initiator = random.choice(processes)
    print(f"Process {initiator.pid} starts the election.")
    
    # The initiator sends its own process ID to the next process
    election_message = initiator.send_election_message(election_message)
    print(f"Process {initiator.pid} sends election message with ID {initiator.pid} to Process {processes[(initiator.pid + 1) % num_processes].pid}")

    # The message circulates around the ring
    for i in range(num_processes):
        current_process = processes[i]
        next_process = processes[(i + 1) % num_processes]
        election_message = current_process.receive_election_message(election_message)
        print(f"Process {current_process.pid} sends election message with IDs {election_message} to Process {next_process.pid}")
    
    # After the message comes back to the initiator, find the largest process ID
    leader_pid = max(election_message)
    print(f"Election complete. Process {leader_pid} is the new leader.")

# Run the ring election with 6 processes
num_processes = int(input("Enter the number of processes in the ring: "))
ring_election(num_processes)
