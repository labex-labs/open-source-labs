# Visualizar o Status Atual

Como desenvolvedor, é importante saber o status atual do seu repositório Git. Isso inclui informações sobre quais arquivos foram modificados, quais arquivos estão preparados (staged) para o commit e quais arquivos não estão sendo rastreados (untracked). O comando `git status` fornece essas informações em um formato fácil de ler.

Sua tarefa é usar o comando `git status` para visualizar o status atual do repositório Git localizado em `https://github.com/labex-labs/git-playground`. Você deve prestar atenção à saída do comando e tentar entender o que ela significa.

Para completar este laboratório, você precisará clonar o repositório Git localizado em `https://github.com/labex-labs/git-playground`.

1. Depois de clonar o repositório, navegue até o diretório raiz do repositório:

```shell
cd git-playground
```

2. Visualize o status atual do repositório Git:

```shell
git status
```

Isso exibirá o status atual da árvore de trabalho (working tree). Você deve ver informações sobre em qual branch você está atualmente, se sua branch está atualizada com o repositório remoto e quaisquer arquivos não rastreados ou modificados.

A saída se parece com isto:

```shell
[object Object]
```
