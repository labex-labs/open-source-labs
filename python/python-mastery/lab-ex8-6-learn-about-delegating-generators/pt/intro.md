# Introdução

Neste laboratório, você aprenderá sobre a delegação de geradores em Python usando a instrução `yield from`. Este recurso, introduzido no Python 3.3, simplifica o código que depende de geradores e corrotinas.

Geradores são funções especiais que podem pausar e retomar a execução, mantendo seu estado entre as chamadas. A instrução `yield from` oferece uma maneira elegante de delegar o controle a outro gerador, aprimorando a legibilidade e a manutenibilidade do código.

**Objetivos:**

- Compreender o propósito da instrução `yield from`
- Aprender como usar `yield from` para delegar a outros geradores
- Aplicar este conhecimento para simplificar o código baseado em corrotinas
- Compreender a conexão com a sintaxe moderna async/await

**Arquivos com os quais você trabalhará:**

- `cofollow.py` - Contém funções utilitárias de corrotinas
- `server.py` - Contém uma implementação simples de servidor de rede
