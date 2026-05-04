<!DOCTYPE html>
<html>
<body>
<h2>Azure Queue Lab</h2>

<p>Queue Count: {{ count }}</p>

<form action="/add" method="post">
  <input name="message" placeholder="Enter message">
  <button type="submit">Add</button>
</form>

<h3>Messages (peek)</h3>
<ul>
{% for m in messages %}
  <li>{{ m.content }}</li>
{% endfor %}
</ul>

</body>
</html>
