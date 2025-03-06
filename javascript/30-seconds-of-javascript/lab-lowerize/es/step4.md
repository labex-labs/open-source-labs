# Manejo de casos extremos

Nuestra función funciona bien para objetos simples, pero ¿qué pasa con casos más complejos? Exploremos algunos casos extremos y veamos cómo nuestra función los maneja.

## Objetos vacíos

Primero, probemos con un objeto vacío:

```javascript
lowerizeKeys({});
```

La salida debería ser un objeto vacío:

```
{}
```

## Objetos con objetos anidados

¿Qué pasa si el objeto contiene objetos anidados? Intentémoslo:

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

La salida será:

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

Observa que solo la clave de primer nivel `User` se convierte a minúsculas. Las claves dentro de los objetos anidados permanecen sin cambios.

Para manejar objetos anidados, necesitaríamos modificar nuestra función para procesar recursivamente todos los objetos. Creemos una versión mejorada:

```javascript
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
```

Esta función mejorada:

1. Verifica si cada valor es también un objeto (y no un array o nulo)
2. Si lo es, llama a sí misma recursivamente en ese objeto anidado
3. De lo contrario, utiliza el valor original

Probémosla con nuestro objeto anidado:

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

Ahora deberías ver todas las claves convertidas a minúsculas, incluso en objetos anidados:

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

¡Buen trabajo! Has creado una función avanzada que puede manejar objetos anidados.
