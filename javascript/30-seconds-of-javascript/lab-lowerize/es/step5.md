# Creando un módulo reutilizable

Ahora que tenemos funciones que funcionan, creemos un archivo de módulo de JavaScript reutilizable que podamos importar en otros proyectos.

Primero, salgamos de la shell interactiva de Node.js presionando Ctrl+C dos veces o escribiendo `.exit` y presionando Enter.

Ahora, creemos un nuevo archivo llamado `object-utils.js` en el directorio del proyecto:

1. En el WebIDE, navega al panel del explorador de archivos a la izquierda.
2. Haz clic derecho en el directorio del proyecto y selecciona "Nuevo archivo".
3. Nombrar el archivo `object-utils.js`.
4. Agrega el siguiente código al archivo:

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

Ahora, creemos un archivo de prueba para verificar que nuestro módulo funcione correctamente. Crea un nuevo archivo llamado `test.js`:

1. En el WebIDE, navega al panel del explorador de archivos a la izquierda.
2. Haz clic derecho en el directorio del proyecto y selecciona "Nuevo archivo".
3. Nombrar el archivo `test.js`.
4. Agrega el siguiente código al archivo:

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

Ahora, ejecutemos el archivo de prueba:

```bash
node test.js
```

Deberías ver una salida similar a:

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

¡Felicidades! Has creado con éxito un módulo de JavaScript reutilizable con funciones para convertir las claves de un objeto a minúsculas. Ahora este módulo se puede importar en cualquiera de tus proyectos de JavaScript.
