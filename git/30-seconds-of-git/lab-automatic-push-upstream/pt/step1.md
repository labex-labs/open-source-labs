# Automatizar a Criação de Branch Upstream

Como desenvolvedor, você deseja automatizar o processo de criação de branches upstream no push para evitar o trabalho de criar manualmente a branch no repositório remoto.

Para este laboratório, você fará um fork (bifurcação) do repositório `https://github.com/labex-labs/git-playground` para sua conta, usando o repositório `git-playground` em sua conta para criar automaticamente a branch upstream no push.

1. No site do GitHub, faça login na sua conta e encontre `https://github.com/labex-labs/git-playground` para fazer o fork do repositório para sua conta.
2. Na página do seu próprio repositório bifurcado, clique no botão `Code` e copie a URL do repositório.
3. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

4. Use o seguinte comando para habilitar a criação automática de branch upstream no push:

```shell
git config --global push.default current
```

5. Envie (push) uma nova branch chamada `new-feature`, que não existe no repositório remoto:

```shell
git checkout -b new-feature
git push
```

6. Verifique se a nova branch foi criada no repositório remoto:

```shell
git ls-remote --heads origin
```

Este é o resultado após concluir o laboratório:

![automatic upstream branch result](../assets/challenge-automatic-push-upstream-step1-1.png)
