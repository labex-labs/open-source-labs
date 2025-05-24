# Editar o Arquivo de Configuração do Git

Como desenvolvedor, você pode precisar modificar o arquivo de configuração do Git para personalizar o comportamento do Git. O arquivo de configuração do Git é um arquivo de texto simples que contém configurações na forma de pares chave-valor. O arquivo pode ser editado usando qualquer editor de texto, mas o Git fornece um editor de texto embutido que pode ser usado para modificar o arquivo de configuração.

Neste exemplo, usaremos o repositório Git chamado `https://github.com/labex-labs/git-playground` para demonstrar como editar o arquivo de configuração do Git.

1. Abra o terminal e navegue até o diretório do repositório Git:

```shell
cd git-playground
```

2. Use o seguinte comando para abrir o arquivo de configuração do Git no editor de texto do Git:

```shell
git config --global -e
```

3. O comando acima abrirá o arquivo de configuração do Git no editor de texto padrão do Git. Você pode alterar a configuração para que o nome de usuário seja `labex_git` e o e-mail do usuário seja `labex_git@example.com`.
4. Depois de fazer as alterações necessárias, pressione <kbd>Esc</kbd> e digite o comando <kbd>:wq</kbd>, em seguida, pressione <kbd>Enter</kbd> para salvar suas alterações e sair do editor.

Este é o resultado após a conclusão:

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```
