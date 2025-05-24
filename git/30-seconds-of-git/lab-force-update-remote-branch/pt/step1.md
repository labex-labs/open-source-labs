# Atualizar Branch Remota Após Reescrever o Histórico

Quando você reescreve o histórico localmente, você cria um novo commit com um hash SHA-1 diferente. Isso significa que o histórico de commits em sua branch local é diferente do histórico de commits na branch remota. Se você tentar enviar (push) suas alterações para a branch remota, o Git rejeitará o push porque verá o histórico de commits como divergente. Para resolver esse problema, você precisa forçar uma atualização da branch remota.

Para completar este laboratório, você usará o repositório Git `git-playground` da sua conta do GitHub, que vem de um fork de `https://github.com/labex-labs/git-playground.git`.

1. Clone o repositório `git-playground` para sua máquina local:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Atualize um commit com a mensagem "Added file2.txt" para um commit com a mensagem "Update file2.txt":

```shell
git commit --amend
```

3. Envie (push) as alterações da branch local para o repositório remoto:

```shell
git push
```

4. Se você não conseguir enviar (push) com sucesso, force o push:

```shell
git push -f origin master
```

A flag `-f` força o Git a atualizar a branch remota com suas alterações, mesmo que o histórico de commits tenha divergido.

Este é o resultado final:

```shell
[object Object]
```
