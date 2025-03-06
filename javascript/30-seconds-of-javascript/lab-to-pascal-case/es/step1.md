# Comprender el Pascal Case y Configurar el Entorno

El Pascal Case es una convención de nomenclatura donde:

- La primera letra de cada palabra está en mayúsculas.
- No se utilizan espacios, guiones ni guiones bajos entre las palabras.
- Todas las demás letras están en minúsculas.

Por ejemplo:

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

Comencemos configurando nuestro entorno de desarrollo.

1. Abra la Terminal desde la interfaz de WebIDE haciendo clic en "Terminal" en la barra de menú superior.

2. Inicie una sesión interactiva de Node.js escribiendo el siguiente comando en la Terminal y presionando Enter:

```bash
node
```

Debería ver aparecer el indicador de Node.js (`>`), lo que indica que ahora está en el entorno interactivo de Node.js.

3. Intentemos una simple manipulación de cadenas de texto (strings) para calentar motores. Escriba el siguiente código en el indicador de Node.js:

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

La salida debería ser:

```
John doe
```

Este simple ejemplo demuestra cómo poner en mayúsculas la primera letra de una cadena de texto (string). Utilizamos:

- `charAt(0)` para obtener el primer carácter.
- `toUpperCase()` para convertirlo a mayúsculas.
- `slice(1)` para obtener el resto de la cadena de texto (string).
- Concatenación con `+` para combinarlos.

Estos métodos de manipulación de cadenas de texto (strings) serán útiles a medida que construyamos nuestro convertidor a Pascal Case.
