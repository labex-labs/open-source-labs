# Fazendo Pull de Todos os Submódulos do Remoto

Você tem um repositório Git com submódulos que precisam ser atualizados de seus respectivos remotos. Fazer o pull manualmente de cada submódulo pode ser demorado e propenso a erros. Você precisa de uma maneira de fazer o pull de todos os submódulos de uma vez.

Assumindo que você tem um repositório Git chamado `git` que contém submódulos, você pode fazer o pull de todos os submódulos de seus respectivos remotos usando o seguinte comando:

```shell
cd git
git submodule update --recursive --remote
```

Este comando atualiza todos os submódulos no repositório para a versão mais recente disponível em seus respectivos remotos.
