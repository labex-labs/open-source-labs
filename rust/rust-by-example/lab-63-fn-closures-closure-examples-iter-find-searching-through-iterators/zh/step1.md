# 在迭代器中进行搜索

`Iterator::find` 是一个函数，它会遍历一个迭代器，并搜索满足某些条件的第一个值。如果没有值满足该条件，则返回 `None`。其签名如下：

```rust
pub trait Iterator {
    // 正在迭代的类型。
    type Item;

    // `find` 接受 `&mut self`，这意味着调用者可能会被借用并修改，但不会被消耗。
    fn find<P>(&mut self, predicate: P) -> Option<Self::Item> where
        // `FnMut` 表示任何捕获的变量最多只能被修改，不能被消耗。`&Self::Item` 表示它通过引用将参数传递给闭包。
        P: FnMut(&Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // 对向量调用 `iter()` 会产生 `&i32`。
    let mut iter = vec1.iter();
    // 对向量调用 `into_iter()` 会产生 `i32`。
    let mut into_iter = vec2.into_iter();

    // 对向量调用 `iter()` 会产生 `&i32`，并且我们想要引用其中一个元素，所以我们必须将 `&&i32` 解构为 `i32`
    println!("在 vec1 中查找 2: {:?}", iter.find(|&&x| x == 2));
    // 对向量调用 `into_iter()` 会产生 `i32`，并且我们想要引用其中一个元素，所以我们必须将 `&i32` 解构为 `i32`
    println!("在 vec2 中查找 2: {:?}", into_iter.find(| &x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // 对数组调用 `iter()` 会产生 `&&i32`
    println!("在 array1 中查找 2: {:?}", array1.iter().find(|&&x| x == 2));
    // 对数组调用 `into_iter()` 会产生 `&i32`
    println!("在 array2 中查找 2: {:?}", array2.into_iter().find(|&x| x == 2));
}
```

`Iterator::find` 会给你一个对该元素的引用。但如果你想要该元素的 _索引_，则使用 `Iterator::position`。

```rust
fn main() {
    let vec = vec![1, 9, 3, 3, 13, 2];

    // 对向量调用 `iter()` 会产生 `&i32`，并且 `position()` 不接受引用，所以
    // 我们必须将 `&i32` 解构为 `i32`
    let index_of_first_even_number = vec.iter().position(|&x| x % 2 == 0);
    assert_eq!(index_of_first_even_number, Some(5));

    // 对向量调用 `into_iter()` 会产生 `i32`，并且 `position()` 不接受引用，所以
    // 我们不需要解构
    let index_of_first_negative_number = vec.into_iter().position(|x| x < 0);
    assert_eq!(index_of_first_negative_number, None);
}
```
