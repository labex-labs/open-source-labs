# Alternatives to Using match with Result\<T, E\>

Это много `match`! Выражение `match` очень полезно, но также является довольно примитивным. В главе 13 вы узнаете о замыканиях, которые используются с многими методами, определенными для `Result<T, E>`. Эти методы могут быть более компактными, чем использование `match`, при обработке значений `Result<T, E>` в вашем коде.

Например, вот другой способ написать ту же логику, как показано в листинге 9-5, на этот раз используя замыкания и метод `unwrap_or_else`:

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

Хотя этот код имеет то же поведение, что и листинг 9-5, он не содержит никаких выражений `match` и проще читать. Вернитесь к этому примеру после прочтения главы 13 и изучите метод `unwrap_or_else` в документации по стандартной библиотеке. Многие другие методы могут упростить огромные вложенные выражения `match`, когда вы работаете с ошибками.
