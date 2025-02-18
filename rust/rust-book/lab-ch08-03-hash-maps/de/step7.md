# Hinzufügen eines Schlüssels und Werts nur, wenn der Schlüssel noch nicht vorhanden ist

Es ist üblich, zu prüfen, ob ein bestimmter Schlüssel bereits in der Hash-Tabelle mit einem Wert existiert, und dann folgende Aktionen auszuführen: Wenn der Schlüssel in der Hash-Tabelle existiert, sollte der vorhandene Wert unverändert bleiben; wenn der Schlüssel nicht existiert, soll er und ein zugehöriger Wert eingefügt werden.

Hash-Tabellen haben für diesen Zweck eine spezielle API namens `entry`, die den Schlüssel, den Sie prüfen möchten, als Parameter nimmt. Der Rückgabewert der `entry`-Methode ist ein Enum namens `Entry`, das einen Wert darstellt, der existieren kann oder auch nicht. Nehmen wir an, wir möchten prüfen, ob der Schlüssel für die Yellow-Mannschaft einen zugehörigen Wert hat. Wenn nicht, möchten wir den Wert `50` einfügen, und dasselbe für die Blue-Mannschaft. Mit der `entry`-API sieht der Code wie in Listing 8-24 aus.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);

scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);

println!("{:?}", scores);
```

Listing 8-24: Verwenden der `entry`-Methode, um nur einzufügen, wenn der Schlüssel noch keinen Wert hat

Die `or_insert`-Methode auf `Entry` ist so definiert, dass sie eine veränderliche Referenz auf den Wert für den entsprechenden `Entry`-Schlüssel zurückgibt, wenn dieser Schlüssel existiert. Wenn nicht, wird der Parameter als neuer Wert für diesen Schlüssel eingefügt, und es wird eine veränderliche Referenz auf den neuen Wert zurückgegeben. Diese Technik ist viel sauberer als das Schreiben der Logik selbst und spielt außerdem besser mit dem Borrow-Checker zusammen.

Das Ausführen des Codes in Listing 8-24 wird `{"Yellow": 50, "Blue": 10}` ausgeben. Der erste Aufruf von `entry` wird den Schlüssel für die Yellow-Mannschaft mit dem Wert `50` einfügen, da die Yellow-Mannschaft noch keinen Wert hat. Der zweite Aufruf von `entry` wird die Hash-Tabelle nicht ändern, da die Blue-Mannschaft bereits den Wert `10` hat.
