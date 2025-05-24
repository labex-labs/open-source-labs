# Resumo

Neste laboratório, aprendemos como usar mutexes para acessar dados com segurança em múltiplas goroutines. Criamos uma struct `Container` para conter um mapa de contadores e usamos um `Mutex` para sincronizar o acesso ao mapa `counters`. Também implementamos um método `inc` para incrementar o contador nomeado e usamos a struct `sync.WaitGroup` para esperar que as goroutines terminassem. Finalmente, imprimimos o mapa `counters` usando a função `fmt.Println`.
