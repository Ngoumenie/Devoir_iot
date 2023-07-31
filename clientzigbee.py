import zigpy
from zigpy.application import ControllerApplication
from zigpy.endpoint import Endpoint

# Initialize the Zigbee network
network = ControllerApplication(auto_form=True)

# Wait for the network to be ready
network.startup()

print("Zigbee client started")

# Create an endpoint
endpoint = Endpoint(network, 2)

# Identify the target node (replace the nwk_address with the desired Zigbee node address)
nwk_address = 0x1234

# Get the target node
node = network.get_node(nwk_address)

# Send a message to the target node
message = "Hello, Zigbee node!"
endpoint.command(6, 0, 1, message)

# Stop the Zigbee network
network.shutdown()
