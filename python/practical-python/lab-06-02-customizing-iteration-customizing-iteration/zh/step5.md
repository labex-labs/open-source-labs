# 练习6.6：使用生成器生成数据

如果你查看练习6.5中的代码，代码的第一部分在生成数据行，而 `while` 循环末尾的语句在消费数据。生成器函数的一个主要特性是你可以将所有数据生成代码移动到一个可复用的函数中。

修改练习6.5中的代码，使得文件读取由生成器函数 `follow(filename)` 来执行。确保以下代码能够正常工作：

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... 这里应该会看到输出的行...
```

将股票报价器代码修改成如下形式：

```python
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
