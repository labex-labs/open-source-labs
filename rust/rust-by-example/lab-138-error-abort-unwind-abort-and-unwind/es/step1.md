# `abort` y `unwind`

La sección anterior ilustra el mecanismo de manejo de errores `panic`. Diferentes caminos de código pueden ser compilados condicionalmente basados en la configuración de panic. Los valores disponibles actualmente son `unwind` y `abort`.

Basado en el ejemplo anterior de limonada, usamos explícitamente la estrategia de panic para probar diferentes líneas de código.

```rust

fn drink(beverage: &str) {
   // No deberías beber demasiadas bebidas azucaradas.
    if beverage == "lemonade" {
        if cfg!(panic="abort"){ println!("This is not your party. Run!!!!");}
        else{ println!("Spit it out!!!!");}
    }
    else{ println!("Some refreshing {} is all I need.", beverage); }
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

Aquí hay otro ejemplo que se centra en reescribir `drink()` y usar explícitamente la palabra clave `unwind`.

```rust

#[cfg(panic = "unwind")]
fn ah(){ println!("Spit it out!!!!");}

#[cfg(not(panic="unwind"))]
fn ah(){ println!("This is not your party. Run!!!!");}

fn drink(beverage: &str){
    if beverage == "lemonade"{ ah();}
    else{println!("Some refreshing {} is all I need.", beverage);}
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

La estrategia de panic se puede configurar desde la línea de comandos usando `abort` o `unwind`.

```console
rustc lemonade.rs -C panic=abort
```
