# Escribir marcas con JSX

> El proyecto de React ya se ha proporcionado en la máquina virtual. En general, solo es necesario agregar código a `App.js`.

Utilice el siguiente comando para instalar las dependencias:

```bash
npm i
```

La sintaxis de marcas que se vio anteriormente se llama JSX. Es opcional, pero la mayoría de los proyectos de React la utilizan por su conveniencia.

JSX es más estricta que HTML. Debes cerrar las etiquetas como `<br />`. Tu componente también no puede devolver múltiples etiquetas JSX. Debes envolverlas en un padre compartido, como un `<h1>...</h1>` o un envoltorio vacío `<>...</>`:

```js
// App.js
export default function Profile() {
  return (
    <>
      <h1>Hedy Lamarr</h1>
    </>
  );
}
```

Si tienes mucha HTML que convertir a JSX, puedes usar un [conversor en línea](https://transform.tools/html-to-jsx).

Para ejecutar el proyecto, use el siguiente comando. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.

```bash
npm start
```
