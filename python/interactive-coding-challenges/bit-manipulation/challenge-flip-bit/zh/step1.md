# 翻转位

## 问题

给定一个二进制数，我们需要将其中一位从0翻转为1，以最大化最长的1序列。例如，如果我们有二进制数 `000011110000`，我们可以将第四位从0翻转为1，得到 `000111110000`，其有一个长度为五个1的序列。我们的目标是编写一个Python函数，该函数接受一个二进制数，并返回翻转一位后最长的1序列的长度。

## 要求

我们的Python函数的要求如下：

- 输入必须是二进制形式的整数。
- 我们可以假设输入是一个32位的数字。
- 我们不必验证输入的长度。
- 输出必须是一个整数。
- 我们不能假设输入是有效的。
- 由于Python没有 >>> 运算符，我们可以假设使用的是正数。
- 我们可以假设这适合内存。

## 示例用法

以下是我们的Python函数应有的一些行为示例：

- `None` -> 异常
- `11111111111111111111111111111111` -> 32
- `00000000000000000000000000000000` -> 1
- `00001111110111011111001111110000` -> 10
