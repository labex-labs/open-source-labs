# `static`

Rust tiene algunos nombres de duración de vida reservados. Uno de ellos es `'static`. Puede encontrarlo en dos situaciones:

```rust
// Una referencia con duración de vida `'static`:
let s: &'static str = "hello world";

// `'static` como parte de una restricción de trato:
fn genérico<T>(x: T) donde T: 'static {}
```

Ambas están relacionadas pero ligeramente diferentes y este es una fuente común de confusión al aprender Rust. Aquí hay algunos ejemplos para cada situación:

## Duración de vida de la referencia

Como duración de vida de una referencia, `'static` indica que los datos apuntados por la referencia viven durante toda la duración del programa en ejecución. Aún puede ser forzado a una duración de vida más corta.

Hay dos maneras de crear una variable con duración de vida `'static`, y ambas se almacenan en la memoria de solo lectura del binario:

- Crear una constante con la declaración `static`.
- Crear un literal de `string` que tiene el tipo: `&'static str`.

Vea el siguiente ejemplo para una demostración de cada método:

```rust
// Crear una constante con duración de vida `'static`.
static NUM: i32 = 18;

// Devuelve una referencia a `NUM` donde su duración de vida `'static`
// se fuerza a la del argumento de entrada.
fn forzar_estático<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // Crear un literal de `string` e imprimirlo:
        let cadena_estática = "Estoy en memoria de solo lectura";
        println!("cadena_estática: {}", cadena_estática);

        // Cuando `cadena_estática` sale del ámbito, la referencia
        // ya no se puede usar, pero los datos permanecen en el binario.
    }

    {
        // Crear un entero para usar en `forzar_estático`:
        let num_duración = 9;

        // Forzar `NUM` a la duración de vida de `num_duración`:
        let estático_forzado = forzar_estático(&num_duración);

        println!("estático_forzado: {}", estático_forzado);
    }

    println!("NUM: {} sigue siendo accesible!", NUM);
}
```

## Restricción de trato

Como una restricción de trato, significa que el tipo no contiene ninguna referencia no estática. Es decir, el receptor puede mantener el tipo durante tanto tiempo como quiera y nunca se tornará inválido hasta que lo abandone.

Es importante entender que esto significa que cualquier dato poseído siempre pasa una restricción de duración de vida `'static`, pero una referencia a ese dato poseído generalmente no:

```rust
use std::fmt::Debug;

fn imprimirlo(entrada: impl Debug + 'static) {
    println!("Valor `'static` pasado es: {:?}", entrada);
}

fn main() {
    // i es poseído y no contiene referencias, por lo tanto es `'static`:
    let i = 5;
    imprimirlo(i);

    // oops, &i solo tiene la duración de vida definida por el ámbito de
    // main(), por lo tanto no es `'static`:
    imprimirlo(&i);
}
```

El compilador le dirá:

```ignore
error[E0597]: `i` no tiene una duración de vida lo suficientemente larga
  --> src/lib.rs:15:15
   |
15 |     imprimirlo(&i);
   |     ---------^^--
   |     |         |
   |     |         el valor prestado no tiene una duración de vida lo suficientemente larga
   |     el argumento requiere que `i` sea prestado para `'static`
16 | }
   | - `i` se descarta aquí mientras todavía está prestado
```
