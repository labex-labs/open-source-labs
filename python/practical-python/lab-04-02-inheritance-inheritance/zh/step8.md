# 使用继承

继承有时用于组织相关的对象。

```python
class Shape:
 ...

class Circle(Shape):
 ...

class Rectangle(Shape):
 ...
```

思考一个逻辑层次结构或分类法。然而，更常见（且实用）的用途与创建可复用或可扩展的代码有关。例如，一个框架可能定义一个基类，并指示你对其进行定制。

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
     ...
        # 自定义处理
```

基类包含一些通用代码。你的类继承并定制特定部分。
