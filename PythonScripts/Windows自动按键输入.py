from pywinauto import application
import win32gui,win32ui,win32con
import win32api
import time
import msvcrt
import ctypes
# DC在pywin32中是一个重要概念。
# windows不允许程序直接访问硬件，所有的操作都需要通过一个设备上下文环境。
# 屏幕上的每个窗口都对应一个DC。DC相当于一个视频缓冲区，对这个缓冲区的操作，
# 会表现在这个缓冲区对应的屏幕窗口上。
# 除了窗口对应的DC外，还可以自己创建DC,
# 然后在创建的DC上面建立数据拷贝到窗口的DC上，就相当于刷新窗口的DC。
def input_windows(windowsname,filename):
    hwnd=win32gui.FindWindow(None,windowsname)
    bu = win32gui.FindWindowEx(hwnd, None, 'Button', None)
    win32gui.SetForegroundWindow(hwnd)
    scancodes = [74, 65, 67, 65, 72]
    for code in scancodes:
        win32api.keybd_event(code, 0, 0, 0)
        win32api.keybd_event(code, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
    # win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, None, 'World')
    # #win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    # win32api.keybd_event(83, 0, 0, 0)  # v键位码是86
    # win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    # win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)
    #win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
    #win32gui.PostMessage(bu, win32con.BN_CLICKED, win32con.MK_LBUTTON, 0)
    win32gui.SendMessage(bu, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    # 鼠标左键抬起
    win32gui.SendMessage(bu, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

hwnd_title=dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

def get_windows(windowsname,filename):
    # 获取窗口句柄,这个函数我们仅能用来找主窗口
    handle=win32gui.FindWindow(None,windowsname)
    win32gui.SetForegroundWindow(handle)#将窗口放在前台并激活
    hdDC=win32gui.GetWindowDC(handle)#获取窗口DC
    newhdDC=win32ui.CreateDCFromHandle(hdDC)#创建一个兼容设备内存的DC
    saveDC=newhdDC.CreateCompatibleDC()
    saveBitmap=win32ui.CreateBitmap()
    # 获取窗口的位置信息
    left,top,right,bottom=win32gui.GetWindowRect(handle)
    # 窗口长宽
    width=right-left
    height=bottom-top
    # bitmap初始化
    saveBitmap.CreateCompatibleBitmap(newhdDC, width, height)
    saveDC.SelectObject(saveBitmap)
    saveDC.BitBlt((0, 0), (width, height), newhdDC, (0, 0), win32con.SRCCOPY)
    saveBitmap.SaveBitmapFile(saveDC, filename)

if __name__ == '__main__':
    # get_windows("HFC4253C1K7E45KS(0-0-40)_设计核实版20201103.xlsx - WPS 表格","12.png")
    win32gui.EnumWindows(get_all_hwnd,0)
    for h,t in hwnd_title.items():
        if t != "":
            print(h,t)
    input_windows("核对数字证书口令","")
