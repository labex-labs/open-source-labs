# Hinzufügen von nützlicher Funktionalität mit abgeleiteten Traits

Es wäre nützlich, während des Debuggings unseres Programms eine `Rectangle`-Instanz ausdrucken zu können und die Werte aller ihrer Felder anzeigen zu sehen. Listing 5-11 versucht, die `println!`-Makro wie in vorherigen Kapiteln zu verwenden. Dies funktioniert jedoch nicht.

Dateiname: `src/main.rs`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 ist {}", rect1);
}
```

Listing 5-11: Versuch, eine `Rectangle`-Instanz auszugeben

Wenn wir diesen Code kompilieren, erhalten wir einen Fehler mit dieser Kernmeldung:

```bash
error[E0277]: `Rectangle` implementiert `std::fmt::Display` nicht
```

Das `println!`-Makro kann viele Arten von Formatierung durchführen, und standardmäßig sagen die geschweiften Klammern `println!`, dass es die Formatierung `Display` verwenden soll: Ausgabe, die für den direkten Endbenutzer bestimmt ist. Die primitiven Typen, die wir bisher gesehen haben, implementieren `Display` standardmäßig, da es nur eine Möglichkeit gibt, eine `1` oder irgendeinen anderen primitiven Typ einem Benutzer zu zeigen. Bei Structs ist jedoch die Art, wie `println!` die Ausgabe formatieren soll, weniger klar, da es mehr Anzeigemöglichkeiten gibt: Möchten Sie Kommas oder nicht? Möchten Sie die geschweiften Klammern ausgeben? Sollen alle Felder angezeigt werden? Aufgrund dieser Mehrdeutigkeit versucht Rust nicht, zu erraten, was wir möchten, und Structs haben keine bereitgestellte Implementierung von `Display`, um mit `println!` und dem `{}`-Platzhalter zu verwenden.

Wenn wir die Fehler weiter lesen, finden wir diese hilfreiche Anmerkung:

    = help: das Trait `std::fmt::Display` ist für `Rectangle` nicht implementiert
    = note: in Formatstrings können Sie möglicherweise `{:?}` (oder {:#?} für
    schöne Ausgabe) verwenden

Lassen Sie uns es ausprobieren! Der `println!`-Makroaufruf sieht jetzt so aus: `println!("rect1 ist {:?}", rect1);`. Indem wir den Spezifizierer `:?` in die geschweiften Klammern setzen, sagen wir `println!`, dass wir ein Ausgabeformat namens `Debug` verwenden möchten. Das `Debug`-Trait ermöglicht es uns, unsere Struct auf eine Weise auszugeben, die für Entwickler nützlich ist, sodass wir ihren Wert während des Debuggings unseres Codes sehen können.

Kompilieren Sie den Code mit dieser Änderung. Verdammt! Wir erhalten immer noch einen Fehler:

```bash
error[E0277]: `Rectangle` implementiert `Debug` nicht
```

Aber wiederum gibt uns der Compiler eine hilfreiche Anmerkung:

```rust
= help: das Trait `Debug` ist für `Rectangle` nicht implementiert
= note: fügen Sie `#[derive(Debug)]` hinzu oder implementieren Sie `Debug` manuell
```

Rust _hat_ tatsächlich Funktionalität, um Debuginformationen auszugeben, aber wir müssen explizit aktivieren, um diese Funktionalität für unsere Struct zur Verfügung zu stellen. Dazu fügen wir das äußere Attribut `#[derive(Debug)]` direkt vor der Struct-Definition hinzu, wie in Listing 5-12 gezeigt.

Dateiname: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 ist {:?}", rect1);
}
```

Listing 5-12: Hinzufügen des Attributes, um das `Debug`-Trait abzuleiten und die `Rectangle`-Instanz mit Debug-Formatierung auszugeben

Wenn wir jetzt das Programm ausführen, erhalten wir keine Fehler mehr, und wir sehen die folgende Ausgabe:

```rust
rect1 ist Rectangle { width: 30, height: 50 }
```

Super! Es ist nicht die schönste Ausgabe, aber sie zeigt die Werte aller Felder für diese Instanz, was definitiv bei der Fehlersuche helfen würde. Wenn wir größere Structs haben, ist es nützlich, eine Ausgabe zu haben, die etwas leichter lesbar ist; in diesen Fällen können wir in der `println!`-Zeichenfolge `{:#?}` statt `{:?}` verwenden. In diesem Beispiel wird die Ausgabe mit dem `{:#?}`-Format wie folgt aussehen:

    rect1 ist Rectangle {
        width: 30,
        height: 50,
    }

Eine andere Möglichkeit, einen Wert im `Debug`-Format auszugeben, ist die Verwendung des `dbg!`-Makros, das die Eigentumsgewalt eines Ausdrucks übernimmt (im Gegensatz zu `println!`, das eine Referenz nimmt), druckt die Datei und die Zeilennummer, an der der `dbg!`-Makroaufruf in Ihrem Code auftritt, zusammen mit dem resultierenden Wert dieses Ausdrucks und gibt die Eigentumsgewalt des Werts zurück.

> Hinweis: Der Aufruf des `dbg!`-Makros druckt auf den Standardfehlerkonsolenstrom (`stderr`), im Gegensatz zu `println!`, das auf den Standardausgabekonsolenstrom (`stdout`) druckt. Wir werden in "Schreiben von Fehlermeldungen an die Standardfehlerstelle anstelle der Standardausgabe" mehr über `stderr` und `stdout` sprechen.

Hier ist ein Beispiel, in dem wir an den Wert interessiert sind, der dem `width`-Feld zugewiesen wird, sowie an dem Wert der gesamten Struct in `rect1`:

Dateiname: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
      1 width: dbg!(30 * scale),
        height: 50,
    };

  2 dbg!(&rect1);
}
```

Wir können `dbg!` um den Ausdruck `30 * scale` legen \[1\], und da `dbg!` die Eigentumsgewalt des Ausdrucks' Werts zurückgibt, wird das `width`-Feld den gleichen Wert erhalten wie, wenn wir den `dbg!`-Aufruf dort nicht hätten. Wir möchten nicht, dass `dbg!` die Eigentumsgewalt von `rect1` übernimmt, daher verwenden wir in dem nächsten Aufruf eine Referenz auf `rect1` \[2\]. Hier sieht die Ausgabe dieses Beispiels aus:

    [src/main.rs:10] 30 * scale = 60
    [src/main.rs:14] &rect1 = Rectangle {
        width: 60,
        height: 50,
    }

Wir können sehen, dass der erste Ausgabeanteil von \[1\] stammt, wo wir den Ausdruck `30 * scale` debuggen, und sein resultierender Wert ist `60` (die für Integer implementierte `Debug`-Formatierung ist es, nur ihren Wert auszugeben). Der `dbg!`-Aufruf bei \[2\] gibt den Wert von `&rect1` aus, was die `Rectangle`-Struct ist. Diese Ausgabe verwendet die schöne `Debug`-Formatierung des `Rectangle`-Typs. Das `dbg!`-Makro kann wirklich hilfreich sein, wenn Sie versuchen, herauszufinden, was Ihr Code tut!

Neben dem `Debug`-Trait hat Rust eine Reihe von Traits für uns bereitgestellt, die wir mit dem `derive`-Attribut verwenden können, um nützliches Verhalten zu unseren benutzerdefinierten Typen hinzuzufügen. Diese Traits und ihr Verhalten sind in Anhang C aufgelistet. Wir werden im Kapitel 10 auch besprechen, wie man diese Traits mit benutzerdefiniertem Verhalten implementiert und wie man eigene Traits erstellt. Es gibt auch viele Attribute außer `derive`; für weitere Informationen siehe den Abschnitt "Attribute" in der Rust-Referenz unter *https://doc.rust-lang.org/reference/attributes.html*.

Unsere `area`-Funktion ist sehr spezifisch: sie berechnet nur die Fläche von Rechtecken. Es wäre nützlich, dieses Verhalten enger an unsere `Rectangle`-Struct zu binden, da es mit keinem anderen Typ funktionieren wird. Schauen wir uns an, wie wir diesen Code weiter refaktorisieren können, indem wir die `area`-Funktion in eine `area`-Methode definieren, die auf unserem `Rectangle`-Typ definiert ist.
