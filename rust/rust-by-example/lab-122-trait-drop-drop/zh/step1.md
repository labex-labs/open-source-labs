# Drop

`Drop` 特性只有一个方法：`drop`，当对象超出作用域时会自动调用该方法。`Drop` 特性的主要用途是释放实现该特性的实例所拥有的资源。

`Box`、`Vec`、`String`、`File` 和 `Process` 是实现 `Drop` 特性以释放资源的一些类型示例。`Drop` 特性也可以为任何自定义数据类型手动实现。

以下示例在 `drop` 函数中添加了一个打印到控制台的操作，以告知何时调用该函数。

```rust
struct Droppable {
    name: &'static str,
}

// `drop` 的这个简单实现添加了一个打印到控制台的操作。
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // 代码块 A
    {
        let _b = Droppable { name: "b" };

        // 代码块 B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // 可以使用 `drop` 函数手动释放变量
    drop(_a);
    // TODO ^ 尝试注释掉这一行

    println!("end of the main function");

    // `_a` 在这里不会再次被 `drop`，因为它已经被（手动）`drop` 过了
}
```
