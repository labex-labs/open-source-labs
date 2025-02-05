# 在服务器上安装应用程序

将wheel文件复制到你的服务器。文件传输到服务器后，设置一个新的Python虚拟环境，并使用pip安装该wheel文件：

```bash
# 安装wheel文件
pip install flaskr-1.0.0-py3-none-any.whl
```

由于这是一个新环境，你需要再次初始化数据库：

```bash
# 初始化数据库
flask --app flaskr init-db
```
