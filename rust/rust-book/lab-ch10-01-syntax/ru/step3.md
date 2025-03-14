# В определениях функций

При определении функции, которая использует обобщения, мы помещаем обобщения в сигнатуру функции, где обычно указываем типы данных параметров и возвращаемого значения. Это делает наш код более гибким и предоставляет больше функциональности для вызывающих функцию кодов, при этом предотвращая дублирование кода.

Продолжая с нашей функцией `largest`, в Listing 10-4 показаны две функции, которые ищут наибольшее значение в срезе. Затем мы объединим их в одну функцию, которая использует обобщения.

Filename: `src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

Listing 10-4: Две функции, которые отличаются только именами и типами в их сигнатурах

Функция `largest_i32` — это та, которую мы извлекли в Listing 10-3, которая находит наибольшее `i32` в срезе. Функция `largest_char` находит наибольший `char` в срезе. Тела функций имеют одинаковый код, поэтому давайте избавимся от дублирования, введя обобщенный параметр типа в одной функции.

Чтобы параметризовать типы в новой единственной функции, нам нужно назвать параметр типа, так же, как мы это делаем для параметров значений функции. Вы можете использовать любой идентификатор в качестве имени параметра типа. Но мы будем использовать `T`, потому что по соглашению имена параметров типа в Rust короткие, часто состоят из одной буквы, и соглашение о именовании типов в Rust — это CamelCase. Короткая форма от _type_ (тип), `T` — это стандартный выбор большинства программистов на Rust.

Когда мы используем параметр в теле функции, мы должны объявить имя параметра в сигнатуре, чтобы компилятор знал, что означает это имя. Аналогично, когда мы используем имя параметра типа в сигнатуре функции, мы должны объявить имя параметра типа перед тем, как использовать его. Чтобы определить обобщенную функцию `largest`, мы помещаем объявления имен типов внутри угловых скобок, `< >`, между именем функции и списком параметров, вот так:

```rust
fn largest<T>(list: &[T]) -> &T {
```

Мы читаем это определение так: функция `largest` является обобщенной по какому-то типу `T`. Эта функция имеет один параметр с именем `list`, который является срезами значений типа `T`. Функция `largest` вернёт ссылку на значение того же типа `T`.

Listing 10-5 показывает объединённое определение функции `largest`, которое использует обобщённый тип данных в своей сигнатуре. В списке также показано, как мы можем вызвать функцию с помощью среза значений `i32` или `char`. Обратите внимание, что этот код ещё не скомпилируется, но мы исправим это позже в этом разделе.

Filename: `src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

Listing 10-5: Функция `largest`, использующая обобщенные параметры типа; этот код ещё не скомпилируется

Если мы сейчас скомпилируем этот код, мы получим эту ошибку:

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

Текст помощи упоминает `std::cmp::PartialOrd`, который является _трейтом_ (особенностью), и мы поговорим о трейтах в следующем разделе. На данный момент просто запомните, что эта ошибка означает, что тело `largest` не будет работать для всех возможных типов, которые может быть `T`. Поскольку мы хотим сравнивать значения типа `T` в теле, мы можем использовать только типы, значения которых можно упорядочить. Чтобы включить сравнения, в стандартной библиотеке есть трейт `std::cmp::PartialOrd`, который можно реализовать для типов (см. Приложение С для более подробной информации о этом трейте). Следуя подсказке текста помощи, мы ограничиваем типы, допустимые для `T`, только теми, которые реализуют `PartialOrd`, и этот пример скомпилируется, потому что стандартная библиотека реализует `PartialOrd` как для `i32`, так и для `char`.
