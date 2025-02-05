# `Rc`

当需要多重所有权时，可以使用 `Rc`（引用计数）。`Rc` 会跟踪引用的数量，这意味着包裹在 `Rc` 中的值的所有者数量。

每当克隆一个 `Rc` 时，其引用计数会增加 1；每当一个克隆的 `Rc` 超出作用域时，其引用计数会减少 1。当一个 `Rc` 的引用计数变为零（即没有剩余的所有者）时，`Rc` 和其包裹的值都会被释放。

克隆 `Rc` 永远不会执行深拷贝。克隆只会创建另一个指向被包裹值的指针，并增加引用计数。

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Rc examples".to_string();
    {
        println!("--- rc_a 被创建 ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("rc_a 的引用计数: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a 被克隆为 rc_b ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("rc_b 的引用计数: {}", Rc::strong_count(&rc_b));
            println!("rc_a 的引用计数: {}", Rc::strong_count(&rc_a));

            // 如果两个 `Rc` 的内部值相等，则它们相等
            println!("rc_a 和 rc_b 相等: {}", rc_a.eq(&rc_b));

            // 我们可以直接使用值的方法
            println!("rc_a 内部值的长度: {}", rc_a.len());
            println!("rc_b 的值: {}", rc_b);

            println!("--- rc_b 超出作用域 ---");
        }

        println!("rc_a 的引用计数: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a 超出作用域 ---");
    }

    // 错误！`rc_examples` 已经被移动到 `rc_a` 中
    // 并且当 `rc_a` 被释放时，`rc_examples` 也会一起被释放
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ 尝试取消注释这一行
}
```
