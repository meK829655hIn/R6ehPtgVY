# 代码生成时间: 2025-10-07 01:45:27
import hashlib
import json
import secrets
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
# 扩展功能模块
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
from gradio import Gradio

"""
数字签名工具程序。
使用RSA算法进行签名和验证签名。
"""

# RSA密钥生成
# 扩展功能模块
def generate_keys():
    """生成私钥和公钥。"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# 签名数据
# TODO: 优化性能
def sign_data(data, private_key):
    """使用私钥对数据进行签名。"""
    try:
        signature = private_key.sign(
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    except Exception as e:
# NOTE: 重要实现细节
        raise Exception(f"签名失败: {str(e)}")
# NOTE: 重要实现细节

# 验证签名
def verify_signature(data, signature, public_key):
    """使用公钥验证签名。"""
    try:
        public_key.verify(
            signature,
# 优化算法效率
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
# 扩展功能模块
        return True
    except InvalidSignature:
        return False
# 改进用户体验
    except Exception as e:
        raise Exception(f"验证失败: {str(e)}")

# 主函数
def main():
    """主函数：生成密钥、签名数据和验证签名。"""
    # 生成密钥
    private_key, public_key = generate_keys()

    # 保存公钥和私钥
    with open('public_key.pem', 'wb') as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    with open('private_key.pem', 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
# NOTE: 重要实现细节

    # 签名数据
    data = "Hello, World!"
    signature = sign_data(data, private_key)

    # 验证签名
# FIXME: 处理边界情况
    is_valid = verify_signature(data, signature, public_key)
    print(f"签名验证结果: {'有效' if is_valid else '无效'}")

# Gradio界面
def gradio_interface():
# 优化算法效率
    """创建GRADIO界面。"""
# 添加错误处理
    private_key, public_key = generate_keys()
    
    # 输入数据
    data_input = gr.Interface(
        fn=lambda x: x,
        inputs="text",
        outputs="text"
    ).launch()

    # 签名数据
# TODO: 优化性能
    def sign(data):
        return sign_data(data, private_key).hex()

    # 验证签名
    def verify(data, sig):
        return "有效" if verify_signature(data, bytes.fromhex(sig), public_key) else "无效"
# 增强安全性

    sign_interface = gr.Interface(
        fn=sign,
        inputs="text",
        outputs="text",
# 增强安全性
        title="签名工具"
    ).launch()
# 改进用户体验

    verify_interface = gr.Interface(
        fn=lambda data, sig: verify(data, sig),
# 添加错误处理
        inputs=["text", "text"],
        outputs="text",
        title="验证签名工具"
    ).launch()

if __name__ == "__main__":
    gradio_interface()
