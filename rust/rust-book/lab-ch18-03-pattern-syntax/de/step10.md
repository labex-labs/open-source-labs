# Strukturzerlegung von Structs und Tupeln

Wir können Strukturzerlegungsmuster noch komplexer kombinieren, miteinander kombinieren und verschachteln. Das folgende Beispiel zeigt eine komplizierte Strukturzerlegung, bei der wir Structs und Tupel in einem Tupel verschachteln und alle primitiven Werte daraus extrahieren:

```rust
let ((feet, inches), Point { x, y }) =
    ((3, 10), Point { x: 3, y: -10 });
```

Dieser Code ermöglicht es uns, komplexe Typen in ihre Bestandteile aufzuteilen, sodass wir die Werte, an denen wir interessiert sind, separat verwenden können.

Die Verwendung von Mustern bei der Strukturzerlegung ist eine bequeme Methode, um Teile von Werten, wie z.B. den Wert aus jedem Feld in einem Struct, voneinander separat zu verwenden.
