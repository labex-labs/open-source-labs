# Der niemals-kehrende Typ

Rust hat einen speziellen Typ namens `!`, der in der Typentheorie als _leerer Typ_ bekannt ist, weil er keine Werte hat. Wir bevorzugen es, ihn als _niemals-Typ_ zu nennen, weil er an der Stelle des Rückgabetyps steht, wenn eine Funktion niemals zurückkehrt. Hier ist ein Beispiel:

```rust
fn bar() ->! {
    --snip--
}
```

Dieser Code wird als "die Funktion `bar` gibt niemals zurück" gelesen. Funktionen, die niemals zurückkehren, werden als _divergierende Funktionen_ bezeichnet. Wir können keine Werte des Typs `!` erstellen, also kann `bar` niemals tatsächlich zurückkehren.

Aber wofür ist ein Typ, für den man keine Werte erstellen kann? Erinnern Sie sich an den Code aus Listing 2-5, einem Teil des Zahlerratspiels; wir haben hier einen Ausschnitt davon in Listing 19-26 wiedergegeben.

```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```

Listing 19-26: Ein `match` mit einem Zweig, der mit `continue` endet

Damals haben wir einige Details in diesem Code übersprungen. Im Abschnitt "Der match-Steuerflusskonstrukt" haben wir diskutiert, dass die Zweige von `match` alle den gleichen Typ zurückgeben müssen. Also funktioniert beispielsweise der folgende Code nicht:

```rust
let guess = match guess.trim().parse() {
    Ok(_) => 5,
    Err(_) => "hello",
};
```

Der Typ von `guess` in diesem Code müsste ein Integer _und_ eine Zeichenkette sein, und Rust erfordert, dass `guess` nur einen Typ hat. Also was gibt `continue` zurück? Wie konnten wir in Listing 19-26 von einem Zweig einen `u32` zurückgeben und einen anderen Zweig haben, der mit `continue` endet?

Wie Sie vielleicht schon erraten haben, hat `continue` einen `!`-Wert. Das heißt, wenn Rust den Typ von `guess` berechnet, betrachtet es beide `match`-Zweige, den einen mit einem Wert vom Typ `u32` und den anderen mit einem `!`-Wert. Da `!` niemals einen Wert haben kann, entscheidet Rust, dass der Typ von `guess` `u32` ist.

Die formale Weise, um dieses Verhalten zu beschreiben, ist, dass Ausdrücke vom Typ `!` in jeden anderen Typ umgewandelt werden können. Wir dürfen diesen `match`-Zweig mit `continue` beenden, weil `continue` keinen Wert zurückgibt; stattdessen bewegt es den Steuerfluss zurück zum Anfang der Schleife, also im `Err`-Fall weisen wir niemals einen Wert an `guess` zu.

Der niemals-Typ ist auch nützlich mit der `panic!`-Makro. Erinnern Sie sich an die `unwrap`-Funktion, die wir auf `Option<T>`-Werten aufrufen, um einen Wert zu erhalten oder mit dieser Definition zu abstürzen:

```rust
impl<T> Option<T> {
    pub fn unwrap(self) -> T {
        match self {
            Some(val) => val,
            None => panic!(
                "called `Option::unwrap()` on a `None` value"
            ),
        }
    }
}
```

In diesem Code passiert dasselbe wie im `match` in Listing 19-26: Rust sieht, dass `val` den Typ `T` hat und `panic!` den Typ `!`, also ist das Ergebnis des gesamten `match`-Ausdrucks `T`. Dieser Code funktioniert, weil `panic!` keinen Wert produziert; es beendet das Programm. Im `None`-Fall werden wir keinen Wert von `unwrap` zurückgeben, also ist dieser Code gültig.

Ein letzter Ausdruck, der den Typ `!` hat, ist eine `loop`:

    print!("forever ");

    loop {
        print!("and ever ");
    }

Hier endet die Schleife niemals, also ist `!` der Wert des Ausdrucks. Dies wäre jedoch nicht der Fall, wenn wir eine `break` einfügen würden, weil die Schleife dann beendet würde, wenn sie auf die `break` stieß.
