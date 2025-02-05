# 可变引用

我们可以通过一些小调整来修复清单4-6中的代码，使其允许我们修改借用的值，这次我们使用的是可变引用：

文件名：`src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

首先，我们将 `s` 改为可变的。然后，在调用 `change` 函数时，我们使用 `&mut s` 创建一个可变引用，并更新函数签名以接受可变引用 `some_string: &mut String`。这使得 `change` 函数会修改它所借用的值这一点非常明确。

可变引用有一个很大的限制：如果你有一个指向某个值的可变引用，那么你就不能有其他指向该值的引用。这段试图为 `s` 创建两个可变引用的代码将会失败：

文件名：`src/main.rs`

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{r1}, {r2}");
```

这里是错误信息：

```bash
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{r1}, {r2}");
  |                -- first borrow later used here
```

这个错误表明这段代码是无效的，因为我们不能一次对 `s` 进行多次可变借用。第一个可变借用在 `r1` 中，并且必须持续到它在 `println!` 中被使用，但在创建那个可变引用和使用它之间，我们试图在 `r2` 中创建另一个可变引用，它借用了与 `r1` 相同的数据。

防止同时对同一数据进行多个可变引用的限制允许进行可变操作，但方式非常可控。这是新的Rust使用者会遇到困难的地方，因为大多数语言允许你随时进行可变操作。有这个限制的好处是Rust可以在编译时防止数据竞争。数据竞争类似于竞态条件，当出现以下三种行为时就会发生：

- 两个或多个指针同时访问同一数据。
- 至少有一个指针用于写入数据。
- 没有用于同步数据访问的机制。

数据竞争会导致未定义行为，并且在运行时试图追踪它们时可能很难诊断和修复；Rust通过拒绝编译存在数据竞争的代码来防止这个问题！

一如既往，我们可以使用花括号创建一个新的作用域，允许有多个可变引用，但不是同时的：

```rust
let mut s = String::from("hello");

{
    let r1 = &mut s;
} // 这里r1超出了作用域，所以我们可以毫无问题地创建一个新的引用

let r2 = &mut s;
```

Rust对可变引用和不可变引用的组合也实施了类似的规则。这段代码会导致错误：

```rust
let mut s = String::from("hello");

let r1 = &s; // 没问题
let r2 = &s; // 没问题
let r3 = &mut s; // 大问题

println!("{r1}, {r2}, and {r3}");
```

这里是错误信息：

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // no problem
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // no problem
6 |     let r3 = &mut s; // BIG PROBLEM
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{r1}, {r2}, and {r3}");
  |                -- immutable borrow later used here
```

哎呀！当我们对同一值有一个不可变引用时，我们也不能有一个可变引用。

不可变引用的使用者并不期望值会突然在他们不知情的情况下发生变化！然而，允许多个不可变引用，因为只是读取数据的人没有能力影响其他人对数据的读取。

请注意，引用的作用域从它被引入的地方开始，并持续到该引用最后一次被使用。例如，这段代码会编译通过，因为不可变引用的最后一次使用，即 `println!`，发生在可变引用被引入之前：

```rust
let mut s = String::from("hello");

let r1 = &s; // 没问题
let r2 = &s; // 没问题
println!("{r1} and {r2}");
// 变量r1和r2在此之后不会再被使用

let r3 = &mut s; // 没问题
println!("{r3}");
```

不可变引用 `r1` 和 `r2` 的作用域在它们最后一次被使用的 `println!` 之后结束，这是在创建可变引用 `r3` 之前。这些作用域不重叠，所以这段代码是允许的：编译器可以在作用域结束之前的某个点判断出该引用不再被使用。

尽管有时借用错误可能会令人沮丧，但请记住，是Rust编译器在早期（在编译时而非运行时）指出了一个潜在的错误，并准确地告诉你问题出在哪里。这样你就不必去追查为什么你的数据不是你所期望的那样。
