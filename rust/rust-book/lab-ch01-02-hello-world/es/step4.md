# Anatomía de un programa Rust

Revisemos en detalle este programa "¡Hola, mundo!". Aquí está la primera pieza del rompecabezas:

```rust
fn main() {

}
```

Estas líneas definen una función llamada `main`. La función `main` es especial: siempre es el primer código que se ejecuta en cada programa ejecutable de Rust. Aquí, la primera línea declara una función llamada `main` que no tiene parámetros y no devuelve nada. Si hubiera parámetros, irían dentro de los paréntesis `()`.

El cuerpo de la función está envuelto en `{}`. Rust requiere llaves alrededor de todos los cuerpos de función. Es buena práctica colocar la llave de apertura en la misma línea que la declaración de la función, agregando un espacio entre ellas.

> Nota: Si quieres adherirte a un estilo estándar en todos los proyectos de Rust, puedes usar una herramienta de formato automático llamada `rustfmt` para formatear tu código en un estilo particular (más sobre `rustfmt` en el Apéndice D). El equipo de Rust ha incluido esta herramienta con la distribución estándar de Rust, al igual que `rustc`, por lo que ya debería estar instalada en tu computadora.

El cuerpo de la función `main` contiene el siguiente código:

```rust
    println!("Hello, world!");
```

Esta línea hace todo el trabajo en este pequeño programa: imprime texto en la pantalla. Hay cuatro detalles importantes de los que hacer notar aquí.

Primero, el estilo de Rust es indentar con cuatro espacios, no una tabulación.

Segundo, `println!` llama a una macro de Rust. Si hubiera llamado a una función en lugar de eso, se escribiría como `println` (sin el `!`). Discutiremos las macros de Rust con más detalle en el Capítulo 19. Por ahora, solo necesitas saber que usar un `!` significa que estás llamando a una macro en lugar de una función normal y que las macros no siempre siguen las mismas reglas que las funciones.

Tercero, se ve la cadena `"Hello, world!"`. Pasamos esta cadena como argumento a `println!`, y la cadena se imprime en la pantalla.

Cuarto, terminamos la línea con un punto y coma (`;`), lo que indica que esta expresión ha terminado y que la siguiente está lista para comenzar. La mayoría de las líneas de código de Rust terminan con un punto y coma.
