from flask import Flask, request, render_template, redirect
from azure.storage.queue import QueueClient
import os

app = Flask(__name__)

def get_queue():
    conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if not conn_str:
        raise Exception("Missing AZURE_STORAGE_CONNECTION_STRING")
    return QueueClient.from_connection_string(conn_str, "demo-queue")

@app.route("/")
def index():
    queue = get_queue()
    props = queue.get_queue_properties()
    count = props.approximate_message_count
    messages = list(queue.peek_messages(10))
    return render_template("index.html", count=count, messages=messages)

@app.route("/add", methods=["POST"])
def add():
    queue = get_queue()
    msg = request.form.get("message")
    queue.send_message(msg)
    return redirect("/")

@app.route("/bulk", methods=["POST"])
def bulk():
    queue = get_queue()
    n = int(request.form.get("count"))
    for i in range(n):
        queue.send_message(f"bulk-{i}")
    return redirect("/")

if __name__ == "__main__":
    app.run()
