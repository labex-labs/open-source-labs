# Realizar um Rebase Interativo

Você está trabalhando em um projeto com uma equipe de desenvolvedores e fez vários commits em seu branch. No entanto, você percebe que alguns dos commits são desnecessários ou precisam ser combinados. Você quer limpar seu histórico de commits e torná-lo mais organizado.

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga estes passos:

1. Navegue até o diretório:
   ```shell
   cd git-playground
   ```
2. Realize um rebase interativo dos últimos 2 commits:
   ```shell
   git rebase -i HEAD~2
   ```
   O arquivo de rebase interativo será aberto em seu editor de texto padrão. Você pode modificar a ordem dos commits e a ação a ser realizada para cada um (pick, squash, drop, reword etc.).
3. Mude "pick" para "squash" na mensagem de commit "Added file2.txt", pressione <kbd>Esc</kbd> e digite o comando <kbd>:wq</kbd>, em seguida, pressione <kbd>Enter</kbd> para salvar suas alterações e sair do editor, altere a mensagem de commit para "Added file1.txt and file2.txt" da mesma forma e saia.
4. Se houver conflitos de merge ou você precisar fazer alterações, você pode continuar o rebase quando estiver pronto usando `git rebase --continue` ou abortá-lo usando `git rebase --abort`.

Executar `git log` lhe dará um resultado que se parece com isto:

```shell
[object Object]
```
