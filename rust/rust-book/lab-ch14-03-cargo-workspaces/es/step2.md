# Creación de un espacio de trabajo

Un _espacio de trabajo_ es un conjunto de paquetes que comparten el mismo _Cargo.lock_ y directorio de salida. Vamos a crear un proyecto usando un espacio de trabajo: usaremos código trivial para que podamos concentrar nuestra atención en la estructura del espacio de trabajo. Hay múltiples maneras de estructurar un espacio de trabajo, así que solo mostraremos una forma común. Tendremos un espacio de trabajo que contendrá un binario y dos bibliotecas. El binario, que proporcionará la funcionalidad principal, dependerá de las dos bibliotecas. Una biblioteca proporcionará una función `add_one` y la otra biblioteca una función `add_two`. Estos tres crates formarán parte del mismo espacio de trabajo. Comenzaremos creando un nuevo directorio para el espacio de trabajo:

```bash
mkdir add
cd add
```

A continuación, en el directorio `add`, creamos el archivo `Cargo.toml` que configurará todo el espacio de trabajo. Este archivo no tendrá una sección `[package]`. En su lugar, comenzará con una sección `[workspace]` que nos permitirá agregar miembros al espacio de trabajo especificando la ruta al paquete con nuestro crate binario; en este caso, esa ruta es _adder_:

Nombre del archivo: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

Luego, crearemos el crate binario `adder` ejecutando `cargo new` dentro del directorio `add`:

```bash
$ cargo new adder
     Creado el paquete binario (aplicación) `adder`
```

En este momento, podemos compilar el espacio de trabajo ejecutando `cargo build`. Los archivos en su directorio `add` deberían verse así:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

El espacio de trabajo tiene un directorio `target` en el nivel superior donde se colocarán los artefactos compilados; el paquete `adder` no tiene su propio directorio `target`. Incluso si ejecutáramos `cargo build` desde dentro del directorio `adder`, los artefactos compilados todavía terminarían en _add/target_ en lugar de `add/adder/target`. Cargo estructura el directorio `target` en un espacio de trabajo de esta manera porque los crates en un espacio de trabajo están destinados a depender unos de otros. Si cada crate tuviera su propio directorio `target`, cada crate tendría que recompilar cada uno de los otros crates en el espacio de trabajo para colocar los artefactos en su propio directorio `target`. Al compartir un solo directorio `target`, los crates pueden evitar la recompilación innecesaria.
