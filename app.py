from flask import Flask, request, render_template, redirect
from azure.storage.queue import QueueClient
import os

app = Flask(__name__)

conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
queue = QueueClient.from_connection_string(conn_str, "demo-queue")

@app.route("/")
def index():
    props = queue.get_queue_properties()
    count = props.approximate_message_count
    messages = queue.peek_messages(10)
    return render_template("index.html", count=count, messages=messages)

@app.route("/add", methods=["POST"])
def add():
    msg = request.form.get("message")
    queue.send_message(msg)
    return redirect("/")

if __name__ == "__main__":
    app.run()
