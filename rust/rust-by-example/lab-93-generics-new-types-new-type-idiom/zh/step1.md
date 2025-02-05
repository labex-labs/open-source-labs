# 新类型习惯用法

新类型习惯用法在编译时提供保证，确保向程序提供正确类型的值。

例如，一个检查年龄（以年为单位）的年龄验证函数，必须被赋予一个 `Years` 类型的值。

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// 截断部分年份
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

取消最后一条打印语句的注释，以观察必须提供的类型为 `Years`。

要将新类型的值作为基础类型获取，可以使用元组或解构语法，如下所示：

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // 元组
    let Years(years_as_primitive_2) = years; // 解构
}
```
