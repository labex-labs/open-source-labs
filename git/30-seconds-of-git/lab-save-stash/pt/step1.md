# Criar um Git Stash

Como desenvolvedor, você pode se encontrar em uma situação em que precisa mudar para um branch diferente ou trabalhar em uma funcionalidade diferente, mas ainda não está pronto para commitar suas alterações. Você não quer perder seu progresso, mas também não quer commitar código incompleto ou com bugs. É aqui que um stash é útil.

Um stash permite que você salve suas alterações sem commitá-las, para que possa mudar para um branch diferente ou trabalhar em uma funcionalidade diferente. Você pode então aplicar seu stash mais tarde, quando estiver pronto para continuar trabalhando em suas alterações.

Para criar um stash, você pode usar o comando `git stash save`. Digamos que você esteja trabalhando em um branch chamado `feature` no repositório `git-playground` e queira salvar suas alterações antes de mudar para um branch diferente:

1. Primeiro, navegue até o diretório `git-playground`:

```shell
cd git-playground
```

2. Mude para um branch chamado `feature`:

```shell
git checkout -b feature
```

3. Faça algumas alterações nos arquivos no diretório:

```shell
echo "Some changes" >> README.md
```

4. Salve suas alterações em um stash:

```shell
git stash save "My changes"
```

5. Mude para um branch diferente:

```shell
git checkout master
```

6. Quando terminar de fazer alterações no outro branch, volte para o branch `feature` e aplique seu stash:

```shell
git stash apply
```

Este é o resultado final:

```shell
stash@{0}: On feature: My changes
```
