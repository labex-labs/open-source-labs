# 配置应用程序

在同一个 `__init__.py` 文件中，为你的应用程序添加必要的配置细节。这包括设置一个密钥并指定数据库文件的位置。

```python
# flaskr/__init__.py

# 上面还有更多代码...

if test_config is None:
    # 如果不是在测试，加载实例配置（如果存在）
    app.config.from_pyfile('config.py', silent=True)
else:
    # 如果传入了测试配置，则加载测试配置
    app.config.from_mapping(test_config)

# 确保实例文件夹存在
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# 一个简单的页面，显示“Hello”
@app.route('/')
def hello():
    return 'Hello, World!'
```
