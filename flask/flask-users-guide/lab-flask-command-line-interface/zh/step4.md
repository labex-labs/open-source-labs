# 创建自定义命令

Flask CLI 允许你创建可从命令行执行的自定义命令。让我们创建一个名为 `greet` 的自定义命令，它接受一个名字作为参数并打印一条问候消息。

创建一个名为 `commands.py` 的新 Python 文件，并添加以下代码：

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

保存文件，并使用以下命令执行它：

```
python commands.py John
```

你应该会在终端中看到“Hello, John!”这条消息被打印出来。
