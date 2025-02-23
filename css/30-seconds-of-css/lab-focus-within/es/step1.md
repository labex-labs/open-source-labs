# Enfoque Dentro De

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para cambiar la apariencia de un formulario cuando cualquiera de sus elementos hijos está enfocado, use la pseudo-clase `:focus-within` para aplicar estilos al elemento padre. Por ejemplo, en el código HTML dado, si cualquiera de los campos de entrada está enfocado, el elemento `form` tendrá un fondo verde. Para aplicar estilos a los elementos hijos, use selectores CSS adecuados como `label` e `input`.

```html
<form>
  <label for="username">Nombre de usuario:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Contraseña:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

Haga clic en 'Ir en vivo' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
