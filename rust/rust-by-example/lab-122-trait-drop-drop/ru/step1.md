# Drop

Трейт `Drop` имеет только один метод: `drop`, который вызывается автоматически, когда объект выходит из области видимости. Основное назначение трейта `Drop` - освобождать ресурсы, принадлежащие экземпляру реализатора.

`Box`, `Vec`, `String`, `File` и `Process` - это некоторые примеры типов, которые реализуют трейт `Drop` для освобождения ресурсов. Трейт `Drop` также можно вручную реализовать для любого пользовательского типа данных.

Следующий пример добавляет вывод в консоль в функцию `drop`, чтобы сообщить, когда она вызывается.

```rust
struct Droppable {
    name: &'static str,
}

// Эта тривиальная реализация `drop` добавляет вывод в консоль.
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // блок A
    {
        let _b = Droppable { name: "b" };

        // блок B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // Переменную можно вручную удалить с помощью функции `drop`
    drop(_a);
    // TODO ^ Попробуйте закомментировать эту строку

    println!("end of the main function");

    // `_a` *не будет* снова удалено здесь, потому что оно уже было
    // (вручную) удалено
}
```
