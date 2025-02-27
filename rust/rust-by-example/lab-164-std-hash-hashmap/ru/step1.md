# HashMap

В то время как векторы хранят значения по целочисленному индексу, `HashMap` хранит значения по ключу. Ключи `HashMap` могут быть булевыми значениями, целыми числами, строками или любым другим типом, реализующим трейты `Eq` и `Hash`. Более подробно об этом в следующем разделе.

Похоже на векторы, `HashMap` могут увеличиваться, но они также могут уменьшать размер, если у них есть избыточное пространство. Вы можете создать `HashMap` с определенной начальной емкостью с использованием `HashMap::with_capacity(uint)`, или использовать `HashMap::new()`, чтобы получить `HashMap` с начальным значением емкости по умолчанию (рекомендуется).

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "We're sorry, the call cannot be completed as dialed.
            Please hang up and try again.",
        "645-7689" => "Hello, this is Mr. Awesome's Pizza. My name is Fred.
            What can I get for you today?",
        _ => "Hi! Who is this again?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // Возвращает ссылку и возвращает Option<&V>
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Calling Daniel: {}", call(number)),
        _ => println!("Don't have Daniel's number."),
    }

    // `HashMap::insert()` возвращает `None`,
    // если вставляемое значение новое, `Some(value)` в противном случае
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Calling Ashley: {}", call(number)),
        _ => println!("Don't have Ashley's number."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` возвращает итератор, который возвращает
    // (&'a ключ, &'a значение) пары в произвольном порядке.
    for (contact, &number) in contacts.iter() {
        println!("Calling {}: {}", contact, call(number));
    }
}
```

Для получения дополнительной информации о том, как работают хеширование и хеш-таблицы (иногда называемые хеш-таблицами), ознакомьтесь с Википедией о хеш-таблицах.
