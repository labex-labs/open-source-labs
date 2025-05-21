# Explorando o Comando Básico `git log`

Agora que clonamos nosso repositório, vamos aprender como visualizar o histórico de commits usando o comando `git log`.

O comando `git log` exibe uma lista de todos os commits no repositório, começando pelo mais recente. Cada entrada de commit inclui:

- Um hash de commit (identificador) único
- Informações do autor
- Data e hora do commit
- Mensagem do commit

Vamos visualizar o histórico básico de commits:

```bash
git log
```

Você deve ver uma saída semelhante à seguinte:

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

Se a saída for longa, você pode navegar por ela usando:

- Pressione `Space` para avançar
- Pressione `b` para retroceder
- Pressione `q` para sair da visualização do log

Observe que cada commit tem um identificador único (a longa string hexadecimal), as informações do autor, a data e hora do commit e uma mensagem descrevendo as alterações feitas.
