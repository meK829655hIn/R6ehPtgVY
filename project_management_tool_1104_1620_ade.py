# 代码生成时间: 2025-11-04 16:20:11
import gr
# 优化算法效率
from gr import *

"""
项目管理工具

这个工具使用GRADIO框架创建一个简单的项目管理界面。
用户可以添加项目、查看所有项目、更新项目状态和删除项目。
# 扩展功能模块
"""

# 项目列表
projects = []

# 添加项目函数
def add_project(name, description):
    """添加项目到列表中"""
    if not name or not description:
        raise ValueError("Name and description cannot be empty.")
# 添加错误处理
    projects.append({"name": name, "description": description, "status": "active"})
    return projects

# 获取所有项目函数
def get_projects():
    """返回所有项目"""
    return projects

# 更新项目状态函数
def update_project_status(project_name, new_status):
    """根据项目名称更新项目状态"""
    for project in projects:
        if project["name"] == project_name:
            project["status"] = new_status
            return projects
    raise ValueError("Project not found.")

# 删除项目函数
# NOTE: 重要实现细节
def delete_project(project_name):
    """根据项目名称删除项目"""
    global projects
    projects = [project for project in projects if project["name"] != project_name]
    return projects

# 创建GRADIO界面
iface = gr.Interface(
    
    fn=add_project,
    inputs=[gr.Textbox(label="Project Name"), gr.Textbox(label="Project Description")],
    outputs=[gr.Dataframe()],
    title="Add Project",
    description="Add a new project to the list."
)

iface2 = gr.Interface(
    fn=get_projects,
    inputs=[],
    outputs=[gr.Dataframe()],
# 改进用户体验
    title="View Projects",
    description="View all projects."
)

iface3 = gr.Interface(
    fn=update_project_status,
    inputs=[gr.Textbox(label="Project Name"), gr.Radio(["active", "inactive"]),],
    outputs=[gr.Dataframe()],
    title="Update Project Status",
    description="Update the status of a project."
)

iface4 = gr.Interface(
# TODO: 优化性能
    fn=delete_project,
    inputs=[gr.Textbox(label="Project Name")],
    outputs=[gr.Dataframe()],
    title="Delete Project",
    description="Delete a project."
)

# 运行所有界面
iface.launch(), iface2.launch(), iface3.launch(), iface4.launch()