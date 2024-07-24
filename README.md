# PythonSSH

这是一个简单的服务器管理工具，用于添加、删除和连接到服务器。它使用Python编写，并依赖于`pexpect`库来处理SSH连接。

## 前置条件

- Python 3.x
- `pexpect`库
- `termcolor`库

## 运行方法

1. 确保您的`Servers.json`文件未被其他程序打开。
2. 运行`addserver.py`以添加新服务器。
3. 运行`deleteserver.py`以删除服务器。
4. 运行`main.py`以连接到服务器。

## 构建方法

- 克隆或下载此仓库。
- 确保您的环境中安装了Python 3.x。
- 安装`pexpect`库（如果尚未安装）：`pip install pexpect`。
- 安装`termcolor`库（如果尚未安装）：`pip install termcolor`。

## 许可证

本项目采用MIT许可证。请查看`LICENSE`文件了解更多信息。

## 注意

- 请确保在运行脚本之前备份您的`Servers.json`文件。
- 本工具仅用于学习和测试目的，不应用于生产环境。

## 贡献

如果您有任何改进意见或想要贡献代码，请随时提交Pull Request或创建Issue。

## 免责声明

本项目不包含任何个人可识别信息（PII）或敏感数据。使用此工具时，请确保遵守所有适用的法律法规和网络安全最佳实践。
