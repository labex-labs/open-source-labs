# Cargo como convención

Con proyectos simples, Cargo no ofrece mucha más ventaja que simplemente usar `rustc`, pero demostrará su valor a medida que tus programas se vuelvan más complejos. Una vez que los programas crecen a múltiples archivos o necesitan una dependencia, es mucho más fácil dejar que Cargo coordine la compilación.

Aunque el proyecto `hello_cargo` es simple, ahora utiliza gran parte de la herramienta real que usarás en el resto de tu carrera de Rust. De hecho, para trabajar en cualquier proyecto existente, puedes usar los siguientes comandos para descargar el código usando Git, cambiar al directorio de ese proyecto y compilar:

```bash
git clone example.org/someproject
cd someproject
cargo build
```

Para obtener más información sobre Cargo, consulta su documentación en *https://doc.rust-lang.org/cargo*.
