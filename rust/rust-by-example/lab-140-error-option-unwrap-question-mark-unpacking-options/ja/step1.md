# `?` を使った `Option` の展開

`match` 文を使って `Option` を展開することができますが、`?` 演算子を使う方が多くの場合簡単です。`x` が `Option` である場合、`x?` を評価すると、`x` が `Some` の場合にはその値を返し、そうでない場合には実行中の関数を終了して `None` を返します。

```rust
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // `current_age` が `None` の場合、これは `None` を返します。
    // `current_age` が `Some` の場合、内側の `u8` が `next_age` に代入されます
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

コードの読みやすさを大幅に向上させるために、複数の `?` を連鎖させることができます。

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

    // 存在する場合、その人の仕事の電話番号の地域コードを取得します。
    fn work_phone_area_code(&self) -> Option<u8> {
        // `?` 演算子がない場合、これには多数のネストした `match` 文が必要になります。
        // もっと多くのコードが必要になります - 自分で書いてみて、どちらが簡単かを比較してみてください。
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
