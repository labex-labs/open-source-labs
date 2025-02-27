# Строки

В Rust есть два типа строк: `String` и `&str`.

`String` хранится в виде вектора байтов (`Vec<u8>`), но гарантируется, что всегда является допустимой последовательностью UTF-8. `String` выделяется в куче, может увеличиваться и не заканчивается нулевым байтом.

`&str` - это срез (`&[u8]`), который всегда указывает на допустимую последовательность UTF-8 и может использоваться для просмотра `String`, точно так же, как `&[T]` - это представление для `Vec<T>`.

```rust
fn main() {
    // (все аннотации типов лишние)
    // Ссылка на строку, выделенную в памяти с атрибутом read only
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Панграмма: {}", pangram);

    // Перебираем слова в обратном порядке, не выделяется новая строка
    println!("Слова в обратном порядке");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // Копируем символы в вектор, сортируем и удаляем дубликаты
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // Создаем пустую и расширяемую `String`
    let mut string = String::new();
    for c in chars {
        // Вставляем символ в конец строки
        string.push(c);
        // Вставляем строку в конец строки
        string.push_str(", ");
    }

    // Обрезанная строка - это срез к исходной строке, поэтому не выделяется новая
    // память
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Используемые символы: {}", trimmed_str);

    // Выделяем строку в куче
    let alice = String::from("I like dogs");
    // Выделяем новую память и храним в ней измененную строку
    let bob: String = alice.replace("dog", "cat");

    println!("Alice говорит: {}", alice);
    println!("Bob говорит: {}", bob);
}
```

Больше методов для `str`/`String` можно найти в модулях `std::str` и `std::string`.

## Литералы и экранирование

Существует несколько способов записать литералы строк с специальными символами. Все они приводят к аналогичному `&str`, поэтому лучше использовать тот вид, который наиболее удобен для записи. Аналогично существуют несколько способов записать литералы байтовых строк, которые все приводят к `&[u8; N]`.

В общем, специальные символы экранируются с помощью обратной косой черты: `\`. Таким образом, вы можете добавить любой символ в свою строку, даже непечатаемые и те, которые вы не знаете, как набрать. Если вы хотите получить литеральную обратную косую черту, экранируйте ее еще одной: `\\`

Литералы строк или символов, встречающиеся внутри литерала, должны быть экранированы: `"\""`, `'\''`.

```rust
fn main() {
    // Вы можете использовать экранирование для записи байтов по их шестнадцатеричным значениям...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("Что ты делаешь\x3F (\\x3F означает?) {}", byte_escape);

    //...или кодовые точки Unicode.
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("Юникодный символ {} (U+211D) называется {}",
                unicode_codepoint, character_name );


    let long_string = "String literals
                        can span multiple lines.
                        The linebreak and indentation here ->\
                        <- can be escaped too!";
    println!("{}", long_string);
}
```

Иногда нужно экранировать слишком много символов или проще всего записать строку как есть. Именно здесь на помощь приходят сырые литералы строк.

```rust
fn main() {
    let raw_str = r"Escapes don't work here: \x3F \u{211D}";
    println!("{}", raw_str);

    // Если вам нужны кавычки в сырой строке, добавьте пару #
    let quotes = r#"And then I said: "There is no escape!""#;
    println!("{}", quotes);

    // Если вам нужен "# в своей строке, просто используйте больше # в разделителе.
    // Вы можете использовать до 65535 #.
    let longer_delimiter = r###"A string with "# in it. And even "##!"###;
    println!("{}", longer_delimiter);
}
```

Хотите строку, которая не является UTF-8? (Помните, `str` и `String` должны быть допустимыми UTF-8). Или, может быть, вам нужен массив байтов, который в основном состоит из текста? На помощь приходят байтовые строки!

```rust
use std::str;

fn main() {
    // Обратите внимание, что это на самом деле не `&str`
    let bytestring: &[u8; 21] = b"this is a byte string";

    // Байтовые массивы не имеют трейта `Display`, поэтому их печать ограничена
    println!("Байтовая строка: {:?}", bytestring);

    // Байтовые строки могут иметь экранирование байтов...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    //...но не Unicode-escapes
    // let escaped = b"\u{211D} is not allowed";
    println!("Некоторые экранированные байты: {:?}", escaped);


    // Сырые байтовые строки работают точно так же, как сырые строки
    let raw_bytestring = br"\u{211D} is not escaped here";
    println!("{:?}", raw_bytestring);

    // Преобразование байтового массива в `str` может завершиться ошибкой
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("И то же самое в виде текста: '{}'", my_str);
    }

    let _quotes = br#"You can also use "fancier" formatting, \
                    like with normal raw strings"#;

    // Байтовые строки не обязательно должны быть UTF-8
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" в SHIFT-JIS

    // Но тогда они не всегда могут быть преобразованы в `str`
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("Преобразование успешно: '{}'", my_str),
        Err(e) => println!("Преобразование не удалось: {:?}", e),
    };
}
```

Для преобразования между кодировками символов ознакомьтесь с crate `encoding`.

Подробнее о способах записи литералов строк и экранирования символов можно найти в главе 'Tokens' Rust Reference.
