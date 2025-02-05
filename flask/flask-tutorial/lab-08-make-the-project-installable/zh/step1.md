# 描述项目

首先，我们需要创建一个`pyproject.toml`文件来描述我们的项目以及如何构建它。

`pyproject.toml`文件应如下所示：

```toml
# pyproject.toml

[project]
name = "flaskr" # 项目名称
version = "1.0.0" # 项目版本
dependencies = [
    "flask", # 项目依赖项
]

[build-system]
requires = ["setuptools"] # 所需的构建系统
build-backend = "setuptools.build_meta" # 后端构建系统
```
