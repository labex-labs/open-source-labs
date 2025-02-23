# Cómo convertir una ruta con tilde en una ruta absoluta en Node.js

Para comenzar a practicar la codificación en Node.js, abre la Terminal o SSH y escribe `node`. Para convertir una ruta con tilde en una ruta absoluta, utiliza el siguiente código:

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

El código utiliza `String.prototype.replace()` con una expresión regular y `os.homedir()` para reemplazar el `~` al principio de la ruta con el directorio home. Aquí hay un ejemplo de cómo utilizar la función `untildify`:

```js
untildify("~/node"); // devuelve '/Users/aUser/node'
```
