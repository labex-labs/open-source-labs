# RAII

Переменные в Rust делают больше, чем просто хранить данные на стеке: они также _владеют_ ресурсами, например, `Box<T>` владеет памятью в куче. Rust налагает требования RAII (Resource Acquisition Is Initialization), поэтому всякий раз, когда объект выходит из области видимости, вызывается его деструктор и освобождаются его принадлежащие ресурсы.

Это поведение защищает от ошибок _утечки ресурсов_, поэтому вы больше никогда не будете вручную освобождать память или беспокоиться о утечках памяти! Вот краткое демонстрация:

```rust
// raii.rs
fn create_box() {
    // Выделить целое число в куче
    let _box1 = Box::new(3i32);

    // `_box1` уничтожается здесь, и память освобождается
}

fn main() {
    // Выделить целое число в куче
    let _box2 = Box::new(5i32);

    // Вложенная область видимости:
    {
        // Выделить целое число в куче
        let _box3 = Box::new(4i32);

        // `_box3` уничтожается здесь, и память освобождается
    }

    // Создаем много коробок просто для好玩ства
    // Нет необходимости вручную освобождать память!
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` уничтожается здесь, и память освобождается
}
```

Конечно, мы можем дополнительно проверить на ошибки памяти с использованием `valgrind`:

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc raii.rs && valgrind./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command:./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```

Здесь нет утечек!

## Деструктор

Концепция деструктора в Rust предоставляется через трейт \[`Drop`\]. Деструктор вызывается, когда ресурс выходит из области видимости. Этот трейт не требуется реализовывать для каждого типа, реализуйте его только для своего типа, если вам нужна собственная логика деструктора.

Запустите следующий пример, чтобы увидеть, как работает трейт \[`Drop`\]. Когда переменная в функции `main` выходит из области видимости, будет вызван пользовательский деструктор.

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop is being dropped");
    }
}

fn main() {
    let x = ToDrop;
    println!("Made a ToDrop!");
}
```
