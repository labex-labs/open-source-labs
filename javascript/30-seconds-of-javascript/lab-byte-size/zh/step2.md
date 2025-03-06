# 使用 Blob 计算字符串字节大小

既然你已经了解了字符串的表示方式，接下来让我们学习如何使用 `Blob` 对象计算字符串的实际字节大小。

`Blob`（二进制大对象，Binary Large Object）表示一个不可变的原始数据的类文件对象。通过将字符串转换为 Blob，你可以访问其 `size` 属性来确定字节大小。

在 Node.js 控制台中，让我们创建一个函数来计算字节大小：

```javascript
const byteSize = (str) => new Blob([str]).size;
```

这个函数接受一个字符串作为输入，将其转换为 Blob，并返回其字节大小。

让我们用一个简单的例子来测试这个函数：

```javascript
byteSize("Hello World");
```

你应该会看到输出：

```
11
```

在这种情况下，字符数量和字节大小相同，因为 "Hello World" 只包含 ASCII 字符，每个字符由一个字节表示。

现在让我们尝试一个非 ASCII 字符：

```javascript
byteSize("😀");
```

你应该会看到输出：

```
4
```

这表明虽然这个表情符号看起来是一个字符，但实际上它占用了 4 个字节的存储空间。
