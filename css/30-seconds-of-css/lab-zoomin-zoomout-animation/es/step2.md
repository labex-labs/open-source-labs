# Estilos CSS básicos

Ahora que tenemos nuestra estructura HTML lista, creemos los estilos CSS básicos para nuestro elemento de animación.

1. Abre el archivo `style.css` en el editor.

2. Si el archivo está vacío o falta, créalo con el siguiente contenido:

```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
}

.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
}
```

3. Entendamos qué hace este CSS:

   - Establecemos algunos estilos básicos para la página (fuente, ancho y márgenes)
   - Estilizamos el encabezado con un color gris oscuro
   - Para nuestro elemento de animación `.zoom-in-out-box`,:
     - Agregamos un margen de 24px alrededor de él
     - Establecemos su ancho y alto en 50px
     - Le damos un color de fondo rosa vibrante

4. Guarda el archivo `style.css` después de realizar estos cambios.

5. Para ver tu progreso, haz clic en el botón "Go Live" en la esquina inferior derecha de VSCode. Esto iniciará un servidor web en el puerto 8080. Luego, actualiza la pestaña **Web 8080** para ver tu cuadro estilizado.

Ahora deberías ver un pequeño cuadrado rosa en tu página web. Este cuadrado es el elemento que animaremos en los siguientes pasos.
