# `panic`

Самым простым механизмом обработки ошибок, с которым мы познакомимся, является `panic`. Он выводит сообщение об ошибке, начинает разматывать стек и обычно завершает программу. Здесь мы явно вызываем `panic` при возникновении ошибки:

```rust
fn drink(beverage: &str) {
    // You shouldn't drink too much sugary beverages.
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```
