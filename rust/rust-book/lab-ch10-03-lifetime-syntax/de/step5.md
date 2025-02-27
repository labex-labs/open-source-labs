# Lifetime Annotation Syntax

Lebenszeitannotationen ändern nicht, wie lange die einzelnen Referenzen existieren. Stattdessen beschreiben sie die Beziehungen zwischen den Lebenszeiten mehrerer Referenzen zueinander, ohne die Lebenszeiten zu beeinflussen. Genauso wie Funktionen beliebige Typen akzeptieren können, wenn die Signatur einen generischen Typparameter angibt, können Funktionen auch Referenzen mit jeder Lebenszeit akzeptieren, indem sie einen generischen Lebenszeitparameter angeben.

Lebenszeitannotationen haben eine etwas ungewöhnliche Syntax: Die Namen von Lebenszeitparametern müssen mit einem Apostroph (`'`) beginnen und sind normalerweise alle in Kleinbuchstaben und sehr kurz, ähnlich wie generische Typen. Die meisten Leute verwenden den Namen `'a` für die erste Lebenszeitannotation. Wir platzieren die Lebenszeitparameterannotationen nach dem `&` einer Referenz, wobei ein Leerzeichen zwischen der Annotation und dem Typ der Referenz platziert wird.

Hier sind einige Beispiele: Eine Referenz auf einen `i32` ohne Lebenszeitparameter, eine Referenz auf einen `i32`, der einen Lebenszeitparameter namens `'a` hat, und eine mutable Referenz auf einen `i32`, die ebenfalls die Lebenszeit `'a` hat.

```rust
&i32        // eine Referenz
&'a i32     // eine Referenz mit expliziter Lebenszeit
&'a mut i32 // eine mutable Referenz mit expliziter Lebenszeit
```

Eine Lebenszeitannotation alleine hat nicht viel Bedeutung, da die Annotations dazu dienen sollen, Rust zu sagen, wie die generischen Lebenszeitparameter mehrerer Referenzen zueinander zusammenhängen. Betrachten wir, wie die Lebenszeitannotationen in Bezug aufeinander im Kontext der `longest`-Funktion stehen.
