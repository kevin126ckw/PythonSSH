import json

# 启用调试模式
debug = True

# 打开服务器列表文件，以追加写方式打开
ServerListFile = open("Servers.txt","a+")

# 将文件指针移到文件开头
ServerListFile.seek(0)

# 读取文件内容并将其解析为JSON格式
ServerListFileData = ServerListFile.read()
ServerList = json.loads(ServerListFileData)

# 如果调试模式启用，打印服务器列表
if debug:
    print(ServerList)

def print_server_info(info, server_data, server_num):
    """
    根据提供的信息类型，打印服务器的详细信息。

    :param info: 信息类型（名称、IP、端口、用户名、密码或所有信息）。
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

# 遍历服务器列表，打印每台服务器的所有信息
for ServerNum in range(len(ServerList)):
    print("ServerNum:", ServerNum)
    # 打印每台服务器的所有信息
    print_server_info("all", ServerList, ServerNum)
    # 打印空行
    print()

# 请求用户输入要删除的服务器编号
del_server = input("input which server do you want to delete:")

# 如果用户想删除所有服务器
if del_server == "all":
    ServerListFile.truncate(0)
    ServerListFile.close()
    print("All Server Deleted")
    exit()
else:
    # 删除指定编号的服务器
    del ServerList[int(del_server)]
    # 将更新后的服务器列表写回文件
    ServerListFile.seek(0)
    ServerListFile.truncate(0)
    ServerListFile.write(json.dumps(ServerList))
    ServerListFile.close()
    print("Server Deleted")
    exit()
