# Resumo

Neste laboratório, aprendemos como usar o pacote `sync/atomic` para gerenciar o estado em Go, incrementando um contador usando múltiplas goroutines. A função `AddUint64` foi usada para incrementar atomicamente o contador, e um `WaitGroup` foi usado para esperar que todas as goroutines terminassem seu trabalho.
