# Strings hin und her

## Umwandlung in einen String

Um einen beliebigen Typ in einen `String` umzuwandeln, ist es so einfach wie das Implementieren des \[`ToString`\]-Attributs für den Typ. Anstatt dies direkt zu tun, sollten Sie das `fmt::Display`-Attribut implementieren, das automatisch \[`ToString`\] bereitstellt und auch das Ausgeben des Typs wie im Abschnitt zu `print!` beschrieben ermöglicht.

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## Analysieren eines Strings

Einer der häufigeren Typen, in den ein String umgewandelt wird, ist eine Zahl. Der übliche Ansatz hierfür ist, die \[`parse`\]-Funktion zu verwenden und entweder auf Typinferenz zu setzen oder den zu parsenden Typ mithilfe der 'Turbofish'-Syntax anzugeben. Beide Alternativen werden im folgenden Beispiel gezeigt.

Dies wird den String in den angegebenen Typ umwandeln, solange das \[`FromStr`\]-Attribut für diesen Typ implementiert ist. Dies ist für zahlreiche Typen in der Standardbibliothek implementiert. Um diese Funktionalität für einen benutzerdefinierten Typ zu erhalten, implementieren Sie einfach das \[`FromStr`\]-Attribut für diesen Typ.

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("Sum: {:?}", sum);
}
```
