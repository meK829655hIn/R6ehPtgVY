# 代码生成时间: 2025-10-19 08:53:25
import gradio as gr
def add_points(member_id, points):
    """
    向会员增加积分
    :param member_id: 会员ID
    :param points: 增加的积分
    :return: 更新后的积分
    """
    try:
        if member_id not in members:
            raise ValueError("会员不存在")
        members[member_id] += points
        return members[member_id]
    except Exception as e:
        return str(e)

def deduct_points(member_id, points):
    """
    扣除会员积分
    :param member_id: 会员ID
    :param points: 扣除的积分
    :return: 更新后的积分
    """
    try:
        if member_id not in members:
            raise ValueError("会员不存在")
        current_points = members[member_id]
        if current_points < points:
            raise ValueError("积分不足")
        members[member_id] -= points
        return members[member_id]
    except Exception as e:
        return str(e)

def get_points(member_id):
    """
    查询会员积分
    :param member_id: 会员ID
    :return: 会员积分
    """
    try:
        if member_id not in members:
            raise ValueError("会员不存在")
        return members[member_id]
    except Exception as e:
        return str(e)

def create_member(member_id):
    """
    创建会员
    :param member_id: 会员ID
    """
    members[member_id] = 0
def main():
    """
    主函数
    """
    members = {}
    # 创建会员
    create_member(1)
    create_member(2)
    # 添加积分
    add_points(1, 100)
    add_points(2, 200)
    # 扣除积分
    deduct_points(1, 50)
    deduct_points(2, 100)
    # 查询积分
    print(get_points(1))
    print(get_points(2))
if __name__ == "__main__":
    members = {}
    # 初始化会员数据
    with open("members.json", "r") as f:
        members = json.load(f)
    # 创建Gradio接口
    with gr.Blocks() as demo:
        gr.Markdown("## 会员积分系统")
        add_points_btn = gr.Button("添加积分")
        deduct_points_btn = gr.Button("扣除积分")
        member_id_input = gr.Textbox(label="会员ID")
        points_input = gr.Textbox(label="积分")
        points_output = gr.Textbox(label="更新后的积分")
        add_points_btn.click(fn=add_points, inputs=(member_id_input, points_input), outputs=points_output)
        deduct_points_btn.click(fn=deduct_points, inputs=(member_id_input, points_input), outputs=points_output)
        points_output = gr.Textbox(label="会员积分")
        member_id_input = gr.Textbox(label="会员ID")
        points_output.change(fn=get_points, inputs=member_id_input, outputs=points_output)
    demo.launch()
    # 保存会员数据
    with open("members.json", "w") as f:
        json.dump(members, f)