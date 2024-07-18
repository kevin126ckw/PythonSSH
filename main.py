import pexpect
import json

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
        print("ServerName:", end="")
        print(server_data[server_num]["name"])
    elif info == "ip":
        print("ServerIP:", end="")
        print(server_data[server_num]["ip"])
    elif info == "port":
        print("ServerPort:", end="")
        print(server_data[server_num]["port"])
    elif info == "username":
        print("ServerUsername:", end="")
        print(server_data[server_num]["username"])
    elif info == "password":
        print("ServerPassword:", end="")
        print(server_data[server_num]["password"])
    elif info == "all":
        print("ServerName:", end="")
        print(server_data[server_num]["name"])
        print("ServerIP:", end="")
        print(server_data[server_num]["ip"])
        print("ServerPort:", end="")
        print(server_data[server_num]["port"])
        print("ServerUsername:", end="")
        print(server_data[server_num]["username"])
        print("ServerPassword:", end="")
        print(server_data[server_num]["password"])


# 调试模式下打印第一台服务器的名称
if debug:
    print_server_info("name", ServerList, 0)
# 打印服务器列表
print("ServerList:")
# 打印空行
print()
for ServerNum in range(len(ServerList)):
    print("ServerNum:", ServerNum)
    # 打印每台服务器的所有信息
    print_server_info("all", ServerList, ServerNum)
    # 打印空行
    print()

while True:
    try:
        # 获取用户输入的服务器编号
        ServerNum = int(input("ServerNum:"))
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
