# 克隆

在处理资源时，默认行为是在赋值或函数调用期间转移它们。然而，有时我们也需要复制资源。

`Clone` 特性正是帮助我们实现这一点。最常见的是，我们可以使用由 `Clone` 特性定义的 `.clone()` 方法。

```rust
// 一个没有资源的单元结构体
#[derive(Debug, Clone, Copy)]
struct Unit;

// 一个包含资源且实现了 `Clone` 特性的元组结构体
#[derive(Clone, Debug)]
struct Pair(Box<i32>, Box<i32>);

fn main() {
    // 实例化 `Unit`
    let unit = Unit;
    // 复制 `Unit`，没有资源需要移动
    let copied_unit = unit;

    // 两个 `Unit` 都可以独立使用
    println!("原始: {:?}", unit);
    println!("副本: {:?}", copied_unit);

    // 实例化 `Pair`
    let pair = Pair(Box::new(1), Box::new(2));
    println!("原始: {:?}", pair);

    // 将 `pair` 移动到 `moved_pair` 中，移动资源
    let moved_pair = pair;
    println!("已移动: {:?}", moved_pair);

    // 错误！`pair` 已经失去了它的资源
    //println!("原始: {:?}", pair);
    // TODO ^ 尝试取消注释这一行

    // 将 `moved_pair` 克隆到 `cloned_pair` 中（包括资源）
    let cloned_pair = moved_pair.clone();
    // 使用 std::mem::drop 丢弃原始的 pair
    drop(moved_pair);

    // 错误！`moved_pair` 已经被丢弃
    //println!("副本: {:?}", moved_pair);
    // TODO ^ 尝试取消注释这一行

    // 来自.clone() 的结果仍然可以使用！
    println!("克隆: {:?}", cloned_pair);
}
```
