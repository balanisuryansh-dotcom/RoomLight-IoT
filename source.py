from flask import Flask, render_template_string, request, redirect
from gpiozero import OutputDevice

app = Flask(__name__)

# GPIO pin connected to relay
relay = OutputDevice(17, active_high=False)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Light Control</title>
</head>
<body>
    <h1>Light</h1>

    <form action="/on" method="post">
        <button type="submit">ON</button>
    </form>

    <br>

    <form action="/off" method="post">
        <button type="submit">OFF</button>
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/on", methods=["POST"])
def turn_on():
    relay.on()
    return redirect("/")

@app.route("/off", methods=["POST"])
def turn_off():
    relay.off()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
