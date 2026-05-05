from flask import Flask, request, render_template, redirect
from azure.storage.queue import QueueClient
import os

app = Flask(__name__)

def get_conn_str():
    # support both names to avoid mismatch issues
    return os.getenv("AZURE_STORAGE_CONNECTION_STRING") or os.getenv("AZURE_STORAGE_CONNECTION_STRING")

def get_queue():
    conn_str = get_conn_str()
    if not conn_str:
        raise Exception("Missing connection string. Check App Service settings.")
    return QueueClient.from_connection_string(conn_str, "demo-queue")

@app.route("/")
def index():
    try:
        queue = get_queue()
        props = queue.get_queue_properties()
        count = props.approximate_message_count
        messages = list(queue.peek_messages(10))
    except Exception as e:
        return f"Error: {str(e)}"
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
