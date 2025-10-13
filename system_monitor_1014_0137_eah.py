# 代码生成时间: 2025-10-14 01:37:18
import psutil
# NOTE: 重要实现细节
import gr

"""
系统资源监控器
使用Python和GRADIO框架实现系统资源监控功能
"""
# 改进用户体验

def get_system_info():
    """获取系统信息"""
    try:
        # 获取CPU使用率
        cpu_usage = psutil.cpu_percent(interval=1)
        # 获取内存使用情况
        memory_usage = psutil.virtual_memory().percent
        # 获取磁盘使用情况
# 优化算法效率
        disk_usage = psutil.disk_usage('/').percent
        # 获取网络使用情况
        network_sent, network_recv = psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv
        
        return {
            "CPU Usage": cpu_usage,
# FIXME: 处理边界情况
            "Memory Usage": memory_usage,
            "Disk Usage": disk_usage,
# 优化算法效率
            "Network Sent": network_sent,
            "Network Received": network_recv
# 扩展功能模块
        }
# 优化算法效率
    except Exception as e:
# NOTE: 重要实现细节
        # 错误处理
        print(f"Error: {e}")
        return None


def main():
    """主函数"""
    # 创建GUI界面
# 扩展功能模块
    interface = gr.Interface(
        get_system_info,
        inputs=[],
# NOTE: 重要实现细节
        outputs="json",
        title="System Monitor",
        description="Monitor system resources using GRADIO and Python"
    )
    
    # 启动GUI界面
    interface.launch()
# NOTE: 重要实现细节

if __name__ == "__main__":
    main()