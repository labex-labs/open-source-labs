# Playground

El [Rust Playground](https://play.rust-lang.org/) es una forma de experimentar con código Rust a través de una interfaz web.

## Usándolo con `mdbook`

En `mdbook`, puede hacer que los ejemplos de código sean reproducibles y editables.

```rust
fn main() {
    println!("Hello World!");
}
```

Esto permite que el lector ejecute su muestra de código, pero también la modifique y ajuste. La clave aquí es agregar la palabra `editable` a su bloque de código separado por una coma.

````markdown
```rust
//...coloca tu código aquí
```
````

Además, puede agregar `ignore` si desea que `mdbook` omita su código cuando se construye y se prueba.

````markdown
```rust
//...coloca tu código aquí
```
````

## Usándolo con la documentación

Es posible que haya notado en algunas de las documentaciones oficiales de Rust un botón que dice "Ejecutar", que abre la muestra de código en una nueva pestaña en Rust Playground. Esta característica se habilita si utiliza el atributo #\[doc\] llamado `html_playground_url`.
