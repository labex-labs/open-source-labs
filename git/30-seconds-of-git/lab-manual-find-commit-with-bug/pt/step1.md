# Encontrar Manualmente o Commit que Introduziu um Bug

Sua tarefa é encontrar manualmente o commit que introduziu um bug no repositório `git-playground`. O repositório pode ser encontrado em `https://github.com/labex-labs/git-playground`. O bug é que o arquivo `file2.txt` deve imprimir "This is file2.txt." em vez de "This is file2.".

Para completar este laboratório, você precisará usar o comando `git bisect` para realizar uma busca binária através do histórico de commits do repositório. Você precisará marcar os commits como "good" (sem bugs) ou "bad" (com bugs) até que você tenha restringido o commit que introduziu o bug.

1. Mude para o diretório do repositório:

```
cd git-playground
```

2. Inicie o processo `git bisect`:

```
git bisect start
```

3. Marque o commit atual como "bad":

```
git bisect bad HEAD
```

4. Marque um commit com a mensagem "Initial commit" como "good". O Git irá automaticamente fazer o checkout de um novo commit para você testar:

```
git bisect good 3050fc0de
```

O Git irá automaticamente fazer o checkout de um novo commit para você testar. 5. Se o conteúdo do arquivo `file2.txt` verificado não corresponder ao bug, marque-o como "good":

```
cat file2.txt
git bisect good
```

6. Se o conteúdo do arquivo `file2.txt` verificado corresponder ao bug, marque-o como "bad":

```
git bisect bad
```

7. Depois de encontrar o commit com bug, reinicie o processo `git bisect`:

```
git bisect reset
```

Agora você pode examinar as mudanças no código no commit com bug para encontrar a origem do bug.

Este é o resultado do teste:

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 is the first bad commit
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
