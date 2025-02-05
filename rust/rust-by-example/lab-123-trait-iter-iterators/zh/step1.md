# 迭代器

`Iterator` 特性用于在数组等集合上实现迭代器。

该特性只要求为 `next` 元素定义一个方法，这个方法既可以在 `impl` 块中手动定义，也可以自动定义（比如数组和范围的情况）。

为方便处理常见情形，`for` 结构通过 `.into_iter()` 方法将某些集合转换为迭代器。

```rust
struct Fibonacci {
    curr: u32,
    next: u32,
}

// 为 `Fibonacci` 实现 `Iterator`。
// `Iterator` 特性只要求为 `next` 元素定义一个方法。
impl Iterator for Fibonacci {
    // 我们可以使用 Self::Item 来引用这个类型
    type Item = u32;

    // 在这里，我们使用 `.curr` 和 `.next` 来定义序列。
    // 返回类型是 `Option<T>`：
    //     * 当 `Iterator` 结束时，返回 `None`。
    //     * 否则，下一个值被包装在 `Some` 中并返回。
    // 我们在返回类型中使用 Self::Item，这样我们可以在不更新函数签名的情况下更改类型。
    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;

        self.curr = self.next;
        self.next = current + self.next;

        // 由于斐波那契数列没有终点，`Iterator`
        // 永远不会返回 `None`，总是返回 `Some`。
        Some(current)
    }
}

// 返回一个斐波那契数列生成器
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // `0..3` 是一个生成 0、1 和 2 的 `Iterator`。
    let mut sequence = 0..3;

    println!("对 0..3 连续调用四次 `next`");
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());

    // `for` 会遍历 `Iterator` 直到它返回 `None`。
    // 每个 `Some` 值都会被解包并绑定到一个变量（这里是 `i`）。
    println!("使用 `for` 遍历 0..3");
    for i in 0..3 {
        println!("> {}", i);
    }

    // `take(n)` 方法将一个 `Iterator` 缩减为其前 `n` 项。
    println!("斐波那契数列的前四项是：");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    // `skip(n)` 方法通过丢弃前 `n` 项来缩短一个 `Iterator`。
    println!("斐波那契数列的接下来四项是：");
    for i in fibonacci().skip(4).take(4) {
        println!("> {}", i);
    }

    let array = [1u32, 3, 3, 7];

    // `iter` 方法会生成一个针对数组/切片的 `Iterator`。
    println!("遍历以下数组 {:?}", &array);
    for i in array.iter() {
        println!("> {}", i);
    }
}
```
