# while

Ключевое слово `while` можно использовать для запуска цикла, пока условие истинно.

Напишем знаменитую FizzBuzz с использованием цикла `while`.

```rust
fn main() {
    // Переменная-счетчик
    let mut n = 1;

    // Цикл, пока `n` меньше 101
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }

        // Увеличиваем счетчик
        n += 1;
    }
}
```
