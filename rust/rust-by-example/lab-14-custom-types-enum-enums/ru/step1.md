# Перечисления (`enum`)

Ключевое слово `enum` позволяет создавать тип, который может быть одним из нескольких различных вариантов. Любой вариант, допустимый для `struct`, также допустим в `enum`.

```rust
// Создаем `enum`, чтобы классифицировать веб-события. Обратите внимание, как
// имена и типная информация вместе определяют вариант:
// `PageLoad!= PageUnload` и `KeyPress(char)!= Paste(String)`.
// Каждый вариант уникален и независим.
enum WebEvent {
    // Вариант `enum` может быть `unit-like`,
    PageLoad,
    PageUnload,
    // похож на кортежные структуры,
    KeyPress(char),
    Paste(String),
    // или структуры, похожие на C.
    Click { x: i64, y: i64 },
}

// Функция, которая принимает `enum` WebEvent в качестве аргумента и
// ничего не возвращает.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("страница загружена"),
        WebEvent::PageUnload => println!("страница выгружена"),
        // Извлекаем `c` из варианта `enum`.
        WebEvent::KeyPress(c) => println!("нажата клавиша '{}'.", c),
        WebEvent::Paste(s) => println!("вставлено \"{}\".", s),
        // Извлекаем `Click` в `x` и `y`.
        WebEvent::Click { x, y } => {
            println!("клик по координатам x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` создает собственное `String` из среза строки.
    let pasted  = WebEvent::Paste("my text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;

    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);
}
```

## Псевдонимы типов (`type aliases`)

Если вы используете псевдоним типа, вы можете ссылаться на каждый вариант `enum` через его псевдоним. Это может быть полезно, если имя `enum` слишком длинное или слишком общее, и вы хотите его переименовать.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// Создает псевдоним типа
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // Мы можем ссылаться на каждый вариант через его псевдоним, а не через его длинное и неудобное
    // имя.
    let x = Operations::Add;
}
```

Самое частое место, где вы увидите это, — это в `impl`-блоках, использующих псевдоним `Self`.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

Для получения более подробной информации о `enum` и псевдонимах типов вы можете прочитать отчет о стабилизации, когда эта функция была стабилизирована в Rust.
