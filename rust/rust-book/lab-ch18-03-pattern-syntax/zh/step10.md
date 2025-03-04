# 解构结构体和元组

我们可以用更复杂的方式混合、匹配和嵌套解构模式。下面的示例展示了一种复杂的解构，我们在一个元组中嵌套结构体和元组，并解构出所有的原始值：

```rust
let ((feet, inches), Point { x, y }) =
    ((3, 10), Point { x: 3, y: -10 });
```

这段代码让我们能够将复杂类型分解为其组成部分，这样我们就可以分别使用我们感兴趣的值。

使用模式进行解构是一种方便的方式，可以将值的各个部分（例如结构体中每个字段的值）彼此分开使用。
