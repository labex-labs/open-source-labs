# 向量

向量是可重新调整大小的数组。与切片一样，它们的大小在编译时是未知的，但可以随时增长或收缩。向量由三个参数表示：

- 指向数据的指针
- 长度
- 容量

容量表示为向量保留了多少内存。只要长度小于容量，向量就可以增长。当需要超过这个阈值时，向量会重新分配更大的容量。

```rust
fn main() {
    // 迭代器可以收集到向量中
    let collected_iterator: Vec<i32> = (0..10).collect();
    println!("将(0..10)收集到: {:?}", collected_iterator);

    // `vec!` 宏可用于初始化向量
    let mut xs = vec![1i32, 2, 3];
    println!("初始向量: {:?}", xs);

    // 在向量末尾插入新元素
    println!("将4推入向量");
    xs.push(4);
    println!("向量: {:?}", xs);

    // 错误！不可变向量不能增长
    collected_iterator.push(0);
    // FIXME ^ 注释掉这一行

    // `len` 方法返回当前存储在向量中的元素数量
    println!("向量长度: {}", xs.len());

    // 使用方括号进行索引（索引从0开始）
    println!("第二个元素: {}", xs[1]);

    // `pop` 从向量中移除最后一个元素并返回它
    println!("弹出最后一个元素: {:?}", xs.pop());

    // 越界索引会导致恐慌
    println!("第四个元素: {}", xs[3]);
    // FIXME ^ 注释掉这一行

    // 可以轻松遍历向量
    println!("xs的内容:");
    for x in xs.iter() {
        println!("> {}", x);
    }

    // 也可以在迭代时将迭代计数枚举到一个单独的变量 (`i`) 中，同时遍历向量
    for (i, x) in xs.iter().enumerate() {
        println!("在位置 {} 我们有值 {}", i, x);
    }

    // 由于 `iter_mut`，可变向量也可以以允许修改每个值的方式进行遍历
    for x in xs.iter_mut() {
        *x *= 3;
    }
    println!("更新后的向量: {:?}", xs);
}
```

在 `std::vec` 模块下可以找到更多 `Vec` 方法。
