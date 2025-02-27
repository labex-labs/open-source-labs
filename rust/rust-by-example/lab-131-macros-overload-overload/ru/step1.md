# Перегрузка

Макросы можно перегружать, чтобы они могли принимать разные комбинации аргументов. В этом отношении `macro_rules!` может работать аналогично блоку `match`:

```rust
// `test!` будет сравнивать `$left` и `$right`
// по-разному, в зависимости от того, как вы его вызываете:
macro_rules! test {
    // Аргументы не обязательно должны быть разделены запятой.
    // Можно использовать любую шаблонную конструкцию!
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ каждый вариант (`arm`) должен заканчиваться точкой с запятой.
    ($left:expr; or $right:expr) => {
        println!("{:?} or {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left || $right)
    };
}

fn main() {
    test!(1i32 + 1 == 2i32; and 2i32 * 2 == 4i32);
    test!(true; or false);
}
```
