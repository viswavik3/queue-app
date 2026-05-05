from flask import Flask, request, render_template, redirect
from azure.storage.queue import QueueClient
import os

app = Flask(__name__)

conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
queue_name = "demo-queue"
queue = QueueClient.from_connection_string(conn_str, queue_name)

@app.route("/")
def index():
    props = queue.get_queue_properties()
    count = props.approximate_message_count
    messages = list(queue.peek_messages(10))
    return render_template("index.html", count=count, messages=messages)

@app.route("/add", methods=["POST"])
def add():
    msg = request.form.get("message")
    queue.send_message(msg)
    return redirect("/")

@app.route("/bulk", methods=["POST"])
def bulk():
    n = int(request.form.get("count"))
    for i in range(n):
        queue.send_message(f"bulk-message-{i}")
    return redirect("/")

if __name__ == "__main__":
    app.run()
