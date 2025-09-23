# 代码生成时间: 2025-09-24 06:20:11
import json
from gradio import Interface, TextBox, Label

"""
API Response Formatter using Gradio framework.
This tool allows users to input a JSON API response and formats it in a readable way.
"""

def format_response(response: str) -> str:
    """
    Formats a JSON API response into a pretty printed string.
    
    Args:
    response (str): A JSON formatted string.
    
    Returns:
    str: A pretty printed JSON string.
    
    Raises:
    ValueError: If the input string is not a valid JSON.
    """
    try:
        # Parse the JSON string to a Python dictionary
        response_dict = json.loads(response)
        # Convert the dictionary back to a string, pretty printed
        formatted_response = json.dumps(response_dict, indent=4)
        return formatted_response
    except json.JSONDecodeError as error:
        # Raise a ValueError if the input string is not a valid JSON
        raise ValueError("Invalid JSON provided.") from error

# Define the Gradio interface
iface = Interface(
    fn=format_response,
    inputs=TextBox(placeholder="Enter your JSON response here..."),
    outputs=Label(),
    title="API Response Formatter",
    description="Format your API responses with this tool."
)

if __name__ == '__main__':
    # Launch the Gradio interface
    iface.launch()