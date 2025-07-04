# Использование Box`<T>` как ссылки

Мы можем переписать код из Listing 15-6, чтобы использовать `Box<T>` вместо ссылки; оператор дереференцирования, применяемый к `Box<T>` в Listing 15-7, работает так же, как и оператор дереференцирования, применяемый к ссылке в Listing 15-6.

Filename: `src/main.rs`

```rust
fn main() {
    let x = 5;
  1 let y = Box::new(x);

    assert_eq!(5, x);
  2 assert_eq!(5, *y);
}
```

Listing 15-7: Использование оператора дереференцирования для Box`<i32>`

Основное отличие между Listing 15-7 и Listing 15-6 заключается в том, что здесь мы задаем `y` как экземпляр коробки, указывающий на скопированное значение `x`, а не ссылку, указывающую на значение `x` \[1\]. В последнем утверждении \[2\] мы можем использовать оператор дереференцирования, чтобы следовать за указателем коробки так же, как это делалось, когда `y` была ссылкой. Далее мы рассмотрим, что особенного в `Box<T>`, которое позволяет нам использовать оператор дереференцирования, определив собственный тип коробки.
