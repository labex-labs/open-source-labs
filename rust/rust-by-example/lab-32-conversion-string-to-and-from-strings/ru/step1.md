# Преобразование в строку и обратно

## Преобразование в строку

Преобразование любого типа в `String` настолько просто, насколько и реализация трейта \[`ToString`\] для этого типа. Вместо прямого выполнения этого вы должны реализовать трейт `fmt::Display`, который автоматически предоставляет \[`ToString`\] и также позволяет выводить тип, как обсуждалось в разделе о `print!`.

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## Парсинг строки

Одним из более распространенных типов является преобразование строки в число. Идиоматический подход к этому - использовать функцию \[`parse`\] и либо обеспечить тип-инференс, либо указать тип для парсинга с использованием синтаксиса "turbofish". Оба варианта показаны в следующем примере.

Это преобразует строку в указанный тип, при условии, что для этого типа реализован трейт \[`FromStr`\]. Это реализовано для многочисленных типов в стандартной библиотеке. Чтобы получить эту функциональность для пользовательского типа, просто реализуйте для него трейт \[`FromStr`\].

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("Sum: {:?}", sum);
}
```
