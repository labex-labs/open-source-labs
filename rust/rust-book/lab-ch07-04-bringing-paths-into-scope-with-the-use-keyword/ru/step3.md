# Providing New Names with the as Keyword

Есть еще одно решение проблемы подключения двух типов с одинаковым именем в один и тот же скоуп с помощью `use`: после пути мы можем указать `as` и новое локальное имя, или _алиас_, для типа. Listing 7-16 показывает другой способ написать код из Listing 7-15, перейменовав один из двух типов `Result` с использованием `as`.

Filename: `src/lib.rs`

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    --snip--
}

fn function2() -> IoResult<()> {
    --snip--
}
```

Listing 7-16: Renaming a type when it's brought into scope with the `as` keyword

Во втором `use`-статменте мы выбрали новое имя `IoResult` для типа `std::io::Result`, которое не будет конфликтовать с `Result` из `std::fmt`, который мы также подключили в скоуп. Listing 7-15 и Listing 7-16 считаются идиоматическими, поэтому решение остается за вами!
