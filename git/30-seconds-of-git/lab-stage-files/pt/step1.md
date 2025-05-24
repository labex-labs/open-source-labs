# Adicionar Arquivos à Área de Staging

Você tem trabalhado em um projeto armazenado em um repositório Git chamado `https://github.com/labex-labs/git-playground`. Você fez algumas alterações no código-base e deseja commitar (commit) essas alterações no repositório. No entanto, você só quer commitar alterações específicas e não todas as alterações que fez. Para fazer isso, você precisa adicionar os arquivos à área de staging.

1. Você fará algumas alterações no diretório `git-playground`:

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. Adicione esses arquivos à área de staging:

```shell
git add index.html style.css
```

3. Visualize o status do diretório de trabalho atual e da área de staging, incluindo informações sobre quais arquivos foram modificados, quais arquivos foram adicionados à área de staging, etc:

```shell
git status
```

4. Alternativamente, adicione todos os arquivos com a extensão `.js`:

```shell
git add *.js
```

5. Visualize o status do diretório de trabalho atual e da área de staging novamente:

```shell
git status
```

6. Você também pode adicionar todas as alterações à área de staging:

```shell
git add .
```

7. Visualize o status do diretório de trabalho atual e da área de staging novamente:

```shell
git status
```

Este é o resultado final:

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
