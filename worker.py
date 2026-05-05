from azure.storage.queue import QueueClient
import os, time

def get_queue():
    conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    return QueueClient.from_connection_string(conn_str, "demo-queue")

while True:
    messages = queue.receive_messages(messages_per_page=1, visibility_timeout=10)

    for msg in messages:
        print(f"Processing: {msg.content}, DequeueCount: {msg.dequeue_count}")

        if "fail" in msg.content:
            print("Simulating failure")
            time.sleep(15)
            continue

        if "slow" in msg.content:
            print("Simulating slow processing")
            time.sleep(12)

        time.sleep(2)
        queue.delete_message(msg.id, msg.pop_receipt)
        print("Deleted")

    time.sleep(1)
