# `impl Trait`

`impl Trait` может использоваться в двух местах:

1.  в качестве типа аргумента
2.  в качестве возвращаемого типа

## В качестве типа аргумента

Если ваша функция является обобщенной по трейту, но вы не заботитесь о конкретном типе, вы можете упростить объявление функции, используя `impl Trait` в качестве типа аргумента.

Например, рассмотрите следующий код:

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Для каждой строки в источнике
            line.map(|line| {
                // Если строка была прочитана успешно, обработайте ее, если нет, верните ошибку
                line.split(',') // Разделите строку, разделенную запятыми
                 .map(|entry| String::from(entry.trim())) // Удалите начальные и конечные пробелы
                 .collect() // Соберите все строки в ряду в Vec<String>
            })
        })
     .collect() // Соберите все строки в Vec<Vec<String>>
}
```

`parse_csv_document` является обобщенной функцией, которая может принимать любой тип, реализующий `BufRead`, например, `BufReader<File>` или `[u8]`, но не имеет значения, какой тип `R`, и `R` используется только для объявления типа `src`, поэтому функцию можно также записать так:

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Для каждой строки в источнике
            line.map(|line| {
                // Если строка была прочитана успешно, обработайте ее, если нет, верните ошибку
                line.split(',') // Разделите строку, разделенную запятыми
                 .map(|entry| String::from(entry.trim())) // Удалите начальные и конечные пробелы
                 .collect() // Соберите все строки в ряду в Vec<String>
            })
        })
     .collect() // Соберите все строки в Vec<Vec<String>>
}
```

Обратите внимание, что использование `impl Trait` в качестве типа аргумента означает, что вы не можете явно указать, какой вариант функции вы используете, то есть `parse_csv_document::<std::io::Empty>(std::io::empty())` не будет работать со вторым примером.

## В качестве возвращаемого типа

Если ваша функция возвращает тип, реализующий `MyTrait`, вы можете записать его возвращаемым типом как `-> impl MyTrait`. Это может значительно упростить ваши сигнатуры типов!

```rust
use std::iter;
use std::vec::IntoIter;

// Эта функция объединяет два `Vec<i32>` и возвращает итератор по ним.
// Посмотрите, насколько сложен ее возвращаемый тип!
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// Это та же функция, но ее возвращаемый тип использует `impl Trait`.
// Посмотрите, насколько проще это!
fn combine_vecs(
    v: Vec<i32>,
    u: Vec<i32>,
) -> impl Iterator<Item=i32> {
    v.into_iter().chain(u.into_iter()).cycle()
}

fn main() {
    let v1 = vec![1, 2, 3];
    let v2 = vec![4, 5];
    let mut v3 = combine_vecs(v1, v2);
    assert_eq!(Some(1), v3.next());
    assert_eq!(Some(2), v3.next());
    assert_eq!(Some(3), v3.next());
    assert_eq!(Some(4), v3.next());
    assert_eq!(Some(5), v3.next());
    println!("all done");
}
```

Важнее всего, некоторые типы Rust нельзя записать явно. Например, каждый замыкание имеет свой собственный неименованный конкретный тип. До появления синтаксиса `impl Trait` вам приходилось выделять память на куче, чтобы вернуть замыкание. Но теперь вы можете сделать это статически, вот так:

```rust
// Возвращает функцию, которая добавляет `y` к своему входу
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

Вы также можете использовать `impl Trait`, чтобы вернуть итератор, который использует замыкания `map` или `filter`! Это делает использование `map` и `filter` проще. Поскольку типы замыканий не имеют имен, вы не можете записать явный возвращаемый тип, если ваша функция возвращает итераторы с замыканиями. Но с `impl Trait` вы можете сделать это легко:

```rust
fn double_positives<'a>(numbers: &'a Vec<i32>) -> impl Iterator<Item = i32> + 'a {
    numbers
     .iter()
     .filter(|x| x > &&0)
     .map(|x| x * 2)
}

fn main() {
    let singles = vec![-3, -2, 2, 3];
    let doubles = double_positives(&singles);
    assert_eq!(doubles.collect::<Vec<i32>>(), vec![4, 6]);
}
```
