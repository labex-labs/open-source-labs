# Zusätzliche bedingte Anweisungen mit Match Guards

Ein _Match Guard_ ist eine zusätzliche `if`-Bedingung, die nach dem Muster in einem `match`-Arm angegeben wird und die ebenfalls zutreffen muss, damit dieser Arm ausgewählt wird. Match Guards sind hilfreich, um komplexere Konzepte auszudrücken, als dies allein ein Muster erlaubt.

Die Bedingung kann Variablen verwenden, die im Muster erstellt werden. Listing 18-26 zeigt ein `match`, bei dem der erste Arm das Muster `Some(x)` hat und auch einen Match Guard von `if x % 2 == 0` (was `true` ist, wenn die Zahl gerade ist).

Dateiname: `src/main.rs`

```rust
let num = Some(4);

match num {
    Some(x) if x % 2 == 0 => println!("Die Zahl {x} ist gerade"),
    Some(x) => println!("Die Zahl {x} ist ungerade"),
    None => (),
}
```

Listing 18-26: Hinzufügen eines Match Guards zu einem Muster

Dieses Beispiel wird `Die Zahl 4 ist gerade` ausgeben. Wenn `num` mit dem Muster im ersten Arm verglichen wird, stimmt es überein, weil `Some(4)` mit `Some(x)` übereinstimmt. Anschließend überprüft der Match Guard, ob der Rest bei der Division von `x` durch 2 gleich 0 ist, und da dies der Fall ist, wird der erste Arm ausgewählt.

Wenn `num` stattdessen `Some(5)` gewesen wäre, wäre der Match Guard im ersten Arm `false` gewesen, weil der Rest bei der Division von 5 durch 2 1 ist, was nicht gleich 0 ist. Rust würde dann zum zweiten Arm gehen, der übereinstimmen würde, weil der zweite Arm keinen Match Guard hat und daher jeder `Some`-Variante entspricht.

Es gibt keine Möglichkeit, die Bedingung `if x % 2 == 0` innerhalb eines Musters auszudrücken, daher ermöglicht uns der Match Guard, diese Logik auszudrücken. Der Nachteil dieser zusätzlichen Ausdrucksfähigkeit ist, dass der Compiler nicht versucht, die Vollständigkeit zu überprüfen, wenn Match Guard-Ausdrücke beteiligt sind.

In Listing 18-11 haben wir erwähnt, dass wir Match Guards verwenden können, um unser Pattern-Shadowing-Problem zu lösen. Erinnern Sie sich, dass wir eine neue Variable innerhalb des Musters im `match`-Ausdruck erstellt haben, anstatt die Variable außerhalb des `match` zu verwenden. Diese neue Variable bedeutete, dass wir nicht gegen den Wert der äußeren Variable testen konnten. Listing 18-27 zeigt, wie wir einen Match Guard verwenden können, um dieses Problem zu beheben.

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = Some(5);
    let y = 10;

    match x {
        Some(50) => println!("Got 50"),
        Some(n) if n == y => println!("Matched, n = {n}"),
        _ => println!("Default case, x = {:?}", x),
    }

    println!("at the end: x = {:?}, y = {y}", x);
}
```

Listing 18-27: Verwenden eines Match Guards, um auf Gleichheit mit einer äußeren Variable zu testen

Dieser Code wird jetzt `Default case, x = Some(5)` ausgeben. Das Muster im zweiten `match`-Arm führt keine neue Variable `y` ein, die die äußere `y` überdecken würde, was bedeutet, dass wir die äußere `y` im Match Guard verwenden können. Anstatt das Muster als `Some(y)` anzugeben, was die äußere `y` überdecken würde, geben wir `Some(n)` an. Dies erstellt eine neue Variable `n`, die nichts überdeckt, da es keine `n`-Variable außerhalb des `match` gibt.

Der Match Guard `if n == y` ist kein Muster und führt daher keine neuen Variablen ein. Diese `y` _ist_ die äußere `y`, statt eine neue überdeckte `y`, und wir können nach einem Wert suchen, der denselben Wert wie die äußere `y` hat, indem wir `n` mit `y` vergleichen.

Sie können auch den _oder_-Operator `|` in einem Match Guard verwenden, um mehrere Muster anzugeben; die Match Guard-Bedingung wird auf alle Muster angewandt. Listing 18-28 zeigt die Priorität, wenn ein Muster, das `|` verwendet, mit einem Match Guard kombiniert wird. Der wichtigste Teil dieses Beispiels ist, dass der `if y`-Match Guard auf `4`, `5` _und_ `6` anwendet, obwohl es so aussehen könnte, als würde `if y` nur auf `6` angewandt werden.

Dateiname: `src/main.rs`

```rust
let x = 4;
let y = false;

match x {
    4 | 5 | 6 if y => println!("yes"),
    _ => println!("no"),
}
```

Listing 18-28: Kombinieren mehrerer Muster mit einem Match Guard

Die Match-Bedingung besagt, dass der Arm nur dann übereinstimmt, wenn der Wert von `x` gleich `4`, `5` oder `6` ist _und_ wenn `y` `true` ist. Wenn dieser Code ausgeführt wird, stimmt das Muster des ersten Arms überein, weil `x` `4` ist, aber der Match Guard `if y` ist `false`, daher wird der erste Arm nicht ausgewählt. Der Code springt zum zweiten Arm, der übereinstimmt, und dieses Programm gibt `no` aus. Der Grund ist, dass die `if`-Bedingung auf das gesamte Muster `4 | 5 | 6` anwendet, nicht nur auf den letzten Wert `6`. Mit anderen Worten, die Priorität eines Match Guards im Bezug auf ein Muster verhält sich so:

```rust
(4 | 5 | 6) if y =>...
```

statt so:

```rust
4 | 5 | (6 if y) =>...
```

Nachdem der Code ausgeführt wurde, ist das Prioritätsverhalten offensichtlich: Wenn der Match Guard nur auf den letzten Wert in der Liste von Werten, die mit dem `|`-Operator angegeben werden, angewendet würde, wäre der Arm übereingestimmt und das Programm hätte `yes` ausgegeben.
