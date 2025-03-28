# Добавить шаблон сообщения коммитов

Без шаблона сообщений коммитов разработчики могут быть склонны писать неясные или неинформативные сообщения коммитов, такие как "исправлена ошибка" или "обновлен код". Это затрудняет другим понять цель изменения и может привести к путанице или ошибкам в дальнейшем. Созданием шаблона сообщений коммитов разработчики будут поощряться предоставлять более детальные и информативные сообщения коммитов, что может улучшить сотрудничество и продуктивность.

## Задачи

Для этого испытания давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Перейдите в директорию репозитория и настройте свою GitHub-identность.
2. Создайте новый файл с именем `commit-template` в текущей директории репозитория.
3. Откройте файл `commit-template` в текстовом редакторе и добавьте следующие строки:

```shell
# <тип>: <тема>

# <тело>

# <подвал>

# Это создает шаблон с тремя разделами:
# "<тип>" указывает тип внесения изменений, например, "feat" или "fix"
# "<тема>" - это краткое #суммари описывающее содержание внесения изменений
# "<тело>" - более подробное описание
# "<подвал>" может содержать другую метаданные, например, #ассоциированный номер задачи или другие комментарии.
```

4. Нажмите <kbd>Esc</kbd> и введите команду <kbd>:wq</kbd>, затем нажмите <kbd>Enter</kbd>, чтобы сохранить изменения и выйти из редактора файла `commit-template`.
5. Добавьте файлы `commit-template` в staging-область.
6. Установите файл `commit-template` в качестве шаблона сообщений коммитов для репозитория.
7. Откройте редактор сообщений коммитов и обратите внимание, что редактор сообщений коммитов теперь содержит шаблон сообщений коммитов, который вы создали в шаге 3.
8. Нажмите <kbd>Esc</kbd> и введите команду <kbd>:q</kbd>, затем нажмите <kbd>Enter</kbd>, чтобы выйти из редактора сообщений коммитов.
