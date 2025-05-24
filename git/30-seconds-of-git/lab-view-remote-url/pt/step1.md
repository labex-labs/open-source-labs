# Visualizar a URL Remota

Como desenvolvedor, você pode precisar visualizar a URL de um repositório remoto por vários motivos, como solucionar problemas com sua configuração do Git ou verificar se você está trabalhando com o repositório correto. No entanto, se você não estiver familiarizado com os comandos Git, pode ser desafiador saber como visualizar a URL remota.

Para este laboratório, usaremos o repositório Git chamado `https://github.com/labex-labs/git-playground`. Para visualizar a URL remota deste repositório, siga estas etapas:

1. Abra seu terminal ou prompt de comando.
2. Navegue até o diretório onde você clonou o repositório `git-playground`:

```shell
cd git-playground
```

3. Execute o seguinte comando para visualizar a URL remota:

```shell
git config --get remote.origin.url
```

A saída deve exibir a URL do repositório remoto, que neste caso é `https://github.com/labex-labs/git-playground.git`.
