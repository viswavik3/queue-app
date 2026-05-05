from azure.storage.queue import QueueClient
import os, time

conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
if not conn_str:
    raise Exception("Missing connection string")

queue = QueueClient.from_connection_string(conn_str, "demo-queue")

while True:
    messages = queue.receive_messages(messages_per_page=1, visibility_timeout=10)

    for msg in messages:
        print(f"Processing: {msg.content}, DequeueCount: {msg.dequeue_count}")

        if "fail" in msg.content:
            time.sleep(15)
            continue

        if "slow" in msg.content:
            time.sleep(12)

        time.sleep(2)
        queue.delete_message(msg.id, msg.pop_receipt)
        print("Deleted")

    time.sleep(1)
