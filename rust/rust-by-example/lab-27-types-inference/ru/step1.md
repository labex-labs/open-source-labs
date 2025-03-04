# Вывод типов

Движок вывода типов довольно умный. Он делает больше, чем просто смотреть на тип выражения значения во время инициализации. Он также смотрит, как переменная используется впоследствии, чтобы вывести ее тип. Вот продвинутый пример вывода типов:

```rust
fn main() {
    // В силу аннотации компилятор знает, что `elem` имеет тип u8.
    let elem = 5u8;

    // Создаем пустой вектор (растяжимый массив).
    let mut vec = Vec::new();
    // На этом этапе компилятор не знает точного типа `vec`, он
    // просто знает, что это вектор чего-то (`Vec<_>`).

    // Вставляем `elem` в вектор.
    vec.push(elem);
    // Ага! Теперь компилятор знает, что `vec` - это вектор `u8` (`Vec<u8>`)
    // TODO ^ Попробуйте закомментировать строку `vec.push(elem)`

    println!("{:?}", vec);
}
```

Не нужно задавать аннотации типов переменным, компилятор доволен, и программист тоже!
