# `panic!`

Макрос `panic!` можно использовать для генерации паники и начала разматывания стека. Во время разматывания время выполнения освободит все ресурсы, **принадлежащие** потоку, вызвав деструктор всех его объектов.

Поскольку мы работаем с программами, содержащими только один поток, `panic!` заставит программу вывести сообщение о панике и завершиться.

```rust
// Переосуществление деления целых чисел (/)
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // Деление на ноль вызывает панику
        panic!("деление на ноль");
    } else {
        dividend / divisor
    }
}

// Задача `main`
fn main() {
    // Целое число, выделенное в куче
    let _x = Box::new(0i32);

    // Эта операция вызовет неудачу задачи
    division(3, 0);

    println!("Эта точка не будет достигнута!");

    // `_x` должно быть уничтожено в этом месте
}
```

Проверим, что `panic!` не утекает память.

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc panic.rs && valgrind./panic
==4401== Memcheck, a memory error detector
==4401== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==4401== Using Valgrind-3.10.0.SVN and LibVEX; rerun with -h for copyright info
==4401== Command:./panic
==4401==
thread '<main>' panicked at 'деление на ноль', panic.rs:5
==4401==
==4401== HEAP SUMMARY:
==4401==     in use at exit: 0 bytes in 0 blocks
==4401==   total heap usage: 18 allocs, 18 frees, 1,648 bytes allocated
==4401==
==4401== All heap blocks were freed -- no leaks are possible
==4401==
==4401== For counts of detected and suppressed errors, rerun with: -v
==4401== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```
