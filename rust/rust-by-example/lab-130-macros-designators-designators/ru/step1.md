# Указатели

Аргументы макроса префиксируются знаком доллара `$` и аннотируются типом с использованием _указателя_:

```rust
macro_rules! create_function {
    // Этот макрос принимает аргумент указателя `ident` и
    // создает функцию с именем `$func_name`.
    // Указатель `ident` используется для имен переменных/функций.
    ($func_name:ident) => {
        fn $func_name() {
            // Макрос `stringify!` преобразует `ident` в строку.
            println!("You called {:?}()",
                     stringify!($func_name));
        }
    };
}

// Создайте функции с именами `foo` и `bar` с помощью вышеуказанного макроса.
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // Этот макрос принимает выражение типа `expr` и выводит
    // его в виде строки вместе с результатом.
    // Указатель `expr` используется для выражений.
    ($expression:expr) => {
        // `stringify!` преобразует выражение *как есть* в строку.
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // Помните, что блоки также являются выражениями!
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

Вот некоторые из доступных указателей:

- `block`
- `expr` используется для выражений
- `ident` используется для имен переменных/функций
- `item`
- `literal` используется для литеральных констант
- `pat` (_шаблон_)
- `path`
- `stmt` (_оператор_)
- `tt` (_дерево токенов_)
- `ty` (_тип_)
- `vis` (_квалификатор видимости_)

Для полного списка см. \[Rust Reference\].
