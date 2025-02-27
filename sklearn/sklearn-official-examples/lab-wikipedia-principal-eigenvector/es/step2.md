# Cargar los archivos de redirección

Analizaremos las redirecciones y construiremos un mapa transitivamente cerrado a partir de ellas.

```python
DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SHORTNAME_SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


def short_name(nt_uri):
    """Quitar los marcadores URI < y > y el prefijo URI común"""
    return nt_uri[SHORTNAME_SLICE]


def index(redirects, index_map, k):
    """Encontrar el índice de un nombre de artículo después de la resolución de redirecciones"""
    k = redirects.get(k, k)
    return index_map.setdefault(k, len(index_map))


def get_redirects(redirects_filename):
    """Analizar las redirecciones y construir un mapa transitivamente cerrado a partir de ellas"""
    redirects = {}
    print("Analizando el archivo de redirecciones NT")
    for l, line in enumerate(BZ2File(redirects_filename)):
        split = line.split()
        if len(split)!= 4:
            print("ignorando línea malformada: " + line)
            continue
        redirects[short_name(split[0])] = short_name(split[2])
        if l % 1000000 == 0:
            print("[%s] línea: %08d" % (datetime.now().isoformat(), l))

    # calcular la clausura transitiva
    print("Calculando la clausura transitiva de la relación de redirección")
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
            print("[%s] línea: %08d" % (datetime.now().isoformat(), l))

    return redirects


# Cargando los archivos de redirección
redirects = get_redirects(redirects_filename)
```
