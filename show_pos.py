import cv2
import tkinter as tk
from tkinter import filedialog

# 回调函数，用于处理鼠标事件
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # 显示当前鼠标位置的像素点坐标
        pixel_value = image[y, x]  # 获取像素值
        print(f'鼠标位置坐标：({x}, {y}), 像素值：{pixel_value}')

# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 打开文件对话框，让用户选择图像文件
file_path = filedialog.askopenfilename()

# 检查用户是否选择了文件
if file_path:
    # 读取所选图像文件
    image = cv2.imread(file_path)

    # 创建窗口并将鼠标事件回调函数与之关联
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', mouse_callback)

    while True:
        cv2.imshow('Image', image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # 按下ESC键退出
            break

    cv2.destroyAllWindows()
