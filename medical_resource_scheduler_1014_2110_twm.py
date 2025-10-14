# 代码生成时间: 2025-10-14 21:10:35
import gradio as gr
def schedule_medical_resources(patient_data):
    """
    根据患者数据分配医疗资源。
    :param patient_data: 包含患者信息的字典，例如{'症状': '头痛', '紧急程度': 5}
    :return: 分配的医疗资源信息
    """
    try:
        # 根据症状和紧急程度分配资源
        if patient_data['紧急程度'] > 3:
            return {'资源': '紧急护理', '说明': '由于紧急程度高，分配紧急护理'}
        else:
            return {'资源': '普通护理', '说明': '紧急程度低，分配普通护理'}
    except KeyError:
        return {'资源': '未知', '说明': '患者数据不完整'}
    except Exception as e:
        return {'资源': '错误', '说明': str(e)}

# 创建Gradio界面
with gr.Blocks() as demo:
    with gr.Row():
        # 输入框，收集患者数据
        patient_input = gr.Textbox(label="患者症状")
        urgency_input = gr.Slider(label="紧急程度", minimum=1, maximum=5, step=1)
    # 输出框，显示医疗资源分配结果
    resource_output = gr.Textbox(label="医疗资源分配结果")

    # 连接输入和输出
    resource_output.change(schedule_medical_resources, 
                            inputs=[patient_input, urgency_input], 
                            outputs=resource_output)

# 启动Gradio界面
demo.launch()