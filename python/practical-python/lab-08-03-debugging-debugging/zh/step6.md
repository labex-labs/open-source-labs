# 在调试器下运行

你也可以在调试器下运行整个程序。

```bash
$ python3 -m pdb someprogram.py
```

它会在第一条语句之前自动进入调试器，让你能够设置断点并更改配置。

常见的调试器命令：

```code
(Pdb) help            # 获取帮助
(Pdb) w(here)         # 打印堆栈跟踪
(Pdb) d(own)          # 下移一个堆栈层级
(Pdb) u(p)            # 上移一个堆栈层级
(Pdb) b(reak) loc     # 设置断点
(Pdb) s(tep)          # 执行一条指令
(Pdb) c(ontinue)      # 继续执行
(Pdb) l(ist)          # 列出源代码
(Pdb) a(rgs)          # 打印当前函数的参数
(Pdb)!statement      # 执行语句
```

对于断点，位置可以是以下之一。

```code
(Pdb) b 45            # 当前文件的第45行
(Pdb) b file.py:45    # file.py的第45行
(Pdb) b foo           # 当前文件中的函数foo()
(Pdb) b module.foo    # 模块中的函数foo()
```
