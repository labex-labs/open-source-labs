# Charger les fichiers de redirection

Nous allons analyser les redirections et construire une carte fermée transitive à partir d'elles.

```python
DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SHORTNAME_SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


def short_name(nt_uri):
    """Supprime les marqueurs d'URI < et > et le préfixe d'URI commun"""
    return nt_uri[SHORTNAME_SLICE]


def index(redirects, index_map, k):
    """Trouve l'index d'un nom d'article après la résolution des redirections"""
    k = redirects.get(k, k)
    return index_map.setdefault(k, len(index_map))


def get_redirects(redirects_filename):
    """Analyse les redirections et construit une carte fermée transitive à partir d'elles"""
    redirects = {}
    print("Analyse du fichier de redirection NT")
    for l, line in enumerate(BZ2File(redirects_filename)):
        split = line.split()
        if len(split)!= 4:
            print("ignorer la ligne malformée : " + line)
            continue
        redirects[short_name(split[0])] = short_name(split[2])
        if l % 1000000 == 0:
            print("[%s] ligne : %08d" % (datetime.now().isoformat(), l))

    # calcule la clôture transitive
    print("Calcul de la clôture transitive de la relation de redirection")
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
            print("[%s] ligne : %08d" % (datetime.now().isoformat(), l))

    return redirects


# Chargement des fichiers de redirection
redirects = get_redirects(redirects_filename)
```
