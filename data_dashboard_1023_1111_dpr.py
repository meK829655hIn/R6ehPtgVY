# 代码生成时间: 2025-10-23 11:11:28
import gr
import pandas as pd
import numpy as np

"""
Data Dashboard using Gradio and Python
This script creates a simple data dashboard that allows users to input data,
process it through various statistical measures, and visualize the results.
"""

# Define a function to calculate basic statistical measures
def calculate_statistics(data):
    """
    Calculate mean, median, and standard deviation of the input data.

    Args:
    data (list): A list of numerical values.

    Returns:
    dict: A dictionary containing mean, median, and standard deviation.
    """
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    return {"mean": mean, "median": median, "std_dev": std_dev}

# Define a function to plot histogram of the data
def plot_histogram(data):
    """
    Plot a histogram of the input data using Gradio.

    Args:
    data (list): A list of numerical values.
    """
    fig, ax = plt.subplots()
    ax.hist(data, bins=10, edgecolor='black')
    ax.set_title('Histogram of Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    return gr.update(value=fig)

# Create a Gradio interface
iface = gr.Interface(
    fn=calculate_statistics,  # Function to execute
    inputs=[gr.inputs.Number(label='Enter data values separated by commas', default='1,2,3,4,5')],  # Input type and label
    outputs=[gr.outputs.Textbox(label='Statistics')],  # Output type and label
    examples=["1,2,3,4,5"],  # Example input
    description="Enter comma-separated numerical data to calculate statistics and visualize it."
)

# Launch the dashboard
iface.launch(share=True)