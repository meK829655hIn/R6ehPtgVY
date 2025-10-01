# 代码生成时间: 2025-10-02 01:37:27
import gradio as gr
import requests

"""
HTTP Request Handler using Gradio framework.
This script demonstrates how to create a simple HTTP request handler using Gradio.
It allows users to send HTTP requests and displays the response.
"""

# Function to handle HTTP requests
def handle_request(url, method, headers, payload):
    """
    Handles an HTTP request to the specified URL with the given method, headers, and payload.

    Args:
    url (str): The URL to send the request to.
    method (str): The HTTP method to use (e.g., GET, POST, PUT, DELETE).
    headers (dict): A dictionary of headers to include in the request.
    payload (str): The payload to send with the request.

    Returns:
    dict: A dictionary containing the status code, headers, and response body.

    Raises:
    requests.RequestException: If an error occurs while sending the request.
    """
    try:
        response = requests.request(method, url, headers=headers, data=payload)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "response": response.text
        }
    except requests.RequestException as e:
        return {"error": str(e)}

# Create a Gradio interface
iface = gr.Interface(
    fn=handle_request,
    inputs=[
        gr.Textbox(label="URL"),
        gr.Radio(["GET", "POST", "PUT", "DELETE"], label="Method"),
        gr.Textbox(label="Headers (JSON)", placeholder='{"Content-Type": "application/json"}'),
        gr.Textbox(label="Payload", placeholder='{"key": "value"}')
    ],
    outputs=[
        gr.Textbox(label="Response")
    ]
)

# Run the interface
iface.launch(prevent_thread_lock=True)