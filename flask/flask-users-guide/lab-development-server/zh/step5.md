# 地址已被使用

当你尝试启动服务器时，如果看到一条显示“Address already in use”（地址已被使用）的 `OSError`，这意味着另一个程序已经在使用开发服务器的默认端口 5000。你可以识别并停止该其他程序，或者选择一个不同的端口。

要识别使用端口 5000 的进程，你可以使用 `netstat` 或 `lsof` 命令。以下是针对 Linux、macOS 和 Windows 的示例：

- Linux：

```bash
netstat -nlp | grep 5000
```

- macOS / Linux：

```bash
lsof -P -i :5000
```

- Windows：

```bash
-ano > netstat | findstr 5000
```

一旦你识别出该进程，就可以使用其他操作系统工具来停止它。停止该进程后，你应该能够毫无问题地运行开发服务器。
