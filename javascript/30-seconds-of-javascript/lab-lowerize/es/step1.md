# Comprender los objetos en JavaScript

Antes de comenzar a convertir las claves de los objetos a minúsculas, entendamos qué son los objetos de JavaScript y cómo podemos trabajar con ellos.

En JavaScript, un objeto es una colección de pares clave-valor. Las claves son cadenas de texto (o Símbolos), y los valores pueden ser de cualquier tipo de dato, incluyendo otros objetos.

Comencemos abriendo la shell interactiva de Node.js:

1. Abra la terminal en su WebIDE
2. Escriba `node` y presione Enter

Ahora debería ver el indicador de Node.js (`>`), que le permite escribir código JavaScript directamente.

Creemos un objeto simple con claves en mayúsculas y minúsculas mezcladas:

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

Escriba este código en el indicador de Node.js y presione Enter. Para ver el objeto, simplemente escriba `user` y presione Enter:

```javascript
user;
```

Debería ver la salida:

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

Como puede ver, este objeto tiene claves con diferentes estilos de capitalización. En el siguiente paso, aprenderemos cómo acceder a estas claves y convertirlas a minúsculas.
