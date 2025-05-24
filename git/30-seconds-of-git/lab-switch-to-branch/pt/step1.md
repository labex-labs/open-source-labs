# Mudar para uma Branch

Você tem trabalhado em um projeto em um repositório Git chamado `https://github.com/labex-labs/git-playground`. Sua equipe criou uma nova branch chamada `feature-1` para trabalhar em uma nova funcionalidade. Você precisa mudar para a branch `feature-1` para continuar trabalhando na funcionalidade.

1. Clone o repositório Git:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegue até o diretório do repositório:

```shell
cd git-playground
```

3. Liste todas as branches no repositório:

```shell
git branch
```

Output:

```shell
feature-1
* master
```

4. Mude para a branch `feature-1`:

```shell
git checkout feature-1
```

Output:

```shell
Switched to branch 'feature-1'
```

5. Verifique se você está agora na branch `feature-1`:

```shell
git branch
```

Output:

```shell
* feature-1
master
```
