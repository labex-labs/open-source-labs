# Prägnanter Kontrollfluss mit if let

Die `if let`-Syntax ermöglicht es, `if` und `let` zu kombinieren, um Werte, die einem Muster entsprechen, auf weniger umständige Weise zu behandeln, während der Rest ignoriert wird. Betrachten Sie das Programm in Listing 6-6, das auf einen `Option<u8>`-Wert in der `config_max`-Variable prüft, aber nur dann Code ausführen möchte, wenn der Wert der `Some`-Variante entspricht.

```rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {max}"),
    _ => (),
}
```

Listing 6-6: Ein `match`, das nur dann Code ausführt, wenn der Wert `Some` ist

Wenn der Wert `Some` ist, geben wir den Wert in der `Some`-Variante aus, indem wir den Wert an die Variable `max` im Muster binden. Wir möchten nichts mit dem `None`-Wert tun. Um den `match`-Ausdruck zu befriedigen, müssen wir nach der Verarbeitung nur einer Variante `_ => ()` hinzufügen, was eine lästige Boilerplate-Code-Zeile ist.

Stattdessen können wir dies auf kürzere Weise mit `if let` schreiben. Der folgende Code verhält sich genauso wie das `match` in Listing 6-6:

```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {max}");
}
```

Die Syntax `if let` nimmt ein Muster und einen Ausdruck, die durch ein Gleichheitszeichen getrennt sind. Es funktioniert auf die gleiche Weise wie ein `match`, wobei der Ausdruck an das `match` übergeben wird und das Muster der erste Arm ist. Im diesem Fall ist das Muster `Some(max)`, und `max` bindet sich an den Wert innerhalb von `Some`. Wir können dann `max` im Körper des `if let`-Blocks genauso verwenden wie wir `max` im entsprechenden `match`-Arm verwendet haben. Der Code im `if let`-Block wird nicht ausgeführt, wenn der Wert nicht mit dem Muster übereinstimmt.

Das Verwenden von `if let` bedeutet weniger Tipparbeit, weniger Einrückungen und weniger Boilerplate-Code. Allerdings verlieren Sie die erschöpfende Prüfung, die `match` erzwingt. Das Auswählen zwischen `match` und `if let` hängt davon ab, was Sie in Ihrer speziellen Situation tun und ob die Gewinnung an Kürze ein angemessener Kompromiss für das Verlust an erschöpfender Prüfung ist.

Mit anderen Worten, Sie können sich `if let` als Syntaxzucker für ein `match` vorstellen, das Code ausführt, wenn der Wert einem Muster entspricht, und alle anderen Werte ignoriert.

Wir können ein `else` mit einem `if let` hinzufügen. Der Codeblock, der mit dem `else` zusammenhängt, ist derselbe wie der Codeblock, der mit dem `_`-Fall im `match`-Ausdruck zusammenhängen würde, der dem `if let` und `else` entspricht. Denken Sie sich die `Coin`-Enum-Definition in Listing 6-4 zurück, wobei die `Quarter`-Variante auch einen `UsState`-Wert enthielt. Wenn wir alle nicht Viertel-Münzen zählen möchten, die wir sehen, und gleichzeitig den Zustand der Viertel-Münzen bekanntgeben möchten, könnten wir das mit einem `match`-Ausdruck tun, wie folgt:

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    _ => count += 1,
}
```

Oder wir könnten einen `if let`- und `else`-Ausdruck verwenden, wie folgt:

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

Wenn Sie in einer Situation sind, in der die Logik Ihres Programms zu umständig ist, um mit einem `match` ausgedrückt zu werden, denken Sie daran, dass `if let` ebenfalls im Rust-Werkzeugkasten vorhanden ist.
