# Nur auf dem Stapel gespeicherte Daten: Copy

Es gibt noch einen Aspekt, über den wir bisher nicht gesprochen haben. Dieser Code mit ganzen Zahlen - einen Teil davon wurde in Listing 4-2 gezeigt - funktioniert und ist gültig:

```rust
let x = 5;
let y = x;

println!("x = {x}, y = {y}");
```

Aber dieser Code scheint im Widerspruch zu stehen zu dem, was wir gerade gelernt haben: Wir haben keinen Aufruf von `clone`, aber `x` ist immer noch gültig und wurde nicht in `y` verschoben.

Der Grund ist, dass Typen wie ganze Zahlen, die zur Compile-Zeit eine bekannte Größe haben, vollständig auf dem Stapel gespeichert werden, sodass Kopien der tatsächlichen Werte schnell erstellt werden können. Das bedeutet, dass es keinen Grund gibt, `x` nach der Erstellung der Variable `y` ungültig zu machen. Mit anderen Worten, es gibt keinen Unterschied zwischen einer tiefen und einer flachen Kopie hier, sodass ein Aufruf von `clone` nichts anderes tun würde als die übliche flache Kopie, und wir können ihn weglassen.

Rust hat eine spezielle Annotation namens `Copy`-Eigenschaft, die wir auf Typen platzieren können, die auf dem Stapel gespeichert werden, wie dies bei ganzen Zahlen der Fall ist (wir werden in Kapitel 10 mehr über Eigenschaften sprechen). Wenn ein Typ die `Copy`-Eigenschaft implementiert, bewegen sich Variablen, die ihn verwenden, nicht, sondern werden einfach kopiert, sodass sie nach der Zuweisung an eine andere Variable immer noch gültig sind.

Rust lässt uns keinen Typ mit `Copy` annotieren, wenn der Typ oder irgendein Teil davon die `Drop`-Eigenschaft implementiert hat. Wenn der Typ etwas besonderes erfordert, wenn der Wert außerhalb seines Gültigkeitsbereichs fällt, und wir der `Copy`-Annotation hinzufügen, erhalten wir einen Compile-Fehler. Um zu erfahren, wie Sie der `Copy`-Annotation zu Ihrem Typ hinzufügen, um die Eigenschaft zu implementieren, siehe "Ableitbare Eigenschaften".

Welche Typen implementieren die `Copy`-Eigenschaft? Sie können die Dokumentation für den jeweiligen Typ überprüfen, um sicher zu sein, aber als allgemeine Regel können alle einfachen skalaren Wertegruppen `Copy` implementieren, und nichts, was eine Zuweisung erfordert oder eine Art von Ressource ist, kann `Copy` implementieren. Hier sind einige der Typen, die `Copy` implementieren:

- Alle ganzzahligen Typen, wie `u32`.
- Der boolesche Typ, `bool`, mit den Werten `true` und `false`.
- Alle Gleitkomma-Typen, wie `f64`.
- Der Zeichensatztyp, `char`.
- Tupel, wenn sie nur aus Typen bestehen, die ebenfalls `Copy` implementieren. Beispielsweise implementiert `(i32, i32)` `Copy`, aber `(i32, String)` nicht.
