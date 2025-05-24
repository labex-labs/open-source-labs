# Adicionar um Modelo de Mensagem de Commit

Sem um modelo de mensagem de commit, os desenvolvedores podem ser tentados a escrever mensagens de commit vagas ou pouco informativas, como "corrigido bug" ou "código atualizado". Isso dificulta que outros entendam o propósito da alteração e pode levar a confusão ou erros no futuro. Ao configurar um modelo de mensagem de commit, os desenvolvedores são incentivados a fornecer mensagens de commit mais detalhadas e informativas, o que pode melhorar a colaboração e a produtividade.

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga estas etapas para configurar um modelo de mensagem de commit para este repositório:

1. Clone o repositório para sua máquina local usando o comando `git clone https://github.com/labex-labs/git-playground`.
2. Navegue até o diretório do repositório usando o comando `cd git-playground` e configure sua conta do GitHub usando os comandos `git config --global user.name "seu-nome-de-usuário"` e `git config --global user.email "seu-email"`.
3. Crie um novo arquivo chamado `commit-template` no diretório do repositório usando o comando `vim commit-template`.
4. Abra o arquivo `commit-template` em um editor de texto e adicione as seguintes linhas:

```shell
# <type>: <subject>

# <body>

# <footer>

#This creates a template with three sections, where "<type>" indicates the type of submission, such as "feat" or "fix", "<subject>" is a short #summary describing the content of the submission, "<body>" is a more detailed description, and "<footer>" can contain other metadata, such as the #associated issue number or other comments.
```

5. Pressione <kbd>Esc</kbd> e digite o comando <kbd>:wq</kbd>, em seguida, pressione <kbd>Enter</kbd> para salvar suas alterações e sair do editor do arquivo `commit-template`.
6. Use o comando `git add commit-template` para adicionar o arquivo `commit-template` à área de staging (staging area).
7. Use o comando `git config commit.template commit-template` para definir o arquivo `commit-template` como o modelo de mensagem de commit para o repositório.
8. Use o comando `git commit` para abrir o editor de mensagem de commit e observe que o editor de mensagem de commit agora contém o modelo de mensagem de commit que você criou na etapa 4.
9. Pressione <kbd>Esc</kbd> e digite o comando <kbd>:q</kbd>, em seguida, pressione <kbd>Enter</kbd> para sair do editor de mensagem de commit.
