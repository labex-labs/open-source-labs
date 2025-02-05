# 包含必要文件

setuptools 构建后端需要另一个名为 `MANIFEST.in` 的文件，以便在项目中包含非 Python 文件。

创建一个包含以下内容的 `MANIFEST.in`：

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

这会告知构建过程复制 `static` 和 `templates` 目录中的所有内容以及 `schema.sql` 文件，同时排除所有字节码文件。
