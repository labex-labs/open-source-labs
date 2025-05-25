# 리디렉션 파일 로드

리디렉션을 파싱하고 전이적으로 닫힌 맵을 생성합니다.

```python
DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SHORTNAME_SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


def short_name(nt_uri):
    """< 및 > URI 마커와 공통 URI 접두사를 제거합니다."""
    return nt_uri[SHORTNAME_SLICE]


def index(redirects, index_map, k):
    """리디렉션 해결 후 문서 이름의 인덱스를 찾습니다."""
    k = redirects.get(k, k)
    return index_map.setdefault(k, len(index_map))


def get_redirects(redirects_filename):
    """리디렉션을 파싱하고 전이적으로 닫힌 맵을 생성합니다."""
    redirects = {}
    print("NT 리디렉션 파일을 파싱 중")
    for l, line in enumerate(BZ2File(redirects_filename)):
        split = line.split()
        if len(split) != 4:
            print("잘못된 형식의 줄 무시: " + line)
            continue
        redirects[short_name(split[0])] = short_name(split[2])
        if l % 1000000 == 0:
            print("[%s] 줄: %08d" % (datetime.now().isoformat(), l))

    # 리디렉션 관계의 전이적 폐쇄를 계산합니다.
    print("리디렉션 관계의 전이적 폐쇄를 계산 중")
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
            print("[%s] 줄: %08d" % (datetime.now().isoformat(), l))

    return redirects


# 리디렉션 파일 로드
redirects = get_redirects(redirects_filename)
```
