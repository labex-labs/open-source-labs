# Просмотр коммитов в определенном диапазоне дат

Теперь мы узнаем, как фильтровать коммиты (коммиты - это записи о внесенных изменениях в репозиторий) по определенным датам. Git предоставляет два полезных параметра для этой цели:

- `--since` или `--after`: Показывает коммиты, более свежие, чем определенная дата
- `--until` или `--before`: Показывает коммиты, более старые, чем определенная дата

Когда мы комбинируем эти параметры, мы можем просматривать коммиты в определенном диапазоне дат.

Давайте посмотрим все коммиты, которые произошли с 25 апреля 2023 года по 27 апреля 2023 года:

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

Эта команда отобразит все коммиты, сделанные с 25 по 27 апреля 2023 года. Вывод должен выглядеть так:

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

Git поддерживает множество форматов дат, в том числе:

- `"YYYY-MM-DD"` (например, `2023-04-25`)
- `"Month DD YYYY"` (например, `Apr 25 2023`)
- `"DD Month YYYY"` (например, `25 Apr 2023`)

Попробуйте другой формат даты, чтобы узнать, есть ли коммиты в другом диапазоне:

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

Эта команда может не вернуть никаких результатов, если в этот период не было сделано ни одного коммита, что абсолютно нормально.
