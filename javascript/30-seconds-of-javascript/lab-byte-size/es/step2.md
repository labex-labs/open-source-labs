# Usar Blob para calcular el tamaño en bytes de una cadena

Ahora que entendemos la representación de cadenas, aprendamos cómo calcular el tamaño real en bytes de una cadena utilizando el objeto `Blob`.

Un `Blob` (Objeto Binario Grande) representa un objeto similar a un archivo de datos sin procesar e inmutables. Al convertir nuestra cadena en un Blob, podemos acceder a su propiedad `size` para determinar el tamaño en bytes.

En la consola de Node.js, creemos una función para calcular el tamaño en bytes:

```javascript
const byteSize = (str) => new Blob([str]).size;
```

Esta función toma una cadena como entrada, la convierte en un Blob y devuelve su tamaño en bytes.

Probemos esta función con un ejemplo sencillo:

```javascript
byteSize("Hello World");
```

Debería ver la salida:

```
11
```

En este caso, la cantidad de caracteres y el tamaño en bytes son los mismos porque "Hello World" contiene solo caracteres ASCII, cada uno representado por un solo byte.

Ahora intentemos con un carácter no ASCII:

```javascript
byteSize("😀");
```

Debería ver la salida:

```
4
```

Esto muestra que aunque el emoji parece ser un solo carácter, en realidad ocupa 4 bytes de almacenamiento.
