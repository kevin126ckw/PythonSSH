import json

# 是否开启调试模式
ConfigFile = open("config.json", "r")
ConfigFileData = ConfigFile.read()
Config = json.loads(ConfigFileData)

debug = Config["Debug"]

# 提示用户确保Servers.txt文件未被打开，按回车继续
input("Please make sure the Servers.json is not open. Press enter to continue")

# 打开服务器列表文件，以追加写方式打开
ServerListFile = open("Servers.json", "a+")

# 将文件指针移到文件开头
ServerListFile.seek(0)

# 读取文件内容
ServerListFileData = ServerListFile.read()

# 如果调试模式开启，打印文件内容
if debug:
    print(ServerListFileData)

# 将文件内容解析为JSON格式
ServerList = json.loads(ServerListFileData)

# 依次输入新服务器的名称、IP、端口、用户名和密码
server_name = input("Please enter the name of the server: ")
server_ip = input("Please enter the IP of the server: ")
server_port = input("Please enter the port of the server(leave blank to use default): ")
if server_port == "" or server_port == " ":
    server_port = "22"
server_username = input("Please enter the username of the server: ")
server_password = input("Please enter the password of the server: ")

# 构建新服务器的信息字典
server_data = {
    "name": server_name,
    "ip": server_ip,
    "port": server_port,
    "username": server_username,
    "password": server_password
}

# 如果调试模式开启，打印新服务器的信息
if debug:
    print(server_data)

# 将新服务器信息添加到服务器列表中
ServerList.append(server_data)

# 清空文件内容，准备写入更新后的服务器列表
ServerListFile.truncate(0)

# 将服务器列表写入文件
ServerListFile.write(json.dumps(ServerList))

# 关闭文件
ServerListFile.close()

# 提示服务器添加成功
print(f'Server {server_name} added successfully!')

# 等待用户输入，以关闭程序
input("Press enter to close")
