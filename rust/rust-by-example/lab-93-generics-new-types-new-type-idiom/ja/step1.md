# 新しい型のイディオム

`newtype` イディオムは、適切な型の値がプログラムに供給されることをコンパイル時に保証します。

たとえば、年齢をチェックする年齢検証関数には、`Years` 型の値が _必ず_ 与えられなければなりません。

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// 小数部分の年を切り捨てます
    pub fn to_years(&self) -> Years {
        Years(self.0 / 365)
    }
}

fn old_enough(age: &Years) -> bool {
    age.0 >= 18
}

fn main() {
    let age = Years(5);
    let age_days = age.to_days();
    println!("Old enough {}", old_enough(&age));
    println!("Old enough {}", old_enough(&age_days.to_years()));
    // println!("Old enough {}", old_enough(&age_days));
}
```

最後の print 文のコメントを解除して、与えられる型が `Years` でなければならないことを確認してください。

`newtype` の値を基本型として取得するには、次のようにタプルまたは分解構文を使用できます。

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // タプル
    let Years(years_as_primitive_2) = years; // 分解
}
```
