# Preventing Dangling References with Lifetimes

Das Hauptziel von Lebenszeiten ist es, _dangling references_ (verhängende Referenzen) zu vermeiden, die dazu führen, dass ein Programm auf Daten verweist, die nicht die Daten sind, auf die es verweisen soll. Betrachten Sie das Programm in Listing 10-16, das einen äußeren und einen inneren Bereich hat.

```rust
fn main() {
  1 let r;

    {
      2 let x = 5;
      3 r = &x;
  4 }

  5 println!("r: {r}");
}
```

Listing 10-16: Ein Versuch, eine Referenz zu verwenden, deren Wert außer Gültigkeitsbereich ist

> Hinweis: Die Beispiele in Listing 10-16, 10-17 und 10-23 deklarieren Variablen ohne ihnen einen Anfangswert zuzuweisen, sodass der Variablennamen im äußeren Bereich existiert. Auf den ersten Blick mag dies mit Rusts fehlender Nullwerte in Konflikt stehen. Wenn wir jedoch versuchen, eine Variable zu verwenden, bevor wir ihr einen Wert zuweisen, erhalten wir einen Kompilierfehler, was zeigt, dass Rust tatsächlich keine Nullwerte zulässt.

Der äußere Bereich deklariert eine Variable namens `r` ohne Anfangswert \[1\], und der innere Bereich deklariert eine Variable namens `x` mit dem Anfangswert `5` \[2\]. Innerhalb des inneren Bereichs versuchen wir, den Wert von `r` als Referenz auf `x` zu setzen \[3\]. Dann endet der innere Bereich \[4\], und wir versuchen, den Wert in `r` auszugeben \[5\]. Dieser Code wird nicht kompilieren, weil der Wert, auf den `r` verweist, außer Gültigkeitsbereich ist, bevor wir versuchen, ihn zu verwenden. Hier ist die Fehlermeldung:

```bash
error[E0597]: `x` does not live long enough
 --> src/main.rs:6:13
  |
6 |         r = &x;
  |             ^^ borrowed value does not live long enough
7 |     }
  |     - `x` dropped here while still borrowed
8 |
9 |     println!("r: {r}");
  |                   - borrow later used here
```

Die Fehlermeldung sagt, dass die Variable `x` "nicht lange genug lebt". Der Grund ist, dass `x` außer Gültigkeitsbereich sein wird, wenn der innere Bereich am Ende der Zeile 7 endet. Aber `r` ist immer noch gültig für den äußeren Bereich; da sein Bereich größer ist, sagen wir, dass es "länger lebt". Wenn Rust diesen Code funktionieren ließe, würde `r` auf einen Speicher verweisen, der freigegeben wurde, als `x` außer Gültigkeitsbereich ging, und alles, was wir mit `r` versuchen würden, würde nicht richtig funktionieren. Wie bestimmt Rust also, dass dieser Code ungültig ist? Es verwendet einen Borrow-Checker.
