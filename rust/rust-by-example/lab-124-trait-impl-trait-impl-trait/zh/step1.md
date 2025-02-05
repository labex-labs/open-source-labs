# `impl Trait`

`impl Trait` 可在两个位置使用：

1.  作为参数类型
2.  作为返回类型

## 作为参数类型

如果你的函数对某个 trait 是泛型的，但你不关心具体类型，那么可以使用 `impl Trait` 作为参数类型来简化函数声明。

例如，考虑以下代码：

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // 对于源中的每一行
            line.map(|line| {
                // 如果该行读取成功，则处理它，否则返回错误
                line.split(',') // 按逗号分隔该行
                 .map(|entry| String::from(entry.trim())) // 去除前导和尾随空格
                 .collect() // 将一行中的所有字符串收集到一个 Vec<String> 中
            })
        })
     .collect() // 将所有行收集到一个 Vec<Vec<String>> 中
}
```

`parse_csv_document` 是泛型的，允许它接受任何实现 `BufRead` 的类型，比如 `BufReader<File>` 或 `[u8]`，但 `R` 是什么类型并不重要，并且 `R` 仅用于声明 `src` 的类型，所以该函数也可以写成：

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // 对于源中的每一行
            line.map(|line| {
                // 如果该行读取成功，则处理它，否则返回错误
                line.split(',') // 按逗号分隔该行
                 .map(|entry| String::from(entry.trim())) // 去除前导和尾随空格
                 .collect() // 将一行中的所有字符串收集到一个 Vec<String> 中
            })
        })
     .collect() // 将所有行收集到一个 Vec<Vec<String>> 中
}
```

请注意，使用 `impl Trait` 作为参数类型意味着你不能明确指定使用函数的哪种形式，即 `parse_csv_document::<std::io::Empty>(std::io::empty())` 在第二个示例中无法使用。

## 作为返回类型

如果你的函数返回一个实现 `MyTrait` 的类型，那么可以将其返回类型写成 `-> impl MyTrait`。这可以极大地简化你的类型签名！

```rust
use std::iter;
use std::vec::IntoIter;

// 此函数合并两个 `Vec<i32>` 并返回一个对其进行迭代的迭代器。
// 看看它的返回类型有多复杂！
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// 这是完全相同的函数，但其返回类型使用了 `impl Trait`。
// 看看它有多简单！
fn combine_vecs(
    v: Vec<i32>,
    u: Vec<i32>,
) -> impl Iterator<Item=i32> {
    v.into_iter().chain(u.into_iter()).cycle()
}

fn main() {
    let v1 = vec![1, 2, 3];
    let v2 = vec![4, 5];
    let mut v3 = combine_vecs(v1, v2);
    assert_eq!(Some(1), v3.next());
    assert_eq!(Some(2), v3.next());
    assert_eq!(Some(3), v3.next());
    assert_eq!(Some(4), v3.next());
    assert_eq!(Some(5), v3.next());
    println!("all done");
}
```

更重要的是，有些 Rust 类型无法完整写出。例如，每个闭包都有其自己的未命名具体类型。在 `impl Trait` 语法出现之前，为了返回一个闭包，你必须在堆上进行分配。但现在你可以完全在静态环境中完成，如下所示：

```rust
// 返回一个将输入加上 `y` 的函数
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

你还可以使用 `impl Trait` 来返回使用 `map` 或 `filter` 闭包的迭代器！这使得使用 `map` 和 `filter` 更加容易。因为闭包类型没有名称，如果你的函数返回带有闭包的迭代器，你就无法写出明确的返回类型。但有了 `impl Trait`，你就可以轻松做到这一点：

```rust
fn double_positives<'a>(numbers: &'a Vec<i32>) -> impl Iterator<Item = i32> + 'a {
    numbers
     .iter()
     .filter(|x| x > &&0)
     .map(|x| x * 2)
}

fn main() {
    let singles = vec![-3, -2, 2, 3];
    let doubles = double_positives(&singles);
    assert_eq!(doubles.collect::<Vec<i32>>(), vec![4, 6]);
}
```
