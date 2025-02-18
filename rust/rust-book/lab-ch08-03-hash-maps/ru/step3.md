# Получение значений из хеш - таблицы (hash map)

Мы можем получить значение из хеш - таблицы, передав его ключ методу `get`, как показано в листинге 8 - 21.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

Листинг 8 - 21: Получение счета команды Blue, хранящегося в хеш - таблице

Здесь переменная `score` будет содержать значение, связанное с командой Blue, и результатом будет `10`. Метод `get` возвращает `Option<&V>`; если в хеш - таблице нет значения для данного ключа, метод `get` вернет `None`. Эта программа обрабатывает `Option`, вызывая метод `copied` для получения `Option<i32>` вместо `Option<&i32>`, а затем `unwrap_or` для установки значения `score` равным нулю, если в `scores` нет записи для данного ключа.

Мы можем перебирать каждую пару ключ - значение в хеш - таблице аналогично тому, как мы это делаем с векторами, используя цикл `for`:

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

Этот код выведет каждую пару в произвольном порядке:

```rust
Yellow: 50
Blue: 10
```
