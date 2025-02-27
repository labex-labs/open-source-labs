# Methoden mit mehr Parametern

Üben wir das Verwenden von Methoden, indem wir eine zweite Methode auf der `Rectangle`-Struktur implementieren. Diesmal möchten wir, dass eine `Rectangle`-Instanz eine andere `Rectangle`-Instanz annimmt und `true` zurückgibt, wenn das zweite `Rectangle` vollständig innerhalb von `self` (der ersten `Rectangle`-Instanz) passt; andernfalls sollte es `false` zurückgeben. Das heißt, nachdem wir die `can_hold`-Methode definiert haben, möchten wir das Programm wie in Listing 5-14 schreiben können.

Dateiname: `src/main.rs`

```rust
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

Listing 5-14: Verwenden der noch nicht implementierten `can_hold`-Methode

Die erwartete Ausgabe würde wie folgt aussehen, da beide Dimensionen von `rect2` kleiner als die Dimensionen von `rect1` sind, aber `rect3` breiter als `rect1` ist:

```rust
Can rect1 hold rect2? true
Can rect1 hold rect3? false
```

Wir wissen, dass wir eine Methode definieren möchten, daher wird sie innerhalb des `impl Rectangle`-Blocks sein. Der Methodenname wird `can_hold` sein, und er wird eine unveränderliche Referenz auf eine andere `Rectangle` als Parameter akzeptieren. Wir können den Typ des Parameters bestimmen, indem wir uns den Code ansehen, der die Methode aufruft: `rect1.can_hold(&rect2)` übergibt `&rect2`, was eine unveränderliche Referenz auf `rect2`, eine `Rectangle`-Instanz, ist. Dies ergibt Sinn, da wir nur `rect2` lesen müssen (anstatt schreiben, was bedeuten würde, dass wir eine veränderliche Referenz benötigen), und wir möchten, dass `main` die Eigentumsgewalt an `rect2` behält, damit wir sie nach dem Aufruf der `can_hold`-Methode erneut verwenden können. Der Rückgabewert von `can_hold` wird ein Boolean sein, und die Implementierung wird überprüfen, ob die Breite und Höhe von `self` größer als die Breite und Höhe der anderen `Rectangle` sind, respektive. Fügen wir die neue `can_hold`-Methode zum `impl`-Block aus Listing 5-13 hinzu, wie in Listing 5-15 gezeigt.

Dateiname: `src/main.rs`

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listing 5-15: Implementieren der `can_hold`-Methode auf `Rectangle`, die eine andere `Rectangle`-Instanz als Parameter annimmt

Wenn wir diesen Code mit der `main`-Funktion aus Listing 5-14 ausführen, erhalten wir die gewünschte Ausgabe. Methoden können mehrere Parameter akzeptieren, die wir der Signatur nach dem `self`-Parameter hinzufügen, und diese Parameter funktionieren genauso wie Parameter in Funktionen.
