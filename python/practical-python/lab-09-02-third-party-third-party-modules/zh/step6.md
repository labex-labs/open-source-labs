# 虚拟环境

解决软件包安装问题的一个常见方法是为自己创建一个所谓的“虚拟环境”。当然，实现这一点并没有“唯一的方法”——实际上，有几种相互竞争的工具和技术。不过，如果你使用的是标准的 Python 安装，你可以尝试输入以下命令：

```bash
$ sudo apt install python3-venv
$ python -m venv mypython
bash %
```

等待片刻后，你将拥有一个新的目录 `mypython`，这是你自己的小型 Python 安装环境。在该目录中，你会找到一个 `bin/` 目录（适用于 Unix）或一个 `Scripts/` 目录（适用于 Windows）。如果你运行在那里找到的 `activate` 脚本，它将“激活”这个版本的 Python，使其成为 shell 的默认 `python` 命令。例如：

```bash
$ source mypython/bin/activate
(mypython) bash %
```

从这里开始，你现在可以为自己安装 Python 软件包了。例如：

    (mypython) $ python -m pip install pandas

...

对于实验和尝试不同的软件包来说，虚拟环境通常能很好地工作。另一方面，如果你正在创建一个应用程序，并且它有特定的软件包依赖项，那就是一个稍有不同的问题了。
