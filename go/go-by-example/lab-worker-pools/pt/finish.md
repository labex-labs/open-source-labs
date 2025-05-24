# Resumo

Este laboratório demonstrou como implementar um _worker pool_ usando _goroutines_ e _channels_. O _worker pool_ recebe trabalho no _channel_ `jobs` e envia os resultados correspondentes no _channel_ `results`. Cada _worker_ dorme por um segundo por _job_ para simular uma tarefa dispendiosa.
