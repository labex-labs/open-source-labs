# Erstellen eines neuen Strings

Viele der gleichen Operationen, die mit `Vec<T>` möglich sind, sind auch mit `String` verfügbar, da `String` tatsächlich als Wrapper um einen Byte-Vektor mit einigen zusätzlichen Garantien, Einschränkungen und Funktionen implementiert ist. Ein Beispiel für eine Funktion, die auf die gleiche Weise mit `Vec<T>` und `String` funktioniert, ist die `new`-Funktion, um eine Instanz zu erstellen, wie in Listing 8-11 gezeigt.

```rust
let mut s = String::new();
```

Listing 8-11: Erstellen eines neuen, leeren `Strings`

Dieser Code erstellt einen neuen, leeren String namens `s`, in den wir dann Daten laden können. Oft haben wir einige Anfangsdaten, mit denen wir den String beginnen möchten. Dazu verwenden wir die `to_string`-Methode, die für jede Art verfügbar ist, die das `Display`-Attribut implementiert, wie dies bei String-Literalen der Fall ist. Listing 8-12 zeigt zwei Beispiele.

```rust
let data = "initial contents";

let s = data.to_string();

// die Methode funktioniert auch direkt auf einem Literal:
let s = "initial contents".to_string();
```

Listing 8-12: Verwenden der `to_string`-Methode, um einen `String` aus einem String-Literal zu erstellen

Dieser Code erstellt einen String, der `initial contents` enthält.

Wir können auch die Funktion `String::from` verwenden, um einen `String` aus einem String-Literal zu erstellen. Der Code in Listing 8-13 ist dem Code in Listing 8-12, der `to_string` verwendet, äquivalent.

```rust
let s = String::from("initial contents");
```

Listing 8-13: Verwenden der `String::from`-Funktion, um einen `String` aus einem String-Literal zu erstellen

Da Strings für so viele Dinge verwendet werden, können wir viele verschiedene generische APIs für Strings verwenden, was uns viele Optionen bietet. Einige von ihnen können redundant erscheinen, aber sie alle haben ihren Platz! In diesem Fall machen `String::from` und `to_string` das gleiche, also ist die Wahl, welche Sie verwenden, eine Frage der Stil- und Lesbarkeit.

Denken Sie daran, dass Strings UTF-8-kodiert sind, sodass wir in ihnen beliebige richtig codierte Daten einschließen können, wie in Listing 8-14 gezeigt.

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שָׁלוֹם");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

Listing 8-14: Speichern von Begrüßungen in verschiedenen Sprachen in Strings

Alle diese sind gültige `String`-Werte.
