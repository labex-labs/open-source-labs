# Fizz Buzz

## 问题

使用 Python 实现 Fizz Buzz。你的函数应以整数 `n` 作为输入，并返回一个字符串列表，代表从 1 到 `n` 的数字，有以下替换规则：

- 3 的倍数应替换为字符串“Fizz”
- 5 的倍数应替换为字符串“Buzz”
- 3 和 5 的倍数都应替换为字符串“FizzBuzz”

你的函数还应处理以下情况：

- 如果输入小于 1，引发异常
- 如果输入不是有效的整数，引发异常

## 要求

要在 Python 中实现 Fizz Buzz，我们需要遵循以下要求：

- 定义一个以整数 `n` 作为输入的函数
- 检查输入是否为有效的整数，如果不是则引发异常
- 检查输入是否小于 1，如果是则引发异常
- 创建一个代表从 1 到 `n` 的数字的字符串列表，并进行上述替换
- 返回该列表

## 示例用法

```python
assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

```python
try:
    fizz_buzz(0)
except ValueError:
    print("无效输入")
```

```python
try:
    fizz_buzz("hello")
except ValueError:
    print("无效输入")
```

```python
try:
    fizz_buzz(-5)
except ValueError:
    print("无效输入")
```
