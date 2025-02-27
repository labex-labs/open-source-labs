# Wenn ein Vektor fallen gelassen wird, fallen auch seine Elemente

Wie jede andere `struct` wird ein Vektor freigegeben, wenn er außerhalb seines Gültigkeitsbereichs tritt, wie in Listing 8-10 annotiert.

```rust
{
    let v = vec![1, 2, 3, 4];

    // mache etwas mit v
} // <- v tritt außerhalb seines Gültigkeitsbereichs und wird hier freigegeben
```

Listing 8-10: Zeigt, wo der Vektor und seine Elemente fallen gelassen werden

Wenn der Vektor fallen gelassen wird, werden auch alle seine Inhalte fallen gelassen, was bedeutet, dass die ganzen Zahlen, die er enthält, bereinigt werden. Der Entleihensprüfer stellt sicher, dass alle Referenzen auf die Inhalte eines Vektors nur während der Gültigkeit des Vektors selbst verwendet werden.

Lassen Sie uns nun zum nächsten Sammlungstyp übergehen: `String`!
