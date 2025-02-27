# Solución de problemas

Para comprobar si has instalado Rust correctamente, abre una **nueva shell** y escribe esta línea:

```bash
# Abre una nueva terminal primero!
rustc --version
```

Deberías ver el número de versión, el hash del commit y la fecha del commit de la última versión estable publicada, en el siguiente formato:

```bash
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

Si ves esta información, ¡has instalado Rust correctamente! Si no ves esta información, comprueba que Rust está en tu variable de entorno `%PATH%` de la siguiente manera.

En Linux, utiliza:

```bash
echo $PATH
```

Si todo esto es correcto y Rust todavía no funciona, hay varios lugares donde puedes obtener ayuda. Descubre cómo ponerte en contacto con otros Rustaceans (un apodo tonto que nos llamamos a nosotros mismos) en la página de la comunidad en *https://www.rust-lang.org/community*.
