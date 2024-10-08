import nuke

# Function to create a Roto node and a Blur node with default settings and connect them
def create_roto_and_blur():
    # Create a Roto node
    roto_node = nuke.createNode('Roto')

    # Create a Blur node
    blur_node = nuke.createNode('Blur')

    # Set default blur value to 1
    blur_node['size'].setValue(1)

    # Position the Blur node below the Roto node
    blur_node.setXYpos(roto_node.xpos(), roto_node.ypos() + 100)

    # Connect the Roto node to the Blur node (Roto output to Blur input)
    blur_node.setInput(0, roto_node)