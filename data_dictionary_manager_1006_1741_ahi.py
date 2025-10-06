# 代码生成时间: 2025-10-06 17:41:39
from gradio import Interface, components

"""
Data Dictionary Manager using Gradio framework.
This program allows users to manage a data dictionary through a simple GUI.
Users can add, update, and remove entries.
"""


# Define a data dictionary
data_dict = {}

# Function to add an entry to the data dictionary
def add_entry(key, value):
    """Add a new entry to the data dictionary."""
    if key in data_dict:
        return f"Error: '{key}' already exists."
    else:
        data_dict[key] = value
        return f"Entry '{key}' added successfully."

# Function to update an existing entry
def update_entry(key, value):
    """Update an existing entry in the data dictionary."""
    if key not in data_dict:
        return f"Error: '{key}' does not exist."
    else:
        data_dict[key] = value
        return f"Entry '{key}' updated successfully."

# Function to remove an entry from the data dictionary
def remove_entry(key):
    """Remove an entry from the data dictionary."""
    if key not in data_dict:
        return f"Error: '{key}' does not exist."
    else:
        del data_dict[key]
        return f"Entry '{key}' removed successfully."

# Function to display the current data dictionary
def display_dict():
    """Return the current state of the data dictionary."""
    return data_dict

# Create a Gradio interface
iface = Interface(
    fn=display_dict, 
    inputs=[], 
    outputs='text', 
    live=True,
    description="Data Dictionary Manager",
    title="Data Dictionary Management"
)

# Define the layout of the interface
with iface:
    # Input fields for key and value
    key_input = components.Textbox(label="Key")
    value_input = components.Textbox(label="Value")
    
    # Buttons for add, update, and remove operations
    add_button = components.Button(label="Add")
    update_button = components.Button(label="Update")
    remove_button = components.Button(label="Remove")
    
    # Function to handle the add operation
    def add(key, value):
        """Add a new entry to the data dictionary."""
        return add_entry(key, value)
    
    # Function to handle the update operation
    def update(key, value):
        """Update an existing entry in the data dictionary."""
        return update_entry(key, value)
    
    # Function to handle the remove operation
    def remove(key):
        """Remove an entry from the data dictionary."""
        return remove_entry(key)
    
    # Connect the input fields and buttons to their respective functions
    add_button.click(add, inputs=[key_input, value_input], outputs="text")
    update_button.click(update, inputs=[key_input, value_input], outputs="text")
    remove_button.click(remove, inputs=[key_input], outputs="text")

# Run the Gradio interface
iface.launch()