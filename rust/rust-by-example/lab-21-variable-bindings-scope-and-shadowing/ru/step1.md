# Область видимости и скрытие

Связывания переменных имеют область видимости и ограничиваются жизнью в _блоке_. Блок - это коллекция инструкций, заключенных в фигурные скобки `{}`.

```rust
fn main() {
    // Это связывание существует в функции main
    let long_lived_binding = 1;

    // Это блок, и его область видимости меньше, чем область видимости функции main
    {
        // Это связывание существует только в этом блоке
        let short_lived_binding = 2;

        println!("внутри short: {}", short_lived_binding);
    }
    // Конец блока

    // Ошибка! `short_lived_binding` не существует в этой области видимости
    println!("внешний short: {}", short_lived_binding);
    // FIXME ^ Закомментируйте эту строку

    println!("внешний long: {}", long_lived_binding);
}
```

Также допускается скрытие переменной.

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("до скрытия: {}", shadowed_binding);

        // Это связывание *скрывает* внешнее
        let shadowed_binding = "abc";

        println!("скрыто в внутреннем блоке: {}", shadowed_binding);
    }
    println!("за пределами внутреннего блока: {}", shadowed_binding);

    // Это связывание *скрывает* предыдущее связывание
    let shadowed_binding = 2;
    println!("скрыто в внешнем блоке: {}", shadowed_binding);
}
```
