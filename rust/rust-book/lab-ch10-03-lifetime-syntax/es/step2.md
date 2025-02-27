# Evitando referencias colgantes con lifetimes

El principal objetivo de los lifetimes es evitar las _referencias colgantes_, que hacen que un programa refiera a datos diferentes de los datos a los que está destinado a referirse. Considere el programa de la Lista 10-16, que tiene un ámbito externo y un ámbito interno.

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

Lista 10-16: Un intento de usar una referencia cuyo valor ya ha salido de ámbito

> Nota: Los ejemplos de la Lista 10-16, 10-17 y 10-23 declaran variables sin darles un valor inicial, por lo que el nombre de la variable existe en el ámbito externo. A primera vista, esto puede parecer en conflicto con el hecho de que Rust no tiene valores nulos. Sin embargo, si intentamos usar una variable antes de darle un valor, obtendremos un error en tiempo de compilación, lo que demuestra que Rust realmente no permite valores nulos.

El ámbito externo declara una variable llamada `r` sin valor inicial \[1\], y el ámbito interno declara una variable llamada `x` con el valor inicial de `5` \[2\]. Dentro del ámbito interno, intentamos establecer el valor de `r` como una referencia a `x` \[3\]. Luego termina el ámbito interno \[4\], y intentamos imprimir el valor en `r` \[5\]. Este código no se compilará porque el valor al que `r` se refiere ya ha salido de ámbito antes de que intentemos usarlo. Aquí está el mensaje de error:

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

El mensaje de error dice que la variable `x` "no tiene vida suficiente". La razón es que `x` estará fuera de ámbito cuando termine el ámbito interno en la línea 7. Pero `r` sigue siendo válido para el ámbito externo; debido a que su ámbito es más grande, decimos que "tiene una vida más larga". Si Rust permitiera que este código funcione, `r` estaría referenciando memoria que se desasignó cuando `x` salió de ámbito, y cualquier cosa que intentemos hacer con `r` no funcionaría correctamente. Entonces, ¿cómo determina Rust que este código es inválido? Utiliza un verificador de préstamos.
