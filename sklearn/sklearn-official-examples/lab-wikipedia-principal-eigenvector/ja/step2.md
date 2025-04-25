# リダイレクトファイルを読み込む

リダイレクションを解析し、それから推移的に閉じたマップを作成します。

```python
DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SHORTNAME_SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


def short_name(nt_uri):
    """< と > URI マーカーと共通の URI 接頭辞を削除する"""
    return nt_uri[SHORTNAME_SLICE]


def index(redirects, index_map, k):
    """リダイレクト解決後の記事名のインデックスを見つける"""
    k = redirects.get(k, k)
    return index_map.setdefault(k, len(index_map))


def get_redirects(redirects_filename):
    """リダイレクトを解析し、それから推移的に閉じたマップを作成する"""
    redirects = {}
    print("NT リダイレクトファイルを解析中")
    for l, line in enumerate(BZ2File(redirects_filename)):
        split = line.split()
        if len(split)!= 4:
            print("整形されていない行を無視：" + line)
            continue
        redirects[short_name(split[0])] = short_name(split[2])
        if l % 1000000 == 0:
            print("[%s] 行：%08d" % (datetime.now().isoformat(), l))

    # 推移的閉包を計算する
    print("リダイレクト関係の推移的閉包を計算中")
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
            print("[%s] 行：%08d" % (datetime.now().isoformat(), l))

    return redirects


# リダイレクトファイルを読み込む
redirects = get_redirects(redirects_filename)
```
