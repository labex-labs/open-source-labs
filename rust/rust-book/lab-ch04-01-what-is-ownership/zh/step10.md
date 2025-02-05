# 返回值与作用域

返回值也可以转移所有权。清单 4-4 展示了一个返回某个值的函数示例，带有与清单 4-3 中类似的注释。

    // src/main.rs
    fn main() {
        let s1 = gives_ownership();         // gives_ownership 将其返回值
                                            // 移动到 s1 中

        let s2 = String::from("hello");     // s2 进入作用域

        let s3 = takes_and_gives_back(s2);  // s2 被移动到
                                            // takes_and_gives_back 中，该函数
                                            // 也将其返回值移动到 s3 中
    } // 在这里，s3 离开作用域并被释放。s2 已被移动，所以
      // 什么也不会发生。s1 离开作用域并被释放

    fn gives_ownership() -> String {             // gives_ownership 会将其
                                                 // 返回值移动到调用它的函数中

        let some_string = String::from("yours"); // some_string 进入作用域

        some_string                              // some_string 被返回并
                                                 // 移动到调用函数中
    }

    // 此函数接受一个 String 并返回一个 String
    fn takes_and_gives_back(a_string: String) -> String { // a_string 进入
                                                          // 作用域

        a_string  // a_string 被返回并移动到调用函数中
    }

清单 4-4：返回值的所有权转移

变量的所有权每次都遵循相同的模式：将一个值赋给另一个变量会移动它。当一个包含堆上数据的变量超出作用域时，除非数据的所有权已被移动到另一个变量，否则该值将由 `drop` 清理。

虽然这样可行，但每个函数都获取所有权然后再返回所有权有点繁琐。如果我们想让一个函数使用一个值但不获取所有权呢？如果我们想再次使用传入的任何值，除了可能想要返回的函数体产生的任何数据之外，还需要将其再次传递回去，这相当麻烦。

Rust 确实允许我们使用元组返回多个值，如清单 4-5 所示。

文件名：`src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{s2}' is {len}.");
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() 返回一个 String 的长度

    (s, length)
}
```

清单 4-5：返回参数的所有权

但对于一个应该很常见的概念来说，这太繁琐且工作量太大了。幸运的是，Rust 有一个用于在不转移所有权的情况下使用值的特性，称为 **引用**。
