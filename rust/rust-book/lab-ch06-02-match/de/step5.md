# Allfälle-Muster und das \_ Platzhalter

Mit Enums können wir auch spezielle Aktionen für einige bestimmte Werte durchführen, aber für alle anderen Werte eine Standardaktion ausführen. Stellen Sie sich vor, dass wir ein Spiel implementieren, bei dem, wenn Sie bei einem Würfelwurf eine 3 werfen, Ihr Spieler nicht bewegt wird, sondern stattdessen einen neuen fancy Hut bekommt. Wenn Sie eine 7 werfen, verliert Ihr Spieler einen fancy Hut. Für alle anderen Werte bewegt sich Ihr Spieler um die entsprechende Anzahl von Feldern auf der Spielfläche. Hier ist ein `match`, das diese Logik implementiert, wobei das Ergebnis des Würfelwurfs hartcodiert ist, anstatt ein zufälliger Wert, und alle anderen Logiken durch Funktionen ohne Körper dargestellt werden, da deren tatsächliche Implementierung für dieses Beispiel außerhalb des Rahmens liegt:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
  1 other => move_player(other),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn move_player(num_spaces: u8) {}
```

Für die ersten beiden Arme sind die Muster die Literalwerte `3` und `7`. Für den letzten Arm, der alle anderen möglichen Werte abdeckt, ist das Muster die Variable, die wir `other` genannt haben \[1\]. Der Code, der für den `other`-Arm ausgeführt wird, verwendet die Variable, indem er sie der `move_player`-Funktion übergibt.

Dieser Code kompiliert, obwohl wir nicht alle möglichen Werte aufgelistet haben, die ein `u8` haben kann, weil das letzte Muster alle Werte abdecken wird, die nicht speziell aufgelistet sind. Dieses Allfälle-Muster erfüllt die Anforderung, dass `match` erschöpfend sein muss. Beachten Sie, dass wir den Allfälle-Arm am Ende platzieren müssen, da die Muster in Reihenfolge ausgewertet werden. Wenn wir den Allfälle-Arm früher platzieren würden, würden die anderen Arme niemals ausgeführt werden, daher wird uns Rust warnen, wenn wir Arme nach einem Allfälle-Arm hinzufügen!

Rust hat auch ein Muster, das wir verwenden können, wenn wir einen Allfälle-Arm möchten, aber den Wert im Allfälle-Muster nicht _verwenden_ möchten: `_` ist ein spezielles Muster, das jedem Wert entspricht und nicht an diesen Wert gebunden wird. Dies sagt Rust aus, dass wir den Wert nicht verwenden werden, sodass Rust uns nicht wegen einer nicht verwendeten Variable warnen wird.

Ändern wir die Spielregeln: Wenn Sie jetzt etwas anderes als eine 3 oder eine 7 werfen, müssen Sie erneut werfen. Wir brauchen den Allfälle-Wert nicht mehr, daher können wir unseren Code ändern, um `_` statt der Variablen `other` zu verwenden:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn reroll() {}
```

Dieses Beispiel erfüllt auch die Erschöpfendkeitsanforderung, da wir in letzterem Arm explizit alle anderen Werte ignorieren; wir haben nichts vergessen.

Schließlich ändern wir die Spielregeln noch einmal, sodass nichts weiter passiert, wenn Sie etwas anderes als eine 3 oder eine 7 werfen. Wir können das ausdrücken, indem wir den Einheitswert (der leere Tupeltyp, den wir in "Der Tupeltyp" erwähnt haben) als Code verwenden, der mit dem `_`-Arm zusammenhängt:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
```

Hier sagen wir Rust explizit aus, dass wir keinen anderen Wert verwenden werden, der nicht mit einem Muster in einem früheren Arm übereinstimmt, und dass wir in diesem Fall keinen Code ausführen möchten.

Es gibt noch mehr zu Mustern und Matching, das wir in Kapitel 18 behandeln werden. Für jetzt werden wir zur `if let`-Syntax übergehen, die in Situationen nützlich sein kann, in denen der `match`-Ausdruck etwas umständlich ist.
