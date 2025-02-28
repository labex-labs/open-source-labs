# Тип, который никогда не возвращает

В Rust есть специальный тип под названием `!`, который в терминах теории типов известен как _пустой тип_, потому что у него нет значений. Мы предпочитаем называть его _типом никогда_, потому что он занимает место возвращаемого типа, когда функция никогда не возвращает. Вот пример:

```rust
fn bar() ->! {
    --snip--
}
```

Этот код читается как "функция `bar` возвращает никогда". Функции, которые возвращают никогда, называются _дивергирующими функциями_. Мы не можем создавать значения типа `!`, поэтому `bar` никогда не может вернуть значение.

Но для чего нужен тип, для которого вы никогда не можете создать значения? Назовем код из Листинга 2-5, который является частью игры в угадывание числа; мы здесь воспроизводим его немного в Листинге 19-26.

```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```

Листинг 19-26: `match` с веткой, которая заканчивается на `continue`

Тогда мы пропустили некоторые детали в этом коде. В разделе "Конструкция управления `match`" мы обсуждали, что ветки `match` должны все возвращать один и тот же тип. Поэтому, например, следующий код не работает:

```rust
let guess = match guess.trim().parse() {
    Ok(_) => 5,
    Err(_) => "hello",
};
```

Тип `guess` в этом коде должен быть целым числом _и_ строкой, а Rust требует, чтобы `guess` имел только один тип. Так что чем возвращает `continue`? Как мы могли вернуть `u32` из одной ветки и иметь другую ветку, которая заканчивается на `continue` в Листинге 19-26?

Как вы, вероятно, догадались, `continue` имеет значение `!`. То есть, когда Rust вычисляет тип `guess`, он смотрит на обе ветки `match`, одну с значением `u32`, а другую с значением `!`. Поскольку `!` никогда не может иметь значение, Rust решает, что тип `guess` - это `u32`.

Формальный способ описания этого поведения заключается в том, что выражения типа `!` могут быть приведены к любому другому типу. Мы можем завершить эту ветку `match` на `continue`, потому что `continue` не возвращает значение; вместо этого он возвращает управление в начало цикла, поэтому в случае `Err` мы никогда не присваиваем значение `guess`.

Тип никогда также полезен с макросом `panic!`. Назовем функцию `unwrap`, которую мы вызываем для значений `Option<T>`, чтобы получить значение или вызвать панику с этой определением:

```rust
impl<T> Option<T> {
    pub fn unwrap(self) -> T {
        match self {
            Some(val) => val,
            None => panic!(
                "called `Option::unwrap()` on a `None` value"
            ),
        }
    }
}
```

В этом коде то же самое происходит, что и в `match` из Листинга 19-26: Rust видит, что `val` имеет тип `T`, а `panic!` имеет тип `!`, поэтому результат всего выражения `match` - это `T`. Этот код работает, потому что `panic!` не возвращает значение; он завершает программу. В случае `None` мы не вернем значение из `unwrap`, поэтому этот код действителен.

Еще одно выражение, которое имеет тип `!`, - это `loop`:

    print!("forever ");

    loop {
        print!("and ever ");
    }

Здесь цикл никогда не заканчивается, поэтому `!` - это значение выражения. Однако, это не было бы так, если бы мы включили `break`, потому что цикл завершился бы, когда дошел до `break`.
