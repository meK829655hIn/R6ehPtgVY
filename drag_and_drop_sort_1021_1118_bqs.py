# 代码生成时间: 2025-10-21 11:18:30
import gradio as gr
def drag_and_drop_sort(event):
    # 获取拖拽排序组件的结果
    item = event.data["item"]
    # 根据拖拽后的索引重新排序列表
    sorted_list = sorted(event.data["item"], key=lambda x: event.data["new_index"].get(x, 0))
    return sorted_list

# 创建拖拽排序组件
with gr.Blocks() as demo:
    # 创建一个列表，用于显示在拖拽排序组件中
    items = ["Apple", "Banana", "Cherry", "Date"]
    
    # 创建拖拽排序组件
    drag_and_drop = gr.DragAndDrop(
        label="Drag and Drop", 
        value=items, 
        elements=items, 
        max_drag=1, 
        drag_target_size=[50, 50]
    )
    
    # 创建输出组件，用于显示排序后的结果
    output = gr.Textbox(label="Sorted List")
    
    # 将拖拽排序组件和输出组件连接
    drag_and_drop.change(drag_and_drop_sort, inputs=drag_and_drop, outputs=output)
    
# 启动应用
demo.launch()
