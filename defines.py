from termcolor import *
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
        print(colored("ServerPassword:", "yellow"), end="")
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
        print(colored("ServerPassword:", "yellow"), end="")
        cprint(server_data[server_num]["password"], "green")
