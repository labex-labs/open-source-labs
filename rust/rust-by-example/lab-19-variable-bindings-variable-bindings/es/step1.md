# Enlaces de variables

Rust proporciona seguridad de tipos a través de la tipificación estática. Los enlaces de variables se pueden anotar por tipo al declararlos. Sin embargo, en la mayoría de los casos, el compilador será capaz de inferir el tipo de la variable a partir del contexto, lo que reduce significativamente la carga de anotación.

Los valores (como literales) se pueden enlazar a variables, utilizando el enlace `let`.

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // copia `an_integer` en `copied_integer`
    let copied_integer = an_integer;

    println!("Un entero: {:?}", copied_integer);
    println!("Un booleano: {:?}", a_boolean);
    println!("Conozca el valor unitario: {:?}", unit);

    // El compilador advierte sobre enlaces de variables no utilizados; estas advertencias se pueden
    // silenciar prefijando el nombre de la variable con un subrayado
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;
    // FIXME ^ Prefija con un subrayado para suprimir la advertencia
    // Tenga en cuenta que las advertencias pueden no aparecer en un navegador
}
```
