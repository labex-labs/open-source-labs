# 脚本模板

最后，这是一个作为命令行脚本运行的 Python 程序的通用代码模板：

```python
#!/usr/bin/env python3
#./prog.py

# 导入语句（库）
import modules

# 函数
def spam():
  ...

def blah():
  ...

# 主函数
def main(argv):
    # 解析命令行参数、环境等
  ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```
