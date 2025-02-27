# Métodos con más parámetros

Vamos a practicar el uso de métodos implementando un segundo método en el struct `Rectangle`. Esta vez queremos que una instancia de `Rectangle` tome otra instancia de `Rectangle` y devuelva `true` si el segundo `Rectangle` puede caber completamente dentro de `self` (el primer `Rectangle`); de lo contrario, debe devolver `false`. Es decir, una vez que hayamos definido el método `can_hold`, queremos poder escribir el programa mostrado en la Lista 5-14.

Nombre de archivo: `src/main.rs`

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

Lista 5-14: Usando el método `can_hold` aún no escrito

La salida esperada se vería como la siguiente porque ambas dimensiones de `rect2` son menores que las dimensiones de `rect1`, pero `rect3` es más ancha que `rect1`:

```rust
Can rect1 hold rect2? true
Can rect1 hold rect3? false
```

Sabemos que queremos definir un método, por lo que estará dentro del bloque `impl Rectangle`. El nombre del método será `can_hold`, y tomará un préstamo inmutable de otro `Rectangle` como parámetro. Podemos determinar el tipo del parámetro viendo el código que llama al método: `rect1.can_hold(&rect2)` pasa `&rect2`, que es un préstamo inmutable a `rect2`, una instancia de `Rectangle`. Esto tiene sentido porque solo necesitamos leer `rect2` (en lugar de escribir, lo que significaría que necesitaríamos un préstamo mutable), y queremos que `main` conserve la posesión de `rect2` para que podamos usarlo nuevamente después de llamar al método `can_hold`. El valor de retorno de `can_hold` será un booleano, y la implementación comprobará si el ancho y la altura de `self` son mayores que el ancho y la altura del otro `Rectangle`, respectivamente. Agreguemos el nuevo método `can_hold` al bloque `impl` de la Lista 5-13, como se muestra en la Lista 5-15.

Nombre de archivo: `src/main.rs`

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

Lista 5-15: Implementando el método `can_hold` en `Rectangle` que toma otra instancia de `Rectangle` como parámetro

Cuando ejecutamos este código con la función `main` de la Lista 5-14, obtendremos la salida deseada. Los métodos pueden tomar múltiples parámetros que agregamos a la firma después del parámetro `self`, y esos parámetros funcionan exactamente como los parámetros en las funciones.
