# Выражения

Программа на Rust (большинство) состоит из серии инструкций:

```rust
fn main() {
    // инструкция
    // инструкция
    // инструкция
}
```

В Rust есть несколько видов инструкций. Два самых распространенных - это объявление связывания переменной и использование `;` с выражением:

```rust
fn main() {
    // связывание переменной
    let x = 5;

    // выражение;
    x;
    x + 1;
    15;
}
```

Блоки также являются выражениями, поэтому их можно использовать в качестве значений при присвоении. Последнее выражение в блоке будет присвоено месту выражения, такому как локальной переменной. Однако, если последнее выражение блока заканчивается точкой с запятой, возвращаемое значение будет `()`.

```rust
fn main() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // Это выражение будет присвоено `y`
        x_cube + x_squared + x
    };

    let z = {
        // Точка с запятой подавляет это выражение и `()` присваивается `z`
        2 * x;
    };

    println!("x is {:?}", x);
    println!("y is {:?}", y);
    println!("z is {:?}", z);
}
```
