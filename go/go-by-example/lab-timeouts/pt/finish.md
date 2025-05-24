# Resumo

Neste laboratório, aprendemos como implementar timeouts em Go usando canais e `select`. Usamos um canal com buffer para evitar vazamentos de goroutine caso o canal nunca seja lido, e `time.After` para aguardar um valor a ser enviado após o timeout. Também usamos `select` para prosseguir com a primeira recepção que estiver pronta.
