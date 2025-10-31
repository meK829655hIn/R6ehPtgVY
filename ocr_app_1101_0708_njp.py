# 代码生成时间: 2025-11-01 07:08:47
import gr
import cv2 as cv
from PIL import Image
import pytesseract

# 初始化Gradio接口
iface = gr.Interface(
    fn=ocr_function,
    inputs=gr.inputs.Image(type="file"),
    outputs="text",
    title="OCR Text Recognition App",
    description="Upload an image to recognize text using OCR."
)

# OCR函数定义
def ocr_function(image):
    # 错误处理
    try:
        # 将上传的图片转换为PIL Image对象
        pil_image = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        # 使用pytesseract进行OCR识别
        text = pytesseract.image_to_string(pil_image)
        # 返回识别的文本
        return text
    except Exception as e:
        # 捕获异常并返回错误信息
        return f"An error occurred: {e}"

# 启动Gradio应用
iface.launch()