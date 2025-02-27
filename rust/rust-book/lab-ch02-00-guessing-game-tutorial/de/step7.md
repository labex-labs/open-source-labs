# Ausgabe von Werten mit println! Platzhaltern

Abgesehen von der schließenden geschweiften Klammer gibt es bisher nur noch eine Zeile im Code, die wir besprechen müssen:

```rust
println!("You guessed: {guess}");
```

Diese Zeile druckt die Zeichenfolge aus, die jetzt die Benutzer-Eingabe enthält. Die geschweiften Klammern `{}` sind ein Platzhalter: denken Sie an `{}` wie an kleine Krabbenklauen, die einen Wert an einem bestimmten Ort halten. Wenn Sie den Wert einer Variable ausgeben möchten, kann der Variablenname innerhalb der geschweiften Klammern stehen. Wenn Sie das Ergebnis der Auswertung eines Ausdrucks ausgeben möchten, legen Sie leere geschweifte Klammern im Formatstring an, und folgen Sie dann den Formatstring mit einer komma-getrennten Liste von Ausdrücken, die in jeder leeren geschweiften Klammer-Platzhalter in derselben Reihenfolge ausgegeben werden sollen. Ein Aufruf von `println!`, um eine Variable und das Ergebnis eines Ausdrucks auszugeben, würde so aussehen:

```rust
let x = 5;
let y = 10;

println!("x = {x} and y + 2 = {}", y + 2);
```

Dieser Code würde ausgeben: `x = 5 and y = 12`.
