from azure.storage.queue import QueueClient
import os
import time

conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
queue = QueueClient.from_connection_string(conn_str, "demo-queue")

while True:
    messages = queue.receive_messages(messages_per_page=1, visibility_timeout=10)

    for msg in messages:
        print(f"Processing: {msg.content}, DequeueCount: {msg.dequeue_count}")

        # Simulate failure for specific messages
        if "fail" in msg.content:
            print("Simulating failure...")
            time.sleep(15)  # exceed visibility timeout
            continue

        # Simulate processing
        time.sleep(3)

        # Delete after success
        queue.delete_message(msg.id, msg.pop_receipt)
        print("Deleted message")

    time.sleep(2)
