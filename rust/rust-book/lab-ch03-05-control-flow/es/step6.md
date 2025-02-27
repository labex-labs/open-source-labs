# Repitiendo Código con `loop`

La palabra clave `loop` le dice a Rust que ejecute un bloque de código una y otra vez para siempre o hasta que le digas explícitamente que pare.

Como ejemplo, cambia el archivo `src/main.rs` en tu directorio `loops` para que se vea así:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    loop {
        println!("again!");
    }
}
```

Cuando ejecutamos este programa, veremos `again!` impreso una y otra vez continuamente hasta que detengamos el programa manualmente. La mayoría de las terminales admiten el atajo de teclado ctrl-C para interrumpir un programa que está atascado en un bucle continuo. Prueba:

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.29s
     Running `target/debug/loops`
again!
again!
again!
again!
^Cagain!
```

El símbolo `^C` representa donde presionaste ctrl-C. Puede que veas o no la palabra `again!` impresa después del `^C`, dependiendo de donde estaba el código en el bucle cuando recibió la señal de interrupción.

Afortunadamente, Rust también proporciona una forma de salir de un bucle usando código. Puedes colocar la palabra clave `break` dentro del bucle para decirle al programa cuándo dejar de ejecutar el bucle. Recuerda que hicimos esto en el juego de adivinanzas en "Saliendo Después de una Adivinanza Correcta" para salir del programa cuando el usuario ganó el juego adivinando el número correcto.

También usamos `continue` en el juego de adivinanzas, que en un bucle le dice al programa que salte cualquier código restante en esta iteración del bucle y vaya a la siguiente iteración.
