# Das match-Steuerflusskonstrukt

Rust hat ein extrem leistungsstarkes Steuerflusskonstrukt namens `match`, das es Ihnen ermöglicht, einen Wert mit einer Reihe von Mustern zu vergleichen und dann basierend auf dem passenden Muster Code auszuführen. Muster können aus Literalwerten, Variablennamen, Platzhaltern und vielen anderen Dingen bestehen; Kapitel 18 behandelt alle verschiedenen Arten von Mustern und was sie tun. Die Stärke von `match` kommt von der Ausdrucksfähigkeit der Muster und der Tatsache, dass der Compiler bestätigt, dass alle möglichen Fälle behandelt werden.

Denken Sie sich einen `match`-Ausdruck wie eine Münzsortieranlage: Münzen gleiten entlang einer Schiene mit verschieden großen Löchern, und jede Münze fällt durch das erste Loch, das sie passt. Auf die gleiche Weise gehen Werte durch jedes Muster in einem `match`, und bei dem ersten Muster, das der Wert "passt", fällt der Wert in den zugehörigen Codeblock, um während der Ausführung verwendet zu werden.

Reden wir von Münzen, lassen Sie uns sie als Beispiel mit `match` verwenden! Wir können eine Funktion schreiben, die eine unbekannte US-Münze annimmt und, ähnlich wie die Zählmaschine, bestimmt, welche Münze es ist und ihren Wert in Cent zurückgibt, wie in Listing 6-3 gezeigt.

```rust
1 enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
  2 match coin {
      3 Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

Listing 6-3: Ein Enum und ein `match`-Ausdruck, der die Varianten des Enums als Muster verwendet

Zerlegen wir das `match` in der `value_in_cents`-Funktion. Zunächst listieren wir das `match`-Schlüsselwort, gefolgt von einem Ausdruck, der in diesem Fall der Wert `coin` ist \[2\]. Dies sieht sehr ähnlich aus wie ein Ausdruck, der mit `if` verwendet wird, aber es gibt einen großen Unterschied: mit `if` muss der Ausdruck einen booleschen Wert zurückgeben, hier kann er jedoch jeden beliebigen Typ zurückgeben. Der Typ von `coin` in diesem Beispiel ist das `Coin`-Enum, das wir bei \[1\] definiert haben.

Als nächstes kommen die `match`-Arme. Ein Arm hat zwei Teile: ein Muster und etwas Code. Der erste Arm hier hat ein Muster, das der Wert `Coin::Penny` ist, und dann den `=>`-Operator, der das Muster und den auszuführenden Code trennt \[3\]. Der Code in diesem Fall ist einfach der Wert `1`. Jeder Arm wird von dem nächsten mit einem Komma getrennt.

Wenn der `match`-Ausdruck ausgeführt wird, wird der resultierende Wert nacheinander mit dem Muster jedes Arms verglichen. Wenn ein Muster mit dem Wert übereinstimmt, wird der zu diesem Muster gehörende Code ausgeführt. Wenn das Muster nicht mit dem Wert übereinstimmt, wird die Ausführung zum nächsten Arm fortgesetzt, ähnlich wie in einer Münzsortieranlage. Wir können so viele Arme wie wir benötigen haben: in Listing 6-3 hat unser `match` vier Arme.

Der mit jedem Arm assoziierte Code ist ein Ausdruck, und der resultierende Wert des Ausdrucks im passenden Arm ist der Wert, der für den gesamten `match`-Ausdruck zurückgegeben wird.

Wir verwenden normalerweise keine geschweiften Klammern, wenn der `match`-Arm-Code kurz ist, wie in Listing 6-3, wo jeder Arm einfach einen Wert zurückgibt. Wenn Sie in einem `match`-Arm mehrere Zeilen Code ausführen möchten, müssen Sie geschweifte Klammern verwenden, und das Komma nach dem Arm ist dann optional. Beispielsweise druckt der folgende Code "Glückspfennig!" jedes Mal, wenn die Methode mit einem `Coin::Penny` aufgerufen wird, gibt aber immer noch den letzten Wert des Blocks, `1`, zurück:

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```
