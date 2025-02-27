# Загрузка файлов с переадресациями

Мы будем разбирать переадресации и создавать из них транзитивно замкнутую карту.

```python
DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SHORTNAME_SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


def short_name(nt_uri):
    """Удалить маркеры URI < и > и общий префикс URI"""
    return nt_uri[SHORTNAME_SLICE]


def index(redirects, index_map, k):
    """Найти индекс имени статьи после разрешения переадресации"""
    k = redirects.get(k, k)
    return index_map.setdefault(k, len(index_map))


def get_redirects(redirects_filename):
    """Разобрать переадресации и создать из них транзитивно замкнутую карту"""
    redirects = {}
    print("Разбор NT файла с переадресациями")
    for l, line in enumerate(BZ2File(redirects_filename)):
        split = line.split()
        if len(split)!= 4:
            print("игнорируем неправильную строку: " + line)
            continue
        redirects[short_name(split[0])] = short_name(split[2])
        if l % 1000000 == 0:
            print("[%s] строка: %08d" % (datetime.now().isoformat(), l))

    # вычислить транзитивное замыкание
    print("Вычисление транзитивного замыкания отношения переадресации")
    for l, source in enumerate(redirects.keys()):
        transitive_target = None
        target = redirects[source]
        seen = {source}
        while True:
            transitive_target = target
            target = redirects.get(target)
            if target is None or target in seen:
                break
            seen.add(target)
        redirects[source] = transitive_target
        if l % 1000000 == 0:
            print("[%s] строка: %08d" % (datetime.now().isoformat(), l))

    return redirects


# Загрузка файлов с переадресациями
redirects = get_redirects(redirects_filename)
```
