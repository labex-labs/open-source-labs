# Creating Idiomatic use Paths

В Listing 7-11 вы, возможно, спросили себя, почему мы указали `use crate::front_of_house::hosting`, а затем вызвали `hosting::add_to_waitlist` в `eat_at_restaurant`, вместо того, чтобы указать путь `use` до самой функции `add_to_waitlist`, чтобы достичь того же результата, как в Listing 7-13.

Filename: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

Listing 7-13: Bringing the `add_to_waitlist` function into scope with `use`, which is unidiomatic

Хотя и в Listing 7-11, и в Listing 7-13 выполняется одна и та же задача, Listing 7-11 представляет собой идиоматический способ подключить функцию с помощью `use`. Подключение родительского модуля функции с помощью `use` означает, что мы должны указывать родительский модуль при вызове функции. Указание родительского модуля при вызове функции делает ясно, что функция не определена локально, при этом минимизируя повторение полного пути. Код в Listing 7-13 неясен, где определена `add_to_waitlist`.

С другой стороны, при подключении структур, перечислений и других элементов с помощью `use`, идиоматично указывать полный путь. Listing 7-14 показывает идиоматический способ подключить структуру `HashMap` из стандартной библиотеки в скоуп бинарного пакета.

Filename: `src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

Listing 7-14: Bringing `HashMap` into scope in an idiomatic way

За этой идиомой нет особой причины: это просто договорённость, которая сформировалась, и люди привыкли читать и писать код на Rust именно так.

Исключение от этой идиомы возникает, если мы подключаем два элемента с одинаковым именем с помощью `use`-статементов, потому что Rust не позволяет этого. Listing 7-15 показывает, как подключить два типа `Result`, которые имеют одинаковое имя, но разные родительские модули, и как ссылаться на них.

Filename: `src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

Listing 7-15: Bringing two types with the same name into the same scope requires using their parent modules.

Как вы можете видеть, использование родительских модулей позволяет различать два типа `Result`. Если бы мы вместо этого указали `use std::fmt::Result` и `use std::io::Result`, то в одном скоупе мы бы имели два типа `Result`, и Rust не знал, какой именно мы имеем в виду, когда используем `Result`.
