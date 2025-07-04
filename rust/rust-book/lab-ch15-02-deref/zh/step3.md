# 像使用引用一样使用 Box`<T>`

我们可以重写清单 15-6 中的代码，使用 `Box<T>` 而不是引用；清单 15-7 中对 `Box<T>` 使用的解引用运算符，其功能与清单 15-6 中对引用使用的解引用运算符相同。

文件名：`src/main.rs`

```rust
fn main() {
    let x = 5;
  1 let y = Box::new(x);

    assert_eq!(5, x);
  2 assert_eq!(5, *y);
}
```

清单 15-7：对 `Box<i32>` 使用解引用运算符

清单 15-7 和清单 15-6 的主要区别在于，这里我们将 `y` 设置为一个指向 `x` 的复制值的盒子实例，而不是指向 `x` 的值的引用（第 1 行）。在最后一个断言中（第 2 行），我们可以使用解引用运算符来跟随盒子的指针，就像 `y` 是引用时一样。接下来，我们将通过定义自己的盒子类型来探索 `Box<T>` 的特殊之处，正是这种特殊之处使我们能够使用解引用运算符。
