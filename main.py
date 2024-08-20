import os

import pexpect

from defines import *

a = r"""

                             _ooOoo_
                            o8888888o
                            88" . "88
                            (| -_- |)
                            O\  =  /O
                         ____/`---'\____
                       .'  \\|     |//  `.
                      /  \\|||  :  |||//  \
                     /  _||||| -:- |||||-  \
                     |   | \\\  -  /// |   |
                     | \_|  ''\---/''  |   |
                     \  .-\__  `-`  ___/-. /
                   ___`. .'  /--.--\  `. . __
                ."" '<  `.___\_<|>_/___.'  >'"".
               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               \  \ `-.   \_ __\ /__ _/   .-` /  /
          ======`-.____`-.___\_____/___.-`____.-'======
                             `=---='
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     佛祖保佑        永无BUG
            佛曰:
                   写字楼里写字间，写字间里程序员；
                   程序人员写程序，又拿程序换酒钱。
                   酒醒只在网上坐，酒醉还来网下眠；
                   酒醉酒醒日复日，网上网下年复年。
                   但愿老死电脑间，不愿鞠躬老板前；
                   奔驰宝马贵者趣，公交自行程序员。
                   别人笑我忒疯癫，我笑自己命太贱；
                   不见满街漂亮妹，哪个归得程序员？
"""

# 新版本已经将读取配置文件的代码移动到defines.py中

debug = Config["Debug"]
if debug:
    cprint("Debug Enabled", "yellow", attrs=["bold"])
if debug:
    print(a)
# 打开服务器列表文件
ServerListFile = open("Servers.json", "r")
# 读取文件内容
ServerListFileData = ServerListFile.read()
# 调试模式下打印文件内容
if debug:
    print("Servers.txt:", ServerListFileData)
# 将文件内容解析为JSON格式
ServerList = json.loads(ServerListFileData)
# 调试模式下打印解析后的数据
if debug:
    print("Serverlist(JsonDecode):", ServerList)

# 调试模式下打印第一台服务器的名称
if debug:
    print_server_info("name", ServerList, 0)
# 打印服务器列表
cprint("ServerList:", "light_blue")
# 打印空行
print()
for ServerNum in range(len(ServerList)):
    cprint(f"ServerNum:{colored(ServerNum, "blue")}", "red")
    # 打印每台服务器的所有信息
    print_server_info("all", ServerList, ServerNum)
    # 打印空行
    print()

while True:
    try:
        # 获取用户输入的服务器编号
        ServerNum = int(input(colored("ServerNum:", "light_grey")))
        # 清屏
        os.system("clear")
        # 使用ssh登录指定的服务器
        shell = pexpect.spawn(
            f'ssh -p {ServerList[ServerNum]["port"]} {ServerList[ServerNum]["username"]}@{ServerList[ServerNum]["ip"]}')
        # 等待密码提示，输入密码后交互式登录
        shell.expect("password:")
        if debug:
            print("Detected password prompt")
        shell.sendline(ServerList[ServerNum]["password"])
        if debug:
            print("Password sent")
            print("Dropping to interactive shell")
        shell.interact()
        if debug:
            print("interactive shell shutdown")
        # 如果配置文件中ClearScreenOnDisconnect为True，则清屏
        if Config["ClearScreenOnDisconnect"]:
            os.system("clear")
        cprint("ServerList:", "light_blue")
        # 打印空行
        print()
        for ServerNum in range(len(ServerList)):
            cprint(f"ServerNum:{colored(ServerNum, "blue")}", "red")
            # 打印每台服务器的所有信息
            print_server_info("all", ServerList, ServerNum)
            # 打印空行
            print()
    except KeyboardInterrupt:
        # 当用户通过Ctrl+C中断程序时，优雅地退出程序
        exit(0)

    finally:
        # 确保文件在程序结束时关闭
        ServerListFile.close()
