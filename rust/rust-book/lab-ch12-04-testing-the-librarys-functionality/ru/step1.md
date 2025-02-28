# Тестируемое разработка

Теперь, когда мы извлекли логику в `src/lib.rs` и оставили сбор аргументов и обработку ошибок в `src/main.rs`, гораздо проще писать тесты для ядра функциональности нашего кода. Мы можем напрямую вызывать функции с различными аргументами и проверять возвращаемые значения, не нужно вызывать нашу бинарную программу из командной строки.

В этом разделе мы добавим логику поиска в программу `minigrep` с использованием процесса тестируемого разработки (TDD) с такими шагами:

1. Напишите тест, который не проходит, и запустите его, чтобы убедиться, что он не проходит по той причине, которую вы ожидаете.
2. Напишите или измените только столько кода, чтобы новый тест прошел.
3. Перестроите код, который вы только что добавили или изменили, и убедитесь, что тесты продолжают проходить.
4. Повторяйте с шага 1!

Хотя это всего лишь один из многих способов написания программного обеспечения, TDD может помочь в проектировании кода. Написание теста перед написанием кода, который делает тест проходящим, помогает поддерживать высокую степень покрытия тестами на протяжении всего процесса.

Мы проведем тестируемое развитие реализации функциональности, которая на самом деле будет искать строку запроса в содержимом файла и генерировать список строк, которые соответствуют запросу. Мы добавим эту функциональность в функцию под названием `search`.
