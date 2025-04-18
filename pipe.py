from multiprocessing import Process, Pipe

def child_proc(conn):
    # Receive message from parent
    msg = conn.recv()
    print(f"Child received: {msg}")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    # Create a child process
    p = Process(target=child_proc, args=(child_conn,))
    p.start()

    # Parent sends a message
    message = "Hello from parent!"
    parent_conn.send(message)
    parent_conn.close()

    p.join()  # Wait for child to finish
