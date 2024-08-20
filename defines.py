from termcolor import *
import json

# 是否开启调试模式
ConfigFile = open("config.json", "r")
ConfigFileData = ConfigFile.read()
Config = json.loads(ConfigFileData)

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
        if server_data[server_num]["port"] == "22":
            pass
        else:
            print(colored("ServerPort:", "yellow"), end="")
            cprint(server_data[server_num]["port"], "green")
    elif info == "username":
        print(colored("ServerUsername:", "yellow"), end="")
        cprint(server_data[server_num]["username"], "green")
    elif info == "password":
        print(colored("ServerPassword:", "yellow"), end="")
        if Config["ShowPassword"]:
            cprint(server_data[server_num]["password"], "green")
        else:
            cprint("*" * len(server_data[server_num]["password"]), "green")
    elif info == "all":
        print_server_info("name", server_data, server_num)
        print_server_info("ip", server_data, server_num)
        print_server_info("port", server_data, server_num)
        print_server_info("username", server_data, server_num)
        print_server_info("password", server_data, server_num)
