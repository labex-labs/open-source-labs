# Die Umleitungsdateien laden

Wir werden die Umleitungen analysieren und daraus eine transitiv abgeschlossene Karte erstellen.

```python
DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SHORTNAME_SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


def short_name(nt_uri):
    """Entfernt die < und > URI-Marker und den üblichen URI-Präfix"""
    return nt_uri[SHORTNAME_SLICE]


def index(redirects, index_map, k):
    """Finds den Index eines Artikelnamens nach der Auflösung der Umleitung"""
    k = redirects.get(k, k)
    return index_map.setdefault(k, len(index_map))


def get_redirects(redirects_filename):
    """Analysiert die Umleitungen und erstellt daraus eine transitiv abgeschlossene Karte"""
    redirects = {}
    print("Analysiere die NT-Umleitungsdatei")
    for l, line in enumerate(BZ2File(redirects_filename)):
        split = line.split()
        if len(split)!= 4:
            print("Ignoriere fehlerhafte Zeile: " + line)
            continue
        redirects[short_name(split[0])] = short_name(split[2])
        if l % 1000000 == 0:
            print("[%s] Zeile: %08d" % (datetime.now().isoformat(), l))

    # Berechne die transitive Schließung
    print("Berechne die transitive Schließung der Umleitungsrelation")
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
            print("[%s] Zeile: %08d" % (datetime.now().isoformat(), l))

    return redirects


# Laden der Umleitungsdateien
redirects = get_redirects(redirects_filename)
```
