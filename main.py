from flask import (
    Flask,
    request,
    jsonify,
    send_from_directory,
    session,
    redirect,
    url_for,
)
from dotenv import load_dotenv
import os
import json
import requests

# Load environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# File to store device information
devices_file = "devices.json"

# Load devices from file
if os.path.exists(devices_file):
    with open(devices_file, "r") as file:
        devices = json.load(file)
else:
    devices = []


# Save devices to file
def save_devices():
    with open(devices_file, "w") as file:
        json.dump(devices, file)


@app.route("/")
def index():
    if "logged_in" not in session or not session["logged_in"]:
        return redirect(url_for("login"))
    return send_from_directory(os.path.dirname(__file__), "index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_password = request.form.get("password")
        if entered_password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            return (
                """<h3>Invalid password. Please try again.</h3><a href='/login'>Go back</a>""",
                401,
            )
    return send_from_directory(os.path.dirname(__file__), "login.html")


@app.route("/<path:filename>")
def serve_static_files(filename):
    if "logged_in" not in session or not session["logged_in"]:
        return redirect(url_for("login"))
    return send_from_directory(os.path.dirname(__file__), filename)


@app.route("/api/relay", methods=["POST"])
def control_relay():
    data = request.json
    action = data.get("action")
    device_name = data.get("device")

    # Find the device by name
    device = next((d for d in devices if d["name"] == device_name), None)
    if not device:
        return jsonify({"message": "Device not found"}), 404

    if action == "on":
        url = f"http://{device['ip']}/cm?cmnd=Power%20On"
        device["status"] = "On"
    elif action == "off":
        url = f"http://{device['ip']}/cm?cmnd=Power%20Off"
        device["status"] = "Off"
    else:
        return jsonify({"message": "Invalid action"}), 400

    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_devices()  # Update status in the file
            return jsonify({"message": f"Relay turned {action}"}), 200
        else:
            return jsonify({"message": "Failed to control the relay"}), 500
    except requests.RequestException as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/add_device", methods=["POST"])
def add_device():
    data = request.json
    name = data.get("name")
    ip = data.get("ip")

    if not name or not ip:
        return jsonify({"message": "Name and IP are required"}), 400

    # Check if the device already exists
    if any(d["name"] == name for d in devices):
        return jsonify({"message": "Device with this name already exists"}), 400

    new_device = {"name": name, "ip": ip, "status": "Unknown"}
    devices.append(new_device)
    save_devices()  # Save to file
    return jsonify({"message": "Device added successfully"}), 200


@app.route("/api/get_devices", methods=["GET"])
def get_devices():
    return jsonify(devices), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
