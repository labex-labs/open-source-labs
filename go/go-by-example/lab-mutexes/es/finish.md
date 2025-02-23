# Resumen

En este laboratorio, aprendimos cómo utilizar mutexes para acceder de manera segura a datos a través de múltiples goroutines. Creamos una estructura `Container` para almacenar un mapa de contadores y utilizamos un `Mutex` para sincronizar el acceso al mapa `counters`. También implementamos un método `inc` para incrementar el contador nombrado y utilizamos la estructura `sync.WaitGroup` para esperar a que las goroutines terminen. Finalmente, imprimimos el mapa `counters` utilizando la función `fmt.Println`.
