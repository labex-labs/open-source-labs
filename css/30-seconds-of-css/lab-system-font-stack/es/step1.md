# Pila de fuentes del sistema

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para lograr una sensación de aplicación nativa, utiliza la fuente nativa del sistema operativo. Define una lista de fuentes utilizando `font-family`. El navegador busca cada fuente sucesiva, prefiriendo la primera si es posible y recurriendo a la siguiente si no puede encontrar la fuente (en el sistema o definida en CSS). Utiliza `-apple-system` para San Francisco en iOS y macOS (no en Chrome), y `BlinkMacSystemFont` para San Francisco en Chrome de macOS. Para Windows 10, utiliza `'Segoe UI'`, para Android utiliza `Roboto`, para Linux con KDE utiliza `Oxygen-Sans`, para Ubuntu (todas las variantes) utiliza `Ubuntu`, y para Linux con GNOME Shell utiliza `Cantarell`. Para macOS 10.10 y versiones inferiores, utiliza `'Helvetica Neue'` y `Helvetica`. Para una fuente sans serif de respaldo ampliamente compatible con todos los sistemas operativos, utiliza `Arial`. Para aplicar la fuente del sistema a un texto específico, utiliza el siguiente HTML y CSS:

```html
<p class="system-font-stack">This text uses the system font.</p>
```

```css
.system-font-stack {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
    sans-serif;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
