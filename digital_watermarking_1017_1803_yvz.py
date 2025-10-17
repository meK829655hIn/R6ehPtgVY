# 代码生成时间: 2025-10-17 18:03:42
import numpy as np
from PIL import Image
import cv2
import gradio as gr

"""
数字水印技术
"""

# 定义一个类DigitalWatermark用于处理数字水印
class DigitalWatermark:
    def __init__(self):
        """初始化"""
        pass

    def embed_watermark(self, image_path, watermark_text):
        """
        将水印嵌入到图片中
        :param image_path: 图片路径
        :param watermark_text: 水印文本
        :return: 嵌入水印后的图片
        """
        try:
            # 读取图片
            image = Image.open(image_path)
            # 将图片转换为灰度图
            image_gray = image.convert('L')
            # 将图片转换为numpy数组
            image_array = np.array(image_gray)

            # 将水印文本转换为二进制
            watermark_binary = ''.join(format(ord(c), '08b') for c in watermark_text)
            # 计算水印长度
            watermark_length = len(watermark_binary)

            # 将水印嵌入到图片的最低有效位
            for i in range(watermark_length):
                image_array[i % image_array.shape[0], i % image_array.shape[1]] = \
                    (image_array[i % image_array.shape[0], i % image_array.shape[1]] & 0xFE) | int(watermark_binary[i])

            # 将numpy数组转换回图片
            watermarked_image = Image.fromarray(image_array)
            return watermarked_image
        except Exception as e:
            print(f"Error embedding watermark: {e}")
            return None

    def extract_watermark(self, image_path):
        """
        从图片中提取水印
        :param image_path: 图片路径
        :return: 提取的水印文本
        """
        try:
            # 读取图片
            image = Image.open(image_path)
            # 将图片转换为灰度图
            image_gray = image.convert('L')
            # 将图片转换为numpy数组
            image_array = np.array(image_gray)

            # 初始化水印字符串
            watermark_text = ""
            # 提取水印
            for i in range(image_array.size):
                watermark_text += str(image_array[i % image_array.shape[0], i % image_array.shape[1]] & 0x01)

            # 将二进制水印转换回文本
            watermark_bytes = bytes(int(watermark_text[i:i+8], 2) for i in range(0, len(watermark_text), 8))
            watermark_text = watermark_bytes.decode('utf-8')
            return watermark_text
        except Exception as e:
            print(f"Error extracting watermark: {e}")
            return None

# 创建一个DigitalWatermark实例
watermark = DigitalWatermark()

# 使用GRADIO创建界面
iface = gr.Interface(
    fn=lambda image: watermark.embed_watermark(image, 'Hello World'),
    inputs=gr.inputs.Image(type='file'),
    outputs=gr.outputs.Image(),
    title="Digital Watermarking",
    description="Embed and extract digital watermarks in images."
)

# 启动界面
iface.launch()