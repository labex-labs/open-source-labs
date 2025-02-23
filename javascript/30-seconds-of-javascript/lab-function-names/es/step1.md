# Cómo obtener nombres de propiedades de función a partir de un objeto en JavaScript

Para obtener una matriz de nombres de propiedades de función a partir de un objeto, utiliza la función `functions` proporcionada a continuación. Esta función también puede incluir, opcionalmente, propiedades heredadas.

Aquí está cómo utilizar la función `functions`:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.keys()` para iterar sobre las propiedades propias del objeto.
3. Si desea incluir propiedades heredadas, establezca el argumento `inherited` en `true` y utilice `Object.getPrototypeOf()` para obtener las propiedades heredadas del objeto.
4. Utilice `Array.prototype.filter()` para conservar solo aquellas propiedades que son funciones.
5. Omita el segundo argumento, `inherited`, para no incluir propiedades heredadas por defecto.

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

Aquí está un ejemplo de uso de la función `functions`:

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
