# Introducción

En este laboratorio, exploramos la sobrecarga de operadores en Rust y cómo se puede lograr a través de traits. Los operadores en Rust se pueden sobrecargar utilizando traits, lo que les permite realizar diferentes tareas según sus argumentos de entrada. El operador `+`, por ejemplo, es azúcar sintáctico para el método `add` y puede ser utilizado por cualquier implementador del trait `Add`. Los traits que sobrecargan operadores, incluyendo `Add`, se pueden encontrar en `core::ops`. El código Rust proporcionado demuestra cómo sobrecargar el operador `+` para los tipos personalizados `Foo` y `Bar`, lo que resulta en tipos de salida diferentes `FooBar` y `BarFoo` respectivamente.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
