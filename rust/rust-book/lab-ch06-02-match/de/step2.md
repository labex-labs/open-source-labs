# Muster, die an Werte binden

Ein weiterer nützlicher Aspekt von `match`-Armen ist, dass sie an die Teile der Werte binden können, die mit dem Muster übereinstimmen. So können wir Werte aus Enum-Varianten extrahieren.

Als Beispiel ändern wir eine unserer Enum-Varianten, um Daten darin zu speichern. Zwischen 1999 und 2008 prägte die Vereinigten Staaten fünfundzwanzig-Cent-Münzen mit unterschiedlichen Designs für jede der 50 Bundesstaaten auf einer Seite. Keine anderen Münzen erhielten Designs für die Bundesstaaten, sodass nur die fünfundzwanzig-Cent-Münzen diesen zusätzlichen Wert haben. Wir können diese Information zu unserem `enum` hinzufügen, indem wir die `Quarter`-Variante ändern, um einen `UsState`-Wert darin zu speichern, was wir in Listing 6-4 getan haben.

```rust
#[derive(Debug)] // damit wir den Zustand in einem Moment überprüfen können
enum UsState {
    Alabama,
    Alaska,
    --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```

Listing 6-4: Ein `Coin`-Enum, in dem die `Quarter`-Variante auch einen `UsState`-Wert speichert

Stellen Sie sich vor, dass ein Freund versucht, alle 50 Bundesstaat-Fünfundzwanzig-Cent-Münzen zu sammeln. Während wir unser Losegeld nach Münztyp sortieren, werden wir auch den Namen des Bundesstaates nennen, der mit jeder fünfundzwanzig-Cent-Münze assoziiert ist, damit, wenn es eine Münze ist, die unser Freund nicht hat, er sie zu seiner Sammlung hinzufügen kann.

Im `match`-Ausdruck für diesen Code fügen wir eine Variable namens `state` zum Muster hinzu, das Werte der Variante `Coin::Quarter` übereinstimmt. Wenn ein `Coin::Quarter` übereinstimmt, wird die Variable `state` an den Wert des Bundesstaates dieser fünfundzwanzig-Cent-Münze gebunden. Dann können wir `state` im Code für diesen Arm verwenden, wie folgt:

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

Wenn wir `value_in_cents(Coin::Quarter(UsState::Alaska))` aufrufen würden, wäre `coin` `Coin::Quarter(UsState::Alaska)`. Wenn wir diesen Wert mit jedem der `match`-Arme vergleichen, stimmen keiner von ihnen überein, bis wir `Coin::Quarter(state)` erreichen. An diesem Punkt wird die Bindung für `state` der Wert `UsState::Alaska` sein. Wir können dann diese Bindung im `println!`-Ausdruck verwenden und so den inneren Bundesstaat-Wert aus der `Coin`-Enum-Variante für `Quarter` herausholen.
