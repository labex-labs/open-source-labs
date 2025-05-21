# Visualizando Commits em um Intervalo de Datas Específico

Agora, aprenderemos como filtrar commits com base em datas específicas. O Git fornece duas opções úteis para esse propósito:

- `--since` ou `--after`: Mostra commits mais recentes que uma data específica
- `--until` ou `--before`: Mostra commits mais antigos que uma data específica

Quando combinamos essas opções, podemos visualizar commits dentro de um intervalo de datas específico.

Vamos visualizar todos os commits que ocorreram entre 25 de abril de 2023 e 27 de abril de 2023:

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

Este comando exibirá todos os commits que foram feitos entre 25 de abril e 27 de abril de 2023. A saída deve ser semelhante a esta:

```
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

O Git aceita muitos formatos de data, incluindo:

- `"YYYY-MM-DD"` (por exemplo, `2023-04-25`)
- `"Month DD YYYY"` (por exemplo, `Apr 25 2023`)
- `"DD Month YYYY"` (por exemplo, `25 Apr 2023`)

Experimente outro formato de data para ver se há algum commit dentro de um intervalo diferente:

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

Este comando pode não retornar nenhum resultado se não houveram commits durante esse período, o que é perfeitamente normal.
