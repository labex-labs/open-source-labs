# 使用不同类型的字符串进行测试

让我们来探究不同类型的字符如何影响字符串的字节大小。

在 Node.js 控制台中，让我们用各种字符串来测试我们的 `byteSize` 函数：

1. 普通英文文本：

```javascript
byteSize("The quick brown fox jumps over the lazy dog");
```

预期输出：

```
43
```

2. 数字和特殊字符：

```javascript
byteSize("123!@#$%^&*()");
```

预期输出：

```
13
```

3. ASCII 和非 ASCII 字符的混合：

```javascript
byteSize("Hello, 世界！");
```

预期输出：

```
13
```

4. 多个表情符号：

```javascript
byteSize("😀😃😄😁");
```

预期输出：

```
16
```

注意，当字符类型混合时，尤其是包含像中文字符和表情符号这样的非 ASCII 字符时，字节大小会大于字符数量。

在处理可能包含国际字符或特殊符号的数据时，理解这一点很重要，因为它会影响存储需求和数据传输大小。

让我们通过输入以下内容退出 Node.js 控制台：

```javascript
.exit
```

这将使你回到常规的终端提示符。
