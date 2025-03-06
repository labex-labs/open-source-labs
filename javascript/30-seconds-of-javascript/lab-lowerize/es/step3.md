# Creando la función para convertir a minúsculas

Ahora que entendemos cómo acceder a las claves de un objeto y usar el método `reduce()`, creemos una función que convierta todas las claves de un objeto a minúsculas.

En la shell interactiva de Node.js, define la siguiente función:

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

Desglosemos lo que hace esta función:

1. `Object.keys(obj)` obtiene todas las claves del objeto de entrada
2. `.reduce()` transforma estas claves en un nuevo objeto
3. Para cada clave, creamos una nueva entrada en el objeto acumulador (`acc`) con:
   - La clave convertida a minúsculas usando `key.toLowerCase()`
   - El valor original del objeto de entrada (`obj[key]`)
4. Comenzamos con un objeto vacío `{}` como valor inicial para el acumulador
5. Finalmente, devolvemos el acumulador, que es nuestro nuevo objeto con claves en minúsculas

Ahora, probemos nuestra función con el objeto `user` que creamos anteriormente:

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

Deberías ver la salida:

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

¡Perfecto! Todas las claves ahora están en minúsculas.

Intentemos otro ejemplo para asegurarnos de que nuestra función funcione correctamente:

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

La salida debería ser:

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

Nuestra función funciona correctamente para diferentes objetos con varios estilos de capitalización de claves.
