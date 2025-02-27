# Введение в оператор `?`

Иногда нам просто нужна простота метода `unwrap`, но без возможности аварийного завершения программы (`panic`). До сих пор `unwrap` заставлял нас вкладываться все глубже и глубже, когда на самом деле мы хотели получить переменную и выйти из функции. Именно для этого и существует оператор `?`.

При обнаружении `Err` есть два допустимых действия:

1.  `panic!`, которое мы уже решили尽量避免, если это возможно
2.  `return`, потому что `Err` означает, что ошибка не может быть обработана

Оператор `?` _почти_[\^†\] эквивалентен методу `unwrap`, который `return`ит вместо того, чтобы вызывать `panic` при возникновении `Err`. Посмотрим, как мы можем упростить предыдущий пример, использующий комбинаторы:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```

## Макрос `try!`

До появления оператора `?` ту же функциональность можно было реализовать с помощью макроса `try!`. Теперь рекомендуется использовать оператор `?`, но вы по-прежнему можете встретить `try!` в старом коде. То же самое функция `multiply` из предыдущего примера, написанная с использованием `try!`, будет выглядеть так:

```rust
// Чтобы скомпилировать и запустить этот пример без ошибок при использовании Cargo, измените значение
// поля `edition` в разделе `[package]` файла `Cargo.toml` на "2015".

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
