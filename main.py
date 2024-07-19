import pexpect
import json
from termcolor import colored, cprint

"""

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

# 是否开启调试模式
debug = False

# 打开服务器列表文件
ServerListFile = open("Servers.txt", "r")
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


def print_server_info(info, server_data, server_num):
    """
    打印服务器信息。

    :param info: 需要打印的信息类型（名称、IP、端口、用户名、密码或所有信息）。
    :param server_data: 服务器数据列表。
    :param server_num: 服务器编号。
    """
    if info == "name":
        print(colored("ServerName:", "yellow"), end="")
        cprint(server_data[server_num]["name"], "green")
    elif info == "ip":
        print(colored("ServerIP:", "yellow"), end="")
        cprint(server_data[server_num]["ip"], "green")
    elif info == "port":
        print(colored("ServerPort:", "yellow"), end="")
        cprint(server_data[server_num]["port"], "green")
    elif info == "username":
        print(colored("ServerUsername:", "yellow"), end="")
        cprint(server_data[server_num]["username"], "green")
    elif info == "password":
        print(colored("ServerPassword:","yellow"), end="")
        cprint(server_data[server_num]["password"], "green")
    elif info == "all":
        print(colored("ServerName:", "yellow"), end="")
        cprint(server_data[server_num]["name"], "green")
        print(colored("ServerIP:", "yellow"), end="")
        cprint(server_data[server_num]["ip"], "green")
        print(colored("ServerPort:", "yellow"), end="")
        cprint(server_data[server_num]["port"], "green")
        print(colored("ServerUsername:", "yellow"), end="")
        cprint(server_data[server_num]["username"], "green")
        print(colored("ServerPassword:","yellow"), end="")
        cprint(server_data[server_num]["password"], "green")


# 调试模式下打印第一台服务器的名称
if debug:
    print_server_info("name", ServerList, 0)
# 打印服务器列表
cprint("ServerList:","light_blue")
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
        ServerNum = int(input(colored("ServerNum:","light_grey")))
        # 使用ssh登录指定的服务器
        shell = pexpect.spawn(
            f'ssh -p {ServerList[ServerNum]["port"]} {ServerList[ServerNum]["username"]}@{ServerList[ServerNum]["ip"]}')
        # 等待密码提示，输入密码后交互式登录
        shell.expect("password:")
        shell.sendline(ServerList[ServerNum]["password"])
        shell.interact()
    finally:
        # 确保文件在程序结束时关闭
        ServerListFile.close()
