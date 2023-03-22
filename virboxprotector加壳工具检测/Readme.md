## VBP Detector

## 简介

该工具是一款基于开源技术开发的加壳检测工具，用于检测可执行文件是否被VirboxProtector加密。

## 环境要求

该工具可以在以下操作系统中运行：

- Windows 7及以上版本
- Linux系统

## 使用方法

### 下载工具

从我们的Github仓库中下载工具：https://github.com/chihuapeng/virbox-tools/tree/main/virboxprotector%E5%8A%A0%E5%A3%B3%E5%B7%A5%E5%85%B7%E6%A3%80%E6%B5%8B

### 安装依赖

该工具需要安装以下依赖：

- Python 3.6及以上版本

您可以使用以下命令安装依赖：

```
pip install tkinter
pip install pyinstaller
```

### 生成工具

在命令行中执行以下命令运行工具对程序进行生成：

#### windows

```bash
.\auto_run.bat
```

#### linux

```bash
chmod +x ./auto_run.sh
./auto_run.sh
```



### 使用工具

在工具的主界面中，您可以通过以下步骤使用工具：

1. 点击“读取文件”按钮，选择要检测的程序文件，并将文件路径添加到列表框中。
2. 点击“读取文件夹”按钮，选择要检测的程序所在的文件夹，并将文件夹中的所有程序文件路径添加到列表框中。
3. 点击“清空列表”按钮，清空列表框中的所有文件路径。
4. 点击“检测加壳”按钮，对列表框中的所有程序文件进行加壳检测。
5. 等待检测结果，列表框中的程序文件会根据检测结果变为绿色或红色。

## 联系我们

如果您在使用过程中遇到任何问题，或者有任何建议和反馈，请通过Github仓库中的Issues页面联系我们：https://github.com/chihuapeng/virbox-tools/tree/main/virboxprotector%E5%8A%A0%E5%A3%B3%E5%B7%A5%E5%85%B7%E6%A3%80%E6%B5%8B/issues



## 免责声明

该工具仅供技术研究和学习交流使用，请勿将其用于任何非法用途。对于使用该工具所造成的任何后果，作者不承担任何法律责任。使用该工具所产生的风险由使用者自行承担。如果您使用该工具，则默认您已接受本免责声明。