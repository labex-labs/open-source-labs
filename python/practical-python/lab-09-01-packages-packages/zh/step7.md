# 问题：主脚本

将包的子模块作为主脚本运行会出错。

```bash
$ python porty/pcost.py # 出错
...
```

_原因：你在单个文件上运行 Python，而 Python 无法正确识别包结构的其余部分（`sys.path` 有误）。_

所有导入都会出错。要解决这个问题，你需要以不同的方式运行程序，使用 `-m` 选项。

```bash
$ python -m porty.pcost # 可行
...
```
