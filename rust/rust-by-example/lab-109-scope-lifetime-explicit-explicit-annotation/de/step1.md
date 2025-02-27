# Explizite Annotation

Der Entleihensprüfer verwendet explizite Lebenszeitangaben, um zu bestimmen, wie lange Referenzen gültig sein sollten. Wenn Lebenszeiten nicht weggelassen werden, erfordert Rust explizite Annotations, um zu bestimmen, wie lang die Lebenszeit einer Referenz sein sollte. Die Syntax zur expliziten Annotation einer Lebenszeit verwendet ein Apostroph-Zeichen wie folgt:

```rust
foo<'a>
// `foo` hat einen Lebenszeitparameter `'a`
```

Ähnlich wie bei Closures erfordert das Verwenden von Lebenszeiten Generics. Darüber hinaus zeigt diese Lebenszeitsyntax an, dass die Lebenszeit von `foo` nicht länger als die von `'a` sein darf. Die explizite Annotation eines Typs hat die Form `&'a T`, wobei `'a` bereits definiert wurde.

Bei mehreren Lebenszeiten ist die Syntax ähnlich:

```rust
foo<'a, 'b>
// `foo` hat Lebenszeitparameter `'a` und `'b`
```

In diesem Fall kann die Lebenszeit von `foo` nicht länger als die von `'a` _oder_ `'b` sein.

Siehe folgendes Beispiel für die Verwendung expliziter Lebenszeitangaben:

```rust
// `print_refs` nimmt zwei Referenzen auf `i32` entgegen, die unterschiedliche
// Lebenszeiten `'a` und `'b` haben. Beide Lebenszeiten müssen mindestens so lang
// wie die Funktion `print_refs` sein.
fn print_refs<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("x ist {} und y ist {}", x, y);
}

// Eine Funktion, die keine Argumente nimmt, aber einen Lebenszeitparameter `'a` hat.
fn failed_borrow<'a>() {
    let _x = 12;

    // FEHLER: `_x` lebt nicht lang genug
    let y: &'a i32 = &_x;
    // Versuch, die Lebenszeit `'a` als expliziten Typannotation innerhalb der
    // Funktion zu verwenden, wird fehlschlagen, weil die Lebenszeit von `&_x`
    // kürzer ist als die von `y`. Eine kurze Lebenszeit kann nicht in eine
    // längere umgewandelt werden.
}

fn main() {
    // Erstellen Sie Variablen, die später entliehen werden.
    let (vier, neun) = (4, 9);

    // Entleihungen (`&`) beider Variablen werden an die Funktion übergeben.
    print_refs(&vier, &neun);
    // Jede Eingabe, die entliehen wird, muss länger als der Entleiher existieren.
    // Mit anderen Worten, die Lebenszeit von `vier` und `neun` muss länger
    // sein als die von `print_refs`.

    failed_borrow();
    // `failed_borrow` enthält keine Referenzen, um `'a` länger als die Lebenszeit
    // der Funktion zu erzwingen, aber `'a` ist länger. Da die Lebenszeit nie
    // eingeschränkt wird, standardmäßig auf `'static`.
}
```
