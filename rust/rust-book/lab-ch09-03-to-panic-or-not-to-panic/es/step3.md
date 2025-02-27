# Casos en los que tienes más información que el compilador

También sería adecuado llamar a `unwrap` o `expect` cuando tienes alguna otra lógica que asegure que el `Result` tendrá un valor `Ok`, pero la lógica no es algo que el compilador entienda. Todavía tendrás un valor `Result` que debes manejar: cualquier operación que estés llamando todavía tiene la posibilidad de fallar en general, aunque sea lógicamente imposible en tu situación particular. Si puedes asegurar mediante la inspección manual del código que nunca tendrás una variante `Err`, es perfectamente aceptable llamar a `unwrap`, y aún mejor documentar la razón por la que crees que nunca tendrás una variante `Err` en el texto de `expect`. Aquí hay un ejemplo:

```rust
use std::net::IpAddr;

let home: IpAddr = "127.0.0.1"
 .parse()
 .expect("La dirección IP codificada en el código debe ser válida");
```

Estamos creando una instancia de `IpAddr` al analizar una cadena codificada en el código. Podemos ver que `127.0.0.1` es una dirección IP válida, por lo que es aceptable usar `expect` aquí. Sin embargo, tener una cadena codificada y válida no cambia el tipo de retorno del método `parse`: todavía obtenemos un valor `Result`, y el compilador todavía nos hará manejar el `Result` como si la variante `Err` fuera una posibilidad porque el compilador no es lo suficientemente inteligente para ver que esta cadena siempre es una dirección IP válida. Si la cadena de la dirección IP provenía de un usuario en lugar de estar codificada en el programa y, por lo tanto, _tuvo_ una posibilidad de fallar, definitivamente querríamos manejar el `Result` de una manera más robusta en lugar de eso. Mencionar la suposición de que esta dirección IP está codificada en el código nos hará cambiar `expect` a un código de manejo de errores mejor si, en el futuro, necesitamos obtener la dirección IP de alguna otra fuente en lugar de eso.
