# 代码生成时间: 2025-10-20 19:18:08
import gradio as gr

# 游戏资源管理类
class GameResourceManager:
    def __init__(self):
        # 初始化资源字典
        self.resources = {}

    # 添加资源
    def add_resource(self, name, value):
        """
        添加资源到资源管理器

        参数：
        name (str): 资源名称
        value (str): 资源值
        """
        if name in self.resources:
            raise ValueError("资源已存在")
        self.resources[name] = value
        return f"资源 {name} 已添加"

    # 获取资源
    def get_resource(self, name):
        """
        根据名称获取资源

        参数：
        name (str): 资源名称

        返回：
        value (str): 资源值
        """
        if name not in self.resources:
            raise ValueError("资源不存在")
        return self.resources[name]

    # 更新资源
    def update_resource(self, name, value):
        """
        更新资源

        参数：
        name (str): 资源名称
        value (str): 新的资源值
        """
        if name not in self.resources:
            raise ValueError("资源不存在")
        self.resources[name] = value
        return f"资源 {name} 已更新"

    # 删除资源
    def delete_resource(self, name):
        """
        删除资源

        参数：
        name (str): 资源名称
        """
        if name not in self.resources:
            raise ValueError("资源不存在")
        del self.resources[name]
        return f"资源 {name} 已删除"

# 创建游戏资源管理器实例
manager = GameResourceManager()

# Gradio界面配置
def add_resource(name, value):
    result = manager.add_resource(name, value)
    return {"result": result}

def get_resource(name):
    result = manager.get_resource(name)
    return {"result": result}

def update_resource(name, value):
    result = manager.update_resource(name, value)
    return {"result": result}

def delete_resource(name):
    result = manager.delete_resource(name)
    return {"result": result}

# 创建Gradio界面
iface = gr.Interface(
    fn=add_resource, 
    inputs=["text", "text"], 
    outputs="json",
    title="Add Resource",
    description="Add a new game resource"
)

iface.launch()