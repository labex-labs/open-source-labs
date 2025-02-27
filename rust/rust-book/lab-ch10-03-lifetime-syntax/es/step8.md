# Anotaciones de lifetimes en definiciones de struct

Hasta ahora, los structs que hemos definido todos contienen tipos con propiedad. Podemos definir structs para contener referencias, pero en ese caso necesitaríamos agregar una anotación de lifetime a cada referencia en la definición del struct. La Lista 10-24 tiene un struct llamado `ImportantExcerpt` que contiene un trozo de cadena.

Nombre de archivo: `src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
       .split('.')
       .next()
       .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

Lista 10-24: Un struct que contiene una referencia, requiriendo una anotación de lifetime

Este struct tiene el único campo `part` que contiene un trozo de cadena, que es una referencia \[2\]. Al igual que con los tipos de datos genéricos, declaramos el nombre del parámetro de lifetime genérico dentro de corchetes angulares después del nombre del struct para que podamos usar el parámetro de lifetime en el cuerpo de la definición del struct \[1\]. Esta anotación significa que una instancia de `ImportantExcerpt` no puede sobrevivir a la referencia que contiene en su campo `part`.

La función `main` aquí crea una instancia del struct `ImportantExcerpt` \[5\] que contiene una referencia a la primera oración de la `String` \[4\] propiedad de la variable `novel` \[3\]. Los datos en `novel` existen antes de que se cree la instancia de `ImportantExcerpt`. Además, `novel` no sale de ámbito hasta después de que la instancia de `ImportantExcerpt` sale de ámbito, por lo que la referencia en la instancia de `ImportantExcerpt` es válida.
