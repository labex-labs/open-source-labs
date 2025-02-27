# Использование супертрейтов

Иногда вы можете написать определение трейта, которое зависит от другого трейта: чтобы тип реализовал первый трейт, вы хотите требовать, чтобы этот тип также реализовывал второй трейт. Вы бы сделали это, чтобы определение вашего трейта могло использовать связанные элементы второго трейта. Трейт, на который ваше определение трейта полагается, называется _супертрейтом_ вашего трейта.

Например, допустим, мы хотим создать трейт `OutlinePrint` с методом `outline_print`, который будет выводить заданное значение в отформатированном виде, так чтобы оно было обрамлено звездочками. То есть, если у нас есть структура `Point`, которая реализует трейт `Display` стандартной библиотеки и выводит `(x, y)`, когда мы вызываем `outline_print` для экземпляра `Point`, у которого `x` равен `1`, а `y` равен `3`, должно быть выведено следующее:

    **********
    *        *
    * (1, 3) *
    *        *
    **********

В реализации метода `outline_print` мы хотим использовать функциональность трейта `Display`. Поэтому мы должны указать, что трейт `OutlinePrint` будет работать только для типов, которые также реализуют `Display` и предоставляют функциональность, необходимую для `OutlinePrint`. Мы можем сделать это в определении трейта, указав `OutlinePrint: Display`. Эта техника похожа на добавление ограничения трейта к трейту. Listing 19-22 показывает реализацию трейта `OutlinePrint`.

Filename: `src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

Listing 19-22: Реализация трейта `OutlinePrint`, который требует функциональности из `Display`

Поскольку мы указали, что `OutlinePrint` требует трейта `Display`, мы можем использовать функцию `to_string`, которая автоматически реализуется для любого типа, реализующего `Display`. Если бы мы попытались использовать `to_string` без добавления двоеточия и указания трейта `Display` после имени трейта, мы получили бы ошибку, говорящую, что метод с именем `to_string` не найден для типа `&Self` в текущем скоупе.

Посмотрим, что произойдет, если мы попытаемся реализовать `OutlinePrint` для типа, который не реализует `Display`, например, для структуры `Point`:

Filename: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

Мы получаем ошибку, говорящую, что требуется `Display`, но он не реализован:

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

Чтобы исправить это, мы реализуем `Display` для `Point` и удовлетворяем ограничение, требуемое `OutlinePrint`, вот так:

Filename: `src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

Затем реализация трейта `OutlinePrint` для `Point` будет успешно скомпилирована, и мы сможем вызвать `outline_print` для экземпляра `Point`, чтобы вывести его в виде обрамленного звездочками.
