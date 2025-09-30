# 代码生成时间: 2025-09-30 21:40:36
import gradio as gr
def responsive_design_demo(input_width, input_height):
    """
    Function to demonstrate responsive design using Gradio.
    This function takes input width and height and returns a message indicating
    whether the design is responsive based on the provided dimensions.
    """
    try:
        # Check if the input dimensions are valid and positive
        if input_width <= 0 or input_height <= 0:
            return "Invalid dimensions. Both width and height should be positive numbers."
        
        # Assume a design is responsive if the width is less than or equal to 768px (common breakpoint for responsiveness)
        responsive = input_width <= 768
        return "Responsive design: {}".format("Yes" if responsive else "No")
    except Exception as e:
        # Return a generic error message if an exception occurs
        return "An error occurred: " + str(e)

# Define the Gradio interface
iface = gr.Interface(
    fn=responsive_design_demo,
    inputs=[
        gr.Slider(minimum=1, maximum=2000, step=1, default=800, label="Width (px)"),
        gr.Slider(minimum=1, maximum=2000, step=1, default=600, label="Height (px)")
    ],
    outputs="text",
    title="Responsive Design Demo",
    description="A simple demo to check if a design is responsive based on given dimensions."
)

# Launch the Gradio interface
iface.launch(share=True)