# Retroceder para um Commit Específico

Como desenvolvedor, você pode precisar desfazer alterações feitas em seu código-base. Por exemplo, você pode ter cometido um erro e precisar voltar para uma versão anterior do seu código. Neste desafio, você usará o Git para retroceder (rewind) para um commit específico em um repositório.

Para completar este laboratório, você usará o repositório Git `git-playground` de `https://github.com/labex-labs/git-playground.git`. Siga estas etapas para completar o desafio:

1. Clone o repositório para sua máquina local:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegue até o repositório:

```shell
cd git-playground
```

3. Visualize o histórico de commits do repositório:

```shell
git log --oneline
```

4. Certifique-se de que a mensagem de commit para a qual você deseja retroceder seja o hash do commit "Initial commit".
5. Use o comando `git reset <commit>` para retroceder para o commit especificado. Por exemplo, se você deseja retroceder para o commit com o hash `3050fc0d3`:

```shell
git reset 3050fc0d3
```

6. Visualize o histórico de commits do repositório novamente:

```shell
git log --oneline
```

7. Se você deseja excluir as alterações e reverter para a versão anterior do seu código, use o comando `git reset --hard <commit>`. Por exemplo, se você deseja excluir as alterações e reverter para o commit com o hash `c0d30f305`:

```shell
git reset --hard c0d30f305
```

Este é o resultado da execução de `git log --oneline`:

```shell
c0d30f305 (HEAD -> master) Initial commit
```
