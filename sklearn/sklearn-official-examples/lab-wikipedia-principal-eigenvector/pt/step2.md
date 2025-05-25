# Carregar os ficheiros de redirecionamento

Vamos analisar os redirecionamentos e construir um mapa transitivamente fechado a partir deles.

```python
DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SHORTNAME_SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


def short_name(nt_uri):
    """Remover os marcadores de URI < e > e o prefixo URI comum"""
    return nt_uri[SHORTNAME_SLICE]


def index(redirects, index_map, k):
    """Encontrar o índice de um nome de artigo após a resolução de redirecionamentos"""
    k = redirects.get(k, k)
    return index_map.setdefault(k, len(index_map))


def get_redirects(redirects_filename):
    """Analisar os redirecionamentos e construir um mapa transitivamente fechado a partir deles"""
    redirects = {}
    print("A analisar o ficheiro de redirecionamento NT")
    for l, line in enumerate(BZ2File(redirects_filename)):
        split = line.split()
        if len(split) != 4:
            print("Ignorar linha malformada: " + line)
            continue
        redirects[short_name(split[0])] = short_name(split[2])
        if l % 1000000 == 0:
            print("[%s] linha: %08d" % (datetime.now().isoformat(), l))

    # calcular o fecho transitivo
    print("A calcular o fecho transitivo da relação de redirecionamento")
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
            print("[%s] linha: %08d" % (datetime.now().isoformat(), l))

    return redirects


# Carregando os ficheiros de redirecionamento
redirects = get_redirects(redirects_filename)
```
