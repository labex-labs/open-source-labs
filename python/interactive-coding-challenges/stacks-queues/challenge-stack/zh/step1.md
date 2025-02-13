# 栈

## 问题

用 Python 中的链表实现一个栈，具备以下方法：

- push：将一个元素添加到栈顶
- pop：移除并返回栈顶的元素。如果栈为空，则返回 None
- peek：返回栈顶的元素而不移除它。如果栈为空，则返回 None
- is_empty：如果栈为空，则返回 True，否则返回 False

## 要求

应满足以下要求：

- 当从空栈中弹出元素时，返回 None
- 实现应使用链表
- 实现应为 Python 语言
- 实现应包含 push、pop、peek 和 is_empty 这四个方法

## 示例用法

### 入栈

- 向空栈入栈：stack.push(1)
- 向非空栈入栈：stack.push(2)

### 出栈

- 从空栈出栈：stack.pop() -> None
- 从单元素栈出栈：stack.pop() -> 1
- 从多元素栈出栈：stack.pop() -> 2

### 查看栈顶元素

- 查看空栈的栈顶元素：stack.peek() -> None
- 查看有一个或多个元素的栈的栈顶元素：stack.peek() -> 2

### 判断栈是否为空

- 空栈时判断是否为空：stack.is_empty() -> True
- 有一个或多个元素的栈时判断是否为空：stack.is_empty() -> False
