# Resumo

Este laboratório demonstrou como usar canais (channels) e goroutines para sincronizar o acesso a um estado compartilhado. Ao ter uma única goroutine como proprietária do estado e usar canais para emitir pedidos de leitura e escrita, podemos evitar condições de corrida (race conditions) e corrupção de dados.
