import pygatt

# Configuration of the server
adapter = pygatt.GATTToolBackend()

# Start the Bluetooth adapter
adapter.start()

# Search for nearby Bluetooth devices
devices = adapter.scan()

# Select the target device
target_device = None
for device in devices:
    if device["name"] == "Nicophil":
        target_device = device
        break

# Check if the target device is found
if target_device is None:
    print("Target device not found")
    adapter.stop()
    exit()

# Connect to the target device
device = adapter.connect(target_device["20:69:80:25:F9:18"])

# Read data from the device
data = device.char_read("00002a00-0000-1000-8000-00805f9b34fb")
received_data = data.decode()
print("Received data:", received_data)

# Close the connection with the device
device.disconnect()

# Stop the Bluetooth adapter
adapter.stop()
