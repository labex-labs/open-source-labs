# 使用 `?` 解包 `Option`

你可以使用 `match` 语句来解包 `Option`，但使用 `?` 运算符通常更容易。如果 `x` 是一个 `Option`，那么计算 `x?` 时，如果 `x` 是 `Some`，它将返回其底层值，否则它将终止正在执行的任何函数并返回 `None`。

```rust
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // 如果 `current_age` 是 `None`，则返回 `None`。
    // 如果 `current_age` 是 `Some`，则内部的 `u8` 会被赋给 `next_age`
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

你可以将多个 `?` 链接在一起，使你的代码更具可读性。

```rust
struct Person {
    job: Option<Job>,
}

#[derive(Clone, Copy)]
struct Job {
    phone_number: Option<PhoneNumber>,
}

#[derive(Clone, Copy)]
struct PhoneNumber {
    area_code: Option<u8>,
    number: u32,
}

impl Person {

    // 获取此人工作电话的区号（如果存在）。
    fn work_phone_area_code(&self) -> Option<u8> {
        // 如果没有 `?` 运算符，这将需要许多嵌套的 `match` 语句。
        // 这将需要更多代码 - 你可以自己尝试编写一下，看看哪种更简单。
        self.job?.phone_number?.area_code
    }
}

fn main() {
    let p = Person {
        job: Some(Job {
            phone_number: Some(PhoneNumber {
                area_code: Some(61),
                number: 439222222,
            }),
        }),
    };

    assert_eq!(p.work_phone_area_code(), Some(61));
}
```
