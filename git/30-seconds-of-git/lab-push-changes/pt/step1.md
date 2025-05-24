# Enviar Alterações Locais para Remoto

Como desenvolvedor, você pode precisar enviar (push) suas alterações locais para um repositório remoto para compartilhar seu trabalho com outros membros da equipe ou para implantar seu código em um ambiente de produção. O comando `git push` é usado para enviar as últimas alterações da branch local para o remoto. No entanto, antes de enviar as alterações, você precisa garantir que sua branch local esteja atualizada com a branch remota. Se houver quaisquer conflitos entre as branches local e remota, você precisará resolvê-los antes de enviar as alterações.

Para completar este laboratório, você usará o repositório Git `git-playground` da sua conta do GitHub, que vem de um fork de `https://github.com/labex-labs/git-playground.git`. Você fez algumas alterações na branch `master` e deseja enviá-las para o repositório remoto. Aqui estão as etapas que você precisa seguir:

1. Clone o repositório para sua máquina local e navegue até o diretório executando os seguintes comandos:

```shell
git clone https://github.com/your-username/git-playground
cd git-playground
```

2. Certifique-se de que sua branch local esteja atualizada com a branch remota executando o seguinte comando:

```shell
git pull origin master
```

3. Depois de puxar (pull) as últimas alterações da branch remota, você pode fazer suas alterações na branch local:

```shell
echo "hello,world" >> file1.txt
```

4. Depois de fazer as alterações, prepare-as usando o comando `git add`:

```shell
git add .
```

5. Faça o commit (commit) das alterações usando o comando `git commit`:

```shell
git commit -m "Added new feature"
```

6. Finalmente, envie (push) as alterações para o repositório remoto usando o comando `git push`:

```shell
git push origin master
```

Este é o resultado da execução de `git log`:

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
