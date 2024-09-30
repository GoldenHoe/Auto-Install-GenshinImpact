import easygui,os,time
from selenium import webdriver
import wget
import sys,win32api
import pyautogui
import webbrowser
from win10toast import ToastNotifier

#自动获得管理员权限
def is_admin():
    try:
        # 在c:\windows目录下新建一个文件test01.txt
        testfile = os.path.join(os.getenv("windir"),"test01.txt")
        open(testfile,"w").close()
    except OSError: # 不成功
        return False
    else: # 成功
        os.remove(testfile) # 删除文件
        return True

print(is_admin())
if is_admin():
    filepath = 'download'
    if not os.path.isdir(filepath):
        # 创建文件夹
        os.mkdir(filepath)
    #检测有无之前的安装程序和临时文件，如果有，删除之前下载过的安装程序

    filenan=os.path.isfile("download/base.exe")
    if filenan == True:
        os.remove('download/base.exe')
    else:
        pass
    #使用CMD命令输出一个提示窗口
    os.system('mshta vbscript:msgbox("汗流浃背了吧老弟！",48,"原神自动安装程序")(window.close)')
    #从Edge打开云原神
    webbrowser.open_new('https://www.bilibili.com/video/BV1a14y1i7N4/?spm_id_from=333.337.search-card.all.click&vd_source=0c23d5da738e2b69356f395abec04def')
    driver = webdriver.Edge()
    driver.get('https://ys.mihoyo.com/cloud/#/')
    #目标URL和文件夹并下载安装程序
    URL = 'https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default'
    PATH = 'download/base.exe'
    wget.download(URL,PATH)
    while True:
        time.sleep(1)
        filena=os.path.isfile("download/base.exe")
        if filena == True:
            break
        if filena == False:
            pass
    time.sleep(2)
    os.system('start download/base.exe')
    #操作窗口和控制鼠标
    # 移动鼠标到指定位置
    time.sleep(1)
    pyautogui.moveTo(636,639)# 移动到 x=636, y=639 的位置，持续 1 秒
    # 模拟鼠标点击
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(948,571)# 移动到 x=948, y=571 的位置，持续 1 秒
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(948, 571)
    pyautogui.click()
    #必要的停止
    time.sleep(10)
    pyautogui.moveTo(1428,826)
    pyautogui.click()

else:
    # 以管理员权限重新运行程序
    win32api.ShellExecute(None,"runas", sys.executable, __file__, None, 1)