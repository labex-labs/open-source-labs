# 模块搜索路径

如前所述，`sys.path` 包含搜索路径。如有需要，你可以手动调整。

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

路径也可以通过环境变量添加。

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles',...]
```

一般来说，无需手动调整模块搜索路径。不过，当你尝试导入位于不寻常位置或当前工作目录无法轻易访问的 Python 代码时，有时就需要这么做。

对于这个涉及模块的练习，确保你在合适的环境中运行 Python 至关重要。模块常常会给新程序员带来与当前工作目录或 Python 路径设置相关的问题。对于本课程，假定你将所有代码都写在 `~/project` 目录中。为了获得最佳效果，启动解释器时你也应该确保处于该目录中。如果不是，你需要确保将 `~/project` 添加到 `sys.path` 中。
