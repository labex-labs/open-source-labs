# Deletar um Git Stash

Você tem um repositório Git chamado `https://github.com/labex-labs/git-playground`. Você criou um _stash_ usando o comando `git stash save "my stash"`. Agora, você quer deletar este _stash_ porque não precisa mais dele.

1. Mude para o diretório do repositório usando o comando `cd git-playground`.
2. Liste todos os _stashes_ usando o comando `git stash list`. Você deve ver o _stash_ que acabou de criar.
3. Delete o _stash_ usando o comando `git stash drop stash@{0}`.
4. Liste todos os _stashes_ novamente usando o comando `git stash list`.

O _stash_ que você acabou de deletar não deve mais estar lá.
