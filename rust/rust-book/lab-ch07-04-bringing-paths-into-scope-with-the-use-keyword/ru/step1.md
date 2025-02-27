# Bringing Paths into Scope with the use Keyword

Надоело каждый раз писать полный путь для вызова функций, это кажется неудобным и повторяющимся. В Listing 7-7, независимо от того, выбирали мы абсолютный или относительный путь к функции `add_to_waitlist`, каждый раз, когда хотели вызвать `add_to_waitlist`, нам также приходилось указывать `front_of_house` и `hosting`. К счастью, есть способ упростить этот процесс: мы можем создать ярлык для пути с помощью ключевого слова `use` один раз, а затем использовать корочее имя везде в этом скоупе.

В Listing 7-11 мы подключаем модуль `crate::front_of_house::hosting` в скоуп функции `eat_at_restaurant`, чтобы нам пришлось указывать только `hosting::add_to_waitlist`, чтобы вызвать функцию `add_to_waitlist` в `eat_at_restaurant`.

Filename: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listing 7-11: Bringing a module into scope with `use`

Добавление `use` и пути в скоуп похоже на создание символической ссылки в файловой системе. Добавив `use crate::front_of_house::hosting` в корне пакета, `hosting` теперь является допустимым именем в этом скоупе, точно так же, будто бы модуль `hosting` был определен в корне пакета. Путей, подключаемых с помощью `use`, также проверяется приватность, как и любые другие пути.

Обратите внимание, что `use` создает ярлык только для конкретного скоупа, в котором оно встречается. Listing 7-12 перемещает функцию `eat_at_restaurant` в новый дочерний модуль под названием `customer`, который представляет собой другой скоуп, чем `use`-statement, поэтому тело функции не скомпилируется.

Filename: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

Listing 7-12: A `use` statement only applies in the scope it's in.

Сообщение об ошибке компилятора показывает, что ярлык больше не действует внутри модуля `customer`:

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

Заметим, что также есть предупреждение, что `use` больше не используется в своем скоупе! Чтобы исправить эту проблему, перенесите `use` внутри модуля `customer` также, или ссылаться на ярлык в родительском модуле с помощью `super::hosting` внутри дочернего модуля `customer`.
