# Introducción

Bienvenido a **Ciclos de Referencia Pueden Deslevar Memoria**. Esta práctica es parte del [Libro de Rust](https://doc.rust-lang.org/book/). Puedes practicar tus habilidades de Rust en LabEx.

En esta práctica, exploraremos cómo las garantías de seguridad de memoria de Rust hacen difícil pero no imposible accidentalmente crear fugas de memoria, específicamente cuando se utilizan `Rc<T>` y `RefCell<T>` lo que puede resultar en ciclos de referencia que impiden que los valores se eliminen y, por lo tanto, desleven memoria.
