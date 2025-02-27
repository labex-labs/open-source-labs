# Verwendung von `Box<T>` wie einer Referenz

Wir können den Code in Listing 15-6 umschreiben, um `Box<T>` statt einer Referenz zu verwenden; der Dereferenzierungsoperator, der auf der `Box<T>` in Listing 15-7 verwendet wird, funktioniert auf die gleiche Weise wie der Dereferenzierungsoperator, der auf der Referenz in Listing 15-6 verwendet wird.

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = 5;
  1 let y = Box::new(x);

    assert_eq!(5, x);
  2 assert_eq!(5, *y);
}
```

Listing 15-7: Verwendung des Dereferenzierungsoperators auf einer `Box<i32>`

Der Hauptunterschied zwischen Listing 15-7 und Listing 15-6 besteht darin, dass wir hier `y` als eine Instanz einer Box setzen, die auf einen kopierten Wert von `x` zeigt, anstatt als eine Referenz, die auf den Wert von `x` zeigt \[1\]. In der letzten Prüfung \[2\] können wir den Dereferenzierungsoperator verwenden, um der Box auf den Zeiger zu folgen, genauso wie wir es getan haben, als `y` eine Referenz war. Als nächstes werden wir untersuchen, was an `Box<T>` besonders ist, das es uns ermöglicht, den Dereferenzierungsoperator zu verwenden, indem wir unseren eigenen Box-Typ definieren.
