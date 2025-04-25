# `Iterator::any`

`Iterator::any` 是一个函数，当传入一个迭代器时，如果有任何元素满足谓词条件，它将返回 `true`，否则返回 `false`。其签名如下：

```rust
pub trait Iterator {
    // 正在迭代的类型。
    type Item;

    // `any` 接受 `&mut self`，这意味着调用者可能会被借用并修改，但不会被消耗。
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut` 表示任何捕获的变量最多只能被修改，不能被消耗。`Self::Item` 表明它按值将参数传递给闭包。
        F: FnMut(Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // 对向量调用 `iter()` 会产生 `&i32`。解构为 `i32`。
    println!("2 在 vec1 中：{}", vec1.iter().any(|&x| x == 2));
    // 对向量调用 `into_iter()` 会产生 `i32`。无需解构。
    println!("2 在 vec2 中：{}", vec2.into_iter().any(|x| x == 2));

    // `iter()` 仅借用 `vec1` 及其元素，因此它们可以再次使用
    println!("vec1 的长度：{}", vec1.len());
    println!("vec1 的第一个元素是：{}", vec1[0]);
    // `into_iter()` 会移动 `vec2` 及其元素，因此它们不能再被使用
    // println!("vec2 的第一个元素是：{}", vec2[0]);
    // println!("vec2 的长度：{}", vec2.len());
    // 待办事项：取消注释上面两行并查看编译器错误。

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // 对数组调用 `iter()` 会产生 `&i32`。
    println!("2 在 array1 中：{}", array1.iter().any(|&x| x == 2));
    // 对数组调用 `into_iter()` 会产生 `i32`。
    println!("2 在 array2 中：{}", array2.into_iter().any(|x| x == 2));
}
```
