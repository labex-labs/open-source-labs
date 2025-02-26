# Introducción

En este laboratorio, aprenderemos a crear un Hook personalizado de React llamado `useOnWindowResize` que ejecutará una devolución de llamada cada vez que se redimensione la ventana. Utilizaremos los Hooks `useRef()` y `useEffect()` para escuchar el evento `'resize'` del objeto global `Window` y limpiar cuando el componente se desmonte. Este Hook puede ser útil para crear aplicaciones web responsivas que necesiten ajustarse a diferentes tamaños de pantalla.
