# 构建应用程序

首先，我们需要为我们的应用创建一个 wheel 文件。我们将为此使用`build`工具。如果你还没有安装`build`工具，请使用 pip 进行安装：

```bash
# 安装build工具
pip install build
```

现在，使用`build`工具来创建 wheel 文件：

```bash
# 构建wheel文件
python -m build --wheel
```

wheel 文件应该位于`dist`目录中，名称类似于`flaskr-1.0.0-py3-none-any.whl`。
