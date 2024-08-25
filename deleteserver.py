import json
from defines import *


debug = Config["Debug"]

# 打开服务器列表文件，以追加写方式打开
ServerListFile = open("Servers.json", "a+")

# 将文件指针移到文件开头
ServerListFile.seek(0)

# 读取文件内容并将其解析为JSON格式
ServerListFileData = ServerListFile.read()
ServerList = json.loads(ServerListFileData)

# 如果调试模式启用，打印服务器列表
if debug:
    print(ServerList)

cprint("ServerList:", "light_blue")
# 打印空行
print()
for ServerNum in range(len(ServerList)):
    cprint(f"ServerNum:{colored(ServerNum, "blue")}", "red")
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
