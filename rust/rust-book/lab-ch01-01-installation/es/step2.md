# Instalando rustup en Linux o macOS

Si estás utilizando Linux o macOS, abre una terminal y escribe el siguiente comando:

```bash
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```

El comando descarga un script y comienza la instalación de la herramienta `rustup`, que instala la última versión estable de Rust. Es posible que se te solicite tu contraseña. Si la instalación es exitosa, aparecerá la siguiente línea:

```rust
Rust is installed now. Great!
```

También necesitarás un _enlazador_, que es un programa que Rust utiliza para unir sus salidas compiladas en un solo archivo. Es probable que ya tengas uno. Si obtienes errores de enlace, debes instalar un compilador de C, que por lo general incluirá un enlazador. Un compilador de C también es útil porque algunos paquetes comunes de Rust dependen de código C y necesitarán un compilador de C.

Los usuarios de Linux generalmente deben instalar GCC o Clang, de acuerdo con la documentación de su distribución. Por ejemplo, si utilizas Ubuntu, puedes instalar el paquete `build-essential`.
