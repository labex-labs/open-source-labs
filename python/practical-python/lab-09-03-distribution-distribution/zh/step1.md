# 创建一个 setup.py 文件

在你的项目目录的顶级目录 `/home/labex/project` 中添加一个 `setup.py` 文件。

```python
# setup.py
import setuptools

setuptools.setup(
    name="porty",
    version="0.0.1",
    author="你的名字",
    author_email="you@example.com",
    description="实用的 Python 代码",
    packages=setuptools.find_packages(),
)
```
