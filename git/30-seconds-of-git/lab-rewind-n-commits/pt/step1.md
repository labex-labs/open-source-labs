# Retroceder (Rewind) Commits

Como desenvolvedor, você tem trabalhado em um projeto e fez vários commits. No entanto, você percebe que os últimos commits contêm erros e precisa voltar para uma versão anterior do seu código. Você precisa usar o Git para retroceder seus commits e retornar à versão anterior do seu código.

Para completar este laboratório, você usará o repositório Git `git-playground` da sua conta GitHub, que vem de um fork de `https://github.com/labex-labs/git-playground.git`. Siga estes passos:

1. Clone o repositório para sua máquina local:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Crie uma nova branch chamada `rewind-commits`:

```shell
git checkout -b rewind-commits
```

3. Visualize o histórico de commits do repositório e perceba que o último commit contém erros e você precisa voltar para a versão anterior do seu código:

```shell
git log
```

4. Use o Git para retroceder seus commits em 1:

```shell
git reset HEAD~1 --hard
```

5. Verifique se você retrocedeu seus commits com sucesso:

```shell
git log
```

6. Envie suas alterações para a branch `rewind-commits`:

```shell
git push --force origin rewind-commits
```

Este é o resultado final:

```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```
