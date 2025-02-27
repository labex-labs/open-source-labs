# Strings

In Rust gibt es zwei Arten von Strings: `String` und `&str`.

Ein `String` wird als Vektor von Bytes (`Vec<u8>`) gespeichert, ist jedoch als gültige UTF-8-Sequenz garantiert. `String` wird auf dem Heap zugewiesen, ist wachsend und nicht null-terminiert.

`&str` ist ein Slice (`&[u8]`), das immer auf eine gültige UTF-8-Sequenz zeigt und wie `&[T]` ein Blick in ein `Vec<T>` auch zum Betrachten eines `Strings` verwendet werden kann.

```rust
fn main() {
    // (alle Typangaben sind überflüssig)
    // Ein Verweis auf einen in nur lesendem Speicher zugewiesenen String
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Pangram: {}", pangram);

    // Iteriere über die Wörter in umgekehrter Reihenfolge, kein neuer String wird zugewiesen
    println!("Wörter in umgekehrter Reihenfolge");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // Kopiere die Zeichen in einen Vektor, sortiere und entferne Duplikate
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // Erstelle einen leeren und wachsenden `String`
    let mut string = String::new();
    for c in chars {
        // Füge ein Zeichen am Ende des Strings hinzu
        string.push(c);
        // Füge einen String am Ende des Strings hinzu
        string.push_str(", ");
    }

    // Der abgeschnittene String ist ein Slice auf den ursprünglichen String, daher wird keine neue
    // Zuweisung durchgeführt
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Verwendete Zeichen: {}", trimmed_str);

    // Weise einen String auf dem Heap zu
    let alice = String::from("I like dogs");
    // Weise neues Speicher zu und speichere den modifizierten String dort
    let bob: String = alice.replace("dog", "cat");

    println!("Alice sagt: {}", alice);
    println!("Bob sagt: {}", bob);
}
```

Weitere `str`/`String`-Methoden können im `std::str`- und `std::string`-Modul gefunden werden.

## Literale und Escape-Sequenzen

Es gibt mehrere Möglichkeiten, Stringliterale mit Sonderzeichen darin zu schreiben. Alle führen zu einem ähnlichen `&str`, daher ist es am besten, die am bequemsten zu schreibende Form zu verwenden. Ähnlich gibt es mehrere Möglichkeiten, Byte-Stringliterale zu schreiben, die alle zu `&[u8; N]` führen.

Allgemein werden Sonderzeichen mit einem Backslash-Zeichen (`\`) escapet. Auf diese Weise können Sie jedem String beliebige Zeichen hinzufügen, auch unausdruckbare und solche, die Sie nicht kennen wie man sie tippen würde. Wenn Sie einen einfachen Backslash haben möchten, escapen Sie ihn mit einem weiteren: `\\`

String- oder Zeichenliteral-Delimiter, die innerhalb eines Literals auftauchen, müssen escapet werden: `"\""`, `'\''`.

```rust
fn main() {
    // Sie können Escape-Sequenzen verwenden, um Bytes nach ihren hexadezimalen Werten zu schreiben...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("What are you doing\x3F (\\x3F bedeutet?) {}", byte_escape);

    //...oder Unicode-Codepunkte.
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("Unicode-Zeichen {} (U+211D) heißt {}",
                unicode_codepoint, character_name );


    let long_string = "String literals
                        können über mehrere Zeilen gehen.
                        Der Zeilenumbruch und die Einrückung hier ->\
                        <- können ebenfalls escapet werden!";
    println!("{}", long_string);
}
```

Manchmal gibt es einfach zu viele Zeichen, die escapet werden müssen, oder es ist einfach bequemer, einen String so wie er ist zu schreiben. Hier kommen Raw-Stringliterale ins Spiel.

```rust
fn main() {
    let raw_str = r"Escapes funktionieren hier nicht: \x3F \u{211D}";
    println!("{}", raw_str);

    // Wenn Sie in einem Raw-String Anführungszeichen benötigen, fügen Sie ein Paar #s hinzu
    let quotes = r#"And then I said: "There is no escape!""#;
    println!("{}", quotes);

    // Wenn Sie # in Ihrem String benötigen, verwenden Sie einfach mehr #s im Delimiter.
    // Sie können bis zu 65535 #s verwenden.
    let longer_delimiter = r###"A string with "# in it. And even "##!"###;
    println!("{}", longer_delimiter);
}
```

Wollen Sie einen String, der nicht UTF-8 ist? (Denken Sie daran, `str` und `String` müssen gültige UTF-8 sein). Oder möchten Sie vielleicht ein Array von Bytes, das hauptsächlich Text ist? Byte-Strings kommen als Retter!

```rust
use std::str;

fn main() {
    // Beachten Sie, dass dies tatsächlich kein `&str` ist
    let bytestring: &[u8; 21] = b"this is a byte string";

    // Byte-Arrays haben das `Display`-Trait nicht, daher ist das Drucken von ihnen etwas eingeschränkt
    println!("Ein Byte-String: {:?}", bytestring);

    // Byte-Strings können Byte-Escape-Sequenzen haben...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    //...aber keine Unicode-Escape-Sequenzen
    // let escaped = b"\u{211D} is not allowed";
    println!("Einige escapete Bytes: {:?}", escaped);


    // Raw-Byte-Strings funktionieren genauso wie Raw-Strings
    let raw_bytestring = br"\u{211D} is not escaped here";
    println!("{:?}", raw_bytestring);

    // Das Konvertieren eines Byte-Arrays in `str` kann fehlschlagen
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("Und als Text gleich: '{}'", my_str);
    }

    let _quotes = br#"You can also use "fancier" formatting, \
                    like with normal raw strings"#;

    // Byte-Strings müssen nicht UTF-8 sein
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" in SHIFT-JIS

    // Aber dann können sie nicht immer in `str` konvertiert werden
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("Konvertierung erfolgreich: '{}'", my_str),
        Err(e) => println!("Konvertierung fehlgeschlagen: {:?}", e),
    };
}
```

Für Umwandlungen zwischen Zeichensätzen schauen Sie sich das encoding-Crate an.

Eine detailliertere Auflistung der Möglichkeiten, Stringliterale und Escape-Zeichen zu schreiben, finden Sie im Kapitel 'Tokens' der Rust-Referenz.
