# Ранние возвраты

В предыдущем примере мы явно обрабатывали ошибки с использованием комбинаторов. Другой способ обработки этого анализа случаев - это использование комбинации операторов `match` и _ранних возвратов_.

То есть, мы можем просто прекратить выполнение функции и вернуть ошибку, если она возникает. Для некоторых этот вид кода может быть проще как для чтения, так и для написания. Рассмотрим этот вариант предыдущего примера, переписанный с использованием ранних возвратов:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

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

На этом этапе мы научились явно обрабатывать ошибки с использованием комбинаторов и ранних возвратов. Хотя в целом мы хотим избегать паники, явная обработка всех наших ошибок является утомительным.

В следующем разделе мы представим `?` для случаев, когда нам просто нужно `unwrap` без возможности вызвать `panic`.
