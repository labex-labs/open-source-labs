# Agrupación de Valores de Configuración

Podemos dar otro pequeño paso para mejorar aún más la función `parse_config`. En este momento, estamos devolviendo una tupla, pero luego la rompemos inmediatamente en partes individuales nuevamente. Esto es una señal de que quizás aún no tenemos la abstracción adecuada.

Otro indicador de que hay margen para mejorar es la parte `config` de `parse_config`, lo que implica que los dos valores que devolvemos están relacionados y son parte de un solo valor de configuración. Actualmente, no estamos transmitiendo este significado en la estructura de los datos más allá de agrupar los dos valores en una tupla; en cambio, pondremos los dos valores en una estructura y daremos a cada campo de la estructura un nombre significativo. Hacer esto hará que sea más fácil para futuros mantenedores de este código entender cómo se relacionan los diferentes valores y cuál es su propósito.

La Lista 12-6 muestra las mejoras en la función `parse_config`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = parse_config(&args);

    println!("Buscando {}", 2 config.query);
    println!("En el archivo {}", 3 config.file_path);

    let contents = fs::read_to_string(4 config.file_path)
     .expect("Debería haber sido posible leer el archivo");

    --snip--
}

5 struct Config {
    query: String,
    file_path: String,
}

6 fn parse_config(args: &[String]) -> Config {
  7 let query = args[1].clone();
  8 let file_path = args[2].clone();

    Config { query, file_path }
}
```

Lista 12-6: Refactorización de `parse_config` para devolver una instancia de una estructura `Config`

Hemos agregado una estructura llamada `Config` definida para tener campos llamados `query` y `file_path` \[5\]. La firma de `parse_config` ahora indica que devuelve un valor `Config` \[6\]. En el cuerpo de `parse_config`, donde antes devolvíamos rebanadas de cadena que referenciaban valores `String` en `args`, ahora definimos `Config` para contener valores `String` propios. La variable `args` en `main` es el propietario de los valores de argumento y solo está permitiendo que la función `parse_config` los preste, lo que significa que violaríamos las reglas de préstamo de Rust si `Config` intentara tomar posesión de los valores en `args`.

Hay varias maneras en las que podríamos manejar los datos `String`; la forma más fácil, aunque algo ineficiente, es llamar al método `clone` en los valores \[7\] \[8\]. Esto hará una copia completa de los datos para que la instancia de `Config` los tenga, lo que toma más tiempo y memoria que almacenar una referencia a los datos de cadena. Sin embargo, clonar los datos también hace que nuestro código sea muy sencillo porque no tenemos que manejar los períodos de vida de las referencias; en esta circunstancia, renunciar un poco de rendimiento para ganar simplicidad es un trato rentable.

> **Los Compromisos de Usar clone**
>
> Hay una tendencia entre muchos Rustaceans a evitar usar `clone` para solucionar problemas de posesión debido a su costo en tiempo de ejecución. En el Capítulo 13, aprenderá a usar métodos más eficientes en este tipo de situaciones. Pero por ahora, está bien copiar algunas cadenas para seguir avanzando porque solo harás estas copias una vez y tu ruta de archivo y cadena de consulta son muy pequeñas. Es mejor tener un programa funcional que sea un poco ineficiente que tratar de hiperoptimizar el código en tu primera iteración. A medida que te vuelvas más experimentado con Rust, será más fácil comenzar con la solución más eficiente, pero por ahora, es perfectamente aceptable llamar a `clone`.

Hemos actualizado `main` para que coloque la instancia de `Config` devuelta por `parse_config` en una variable llamada `config` \[1\], y actualizamos el código que anteriormente usaba las variables separadas `query` y `file_path` para que ahora use los campos de la estructura `Config` en su lugar \[2\] \[3\] \[4\].

Ahora nuestro código transmite más claramente que `query` y `file_path` están relacionados y que su propósito es configurar cómo funcionará el programa. Cualquier código que use estos valores sabe que los encontrará en la instancia `config` en los campos nombrados con su propósito.
