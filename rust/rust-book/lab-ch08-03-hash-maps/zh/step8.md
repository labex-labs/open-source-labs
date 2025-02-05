# 根据旧值更新值

哈希映射的另一个常见用例是查找键的值，然后根据旧值对其进行更新。例如，清单 8-25 展示了一段代码，用于统计某些文本中每个单词出现的次数。我们使用一个以单词为键的哈希映射，并增加其值来跟踪我们看到该单词的次数。如果这是我们第一次看到某个单词，我们将首先插入值 `0`。

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```

清单 8-25：使用存储单词及其计数的哈希映射统计单词出现次数

这段代码将打印 `{"world": 2, "hello": 1, "wonderful": 1}`。你可能会看到相同的键值对以不同的顺序打印出来：回想一下“在哈希映射中访问值”，遍历哈希映射时顺序是任意的。

`split_whitespace` 方法返回一个迭代器，该迭代器遍历 `text` 中按空格分隔的子切片。`or_insert` 方法返回指定键对应值的可变引用（`&mut V`）。在这里，我们将该可变引用存储在 `count` 变量中，所以为了给该值赋值，我们必须首先使用星号（`*`）对 `count` 进行解引用。可变引用在 `for` 循环结束时超出作用域，所以所有这些更改都是安全的，并且符合借用规则。
