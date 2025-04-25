# 运行应用程序

在你的应用程序设置和配置完成后，现在你可以使用 `flask` 命令来运行它。请确保从顶级目录运行此命令，而不是从 `flaskr` 包中运行。

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

你应该会看到类似这样的输出：

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

然后，打开 **Web 5000** 标签页，你应该会看到如下内容：

![Flask 应用程序的 Hello World 页面](../assets/hello-world.png)
