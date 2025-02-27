# @-Bindungen

Der _at_-Operator `@` ermöglicht es uns, eine Variable zu erstellen, die einen Wert speichert, während wir diesen Wert auf einen Muster-Vergleich testen. In Listing 18-29 möchten wir testen, ob das `id`-Feld eines `Message::Hello` im Bereich `3..=7` liegt. Wir möchten auch den Wert an die Variable `id_variable` binden, damit wir ihn im mit dem Arm assoziierten Code verwenden können. Wir könnten diese Variable `id` nennen, wie das Feld, aber für dieses Beispiel verwenden wir einen anderen Namen.

Dateiname: `src/main.rs`

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_variable @ 3..=7,
    } => println!("Gefunden eine ID im Bereich: {id_variable}"),
    Message::Hello { id: 10..=12 } => {
        println!("Gefunden eine ID in einem anderen Bereich")
    }
    Message::Hello { id } => println!("Eine andere ID: {id}"),
}
```

Listing 18-29: Verwenden von `@` zum Binden an einen Wert in einem Muster und zum Testen desselben

Dieses Beispiel wird `Gefunden eine ID im Bereich: 5` ausgeben. Indem wir `id_variable @` vor dem Bereich `3..=7` angeben, fangen wir den Wert ein, der dem Bereich entspricht, und testen gleichzeitig, ob der Wert dem Bereichsmuster entspricht.

Im zweiten Arm, wo wir nur einen Bereich im Muster angegeben haben, hat der mit dem Arm assoziierte Code keine Variable, die den tatsächlichen Wert des `id`-Felds enthält. Der Wert des `id`-Felds könnte 10, 11 oder 12 sein, aber der Code, der mit diesem Muster zusammenhängt, weiß nicht, welcher Wert es ist. Der Muster-Code kann den Wert aus dem `id`-Feld nicht verwenden, weil wir den `id`-Wert nicht in einer Variable gespeichert haben.

Im letzten Arm, wo wir eine Variable ohne Bereich angegeben haben, haben wir den Wert in der Variable `id` im Code des Arms zur Verfügung. Der Grund ist, dass wir die Kurzschreibweise für Strukturfelder verwendet haben. Aber wir haben in diesem Arm keinen Test auf den Wert im `id`-Feld durchgeführt, wie wir es in den ersten beiden Armen getan haben: jeder Wert würde diesem Muster entsprechen.

Das Verwenden von `@` ermöglicht es uns, einen Wert zu testen und ihn in einer Variable innerhalb eines Musters zu speichern.
