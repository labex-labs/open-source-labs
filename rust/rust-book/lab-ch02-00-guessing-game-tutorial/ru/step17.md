# Обработка некорректного ввода

Для дальнейшего усовершенствования поведения игры, вместо того чтобы программа падала при вводе пользователем нечислового значения, давайте сделаем так, чтобы игра игнорировала нечисловой ввод, чтобы пользователь мог продолжать угадывать. Мы можем это сделать, изменив строку, где `guess` преобразуется из `String` в `u32`, как показано в Листинге 2-5.

Имя файла: `src/main.rs`

```rust
--snip--

io::stdin()
 .read_line(&mut guess)
 .expect("Failed to read line");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("You guessed: {guess}");

--snip--
```

Листинг 2-5: Игнорирование нечисловой попытки угадать и запрос нового ввода вместо аварийного завершения программы

Мы переходим от вызова `expect` к выражению `match`, чтобы перейти от аварийного завершения при ошибке к обработке ошибки. Помните, что `parse` возвращает тип `Result`, а `Result` - это перечисление, которое имеет варианты `Ok` и `Err`. Мы используем выражение `match` здесь, как и с результатом `Ordering` метода `cmp`.

Если `parse` успешно преобразует строку в число, он вернет значение `Ok`, которое содержит полученное число. Это значение `Ok` соответствует шаблону первой ветви, и выражение `match` просто вернет значение `num`, которое `parse` сгенерировал и поместил в значение `Ok`. Это число окажется в том месте, где мы хотим его в новой переменной `guess`, которую мы создаем.

Если `parse` _не_ может преобразовать строку в число, он вернет значение `Err`, которое содержит дополнительную информацию об ошибке. Значение `Err` не соответствует шаблону `Ok(num)` в первой ветви `match`, но оно соответствует шаблону `Err(_)` во второй ветви. Нижнее подчеркивание, `_`, - это значение, которое ловит все; в этом примере мы говорим, что хотим соответствовать всем значениям `Err`, независимо от информации внутри них. Таким образом, программа выполнит код второй ветви, `continue`, который говорит программе перейти к следующей итерации `loop` и запросить новую попытку. Таким образом, по существу, программа игнорирует все ошибки, которые может встретить `parse`!

Теперь все в программе должно работать, как ожидается. Давайте попробуем:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

Отлично! С одной маленькой последней доработкой мы завершим игру-угадайку. Напомним, что программа по-прежнему выводит секретное число. Это хорошо работало для тестирования, но оно портит игру. Давайте удалим `println!`, который выводит секретное число. Листинг 2-6 показывает окончательный код.

Имя файла: `src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```

Листинг 2-6: Полный код игры-угадайки

На этом этапе вы успешно создали игру-угадайку. Поздравляем!
