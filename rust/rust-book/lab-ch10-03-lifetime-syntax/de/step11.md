# The Static Lifetime

Eine besondere Lebenszeit, über die wir sprechen müssen, ist `'static`, die angibt, dass die betroffene Referenz _kann_ für die gesamte Laufzeit des Programms existieren. Alle String-Literale haben die Lebenszeit `'static`, die wir wie folgt annotieren können:

```rust
let s: &'static str = "I have a static lifetime.";
```

Der Text dieses Strings wird direkt im Binärprogramm gespeichert, das immer verfügbar ist. Daher ist die Lebenszeit aller String-Literale `'static`.

Sie können in Fehlermeldungen Vorschläge sehen, die die Lebenszeit `'static` verwenden. Bevor Sie `'static` als Lebenszeit für eine Referenz angeben, überlegen Sie sich, ob die Referenz tatsächlich die gesamte Lebenszeit Ihres Programms hat und ob Sie das möchten. In den meisten Fällen resultiert eine Fehlermeldung, die die Lebenszeit `'static` vorschlägt, aus einem Versuch, einen verhängenden Verweis zu erstellen oder aus einem Missmatch der verfügbaren Lebenszeiten. In solchen Fällen ist die Lösung, diese Probleme zu beheben, nicht die Lebenszeit `'static` anzugeben.
