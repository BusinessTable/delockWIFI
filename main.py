from flask import Flask, request, jsonify, send_from_directory
import os
import requests

app = Flask(__name__)

# Store devices in memory (can be replaced with a database)
devices = []

@app.route('/')
def serve_index():
    return send_from_directory(os.path.dirname(__file__), 'index.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(os.path.dirname(__file__), filename)

@app.route('/api/relay', methods=['POST'])
def control_relay():
    data = request.json
    action = data.get('action')
    device_name = data.get('device')

    # Find the device by name
    device = next((d for d in devices if d['name'] == device_name), None)
    if not device:
        return jsonify({"message": "Device not found"}), 404

    if action == 'on':
        url = f"http://{device['ip']}/cm?cmnd=Power%20On"
    elif action == 'off':
        url = f"http://{device['ip']}/cm?cmnd=Power%20Off"
    elif action == 'toggle':
        url = f"http://{device['ip']}/cm?cmnd=Power%20Toggle"
    else:
        return jsonify({"message": "Invalid action"}), 400

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return jsonify({"message": f"Relay turned {action}"}), 200
        else:
            return jsonify({"message": "Failed to control the relay"}), 500
    except requests.RequestException as e:
        return jsonify({"message": str(e)}), 500

@app.route('/api/add_device', methods=['POST'])
def add_device():
    data = request.json
    name = data.get('name')
    ip = data.get('ip')

    if not name or not ip:
        return jsonify({"message": "Name and IP are required"}), 400

    devices.append({"name": name, "ip": ip})
    return jsonify({"message": "Device added successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
