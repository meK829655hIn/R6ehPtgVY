# 代码生成时间: 2025-10-24 23:38:07
import hashlib
from gradio import Interface

"""
文件完整性校验器
通过GRADIO框架提供的界面，用户可以上传文件，程序将计算文件的MD5哈希值来校验其完整性。
"""

def calculate_md5(file_path):
    """
    计算文件的MD5哈希值
    :param file_path: 文件路径
    :return: 文件的MD5哈希值
    """
    try:
        with open(file_path, 'rb') as file:
            hash_md5 = hashlib.md5()
            for chunk in iter(lambda: file.read(4096), b''):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()
    except FileNotFoundError:
        print("文件未找到")
        return None
    except Exception as e:
        print(f"计算文件MD5时发生错误：{e}")
        return None

def main():
    """
    主函数
    设置GRADIO界面，用户可以上传文件，并显示文件的MD5哈希值。
    """
    file_input = gr.Interface(
        fn=calculate_md5,
        inputs="file",
        outputs="text",
        title="文件完整性校验器",
        description="上传文件以计算其MD5哈希值"
    )
    file_input.launch()

if __name__ == '__main__':
    main()