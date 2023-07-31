import zigpy
from zigpy.device import Device
from zigpy.endpoint import Endpoint

# Initialize the Zigbee network
device = Device()
network = zigpy.application.ControllerApplication(device, auto_form=True)

# Wait for the network to be ready
network.startup()
print("Zigbee Server started")

# Create an endpoint
endpoint = Endpoint(device, 1)

# Define a callback function for incoming messages
def message_callback(msg):
    print(f"Message received: {msg.data}")

# Associate the callback function with the endpoint
endpoint.in_clusters[6].subscribe(message_callback)

# Main loop of the server
while True:
    # Check for incoming messages
    network.process_data_frames()

# Stop the Zigbee network
network.shutdown()
