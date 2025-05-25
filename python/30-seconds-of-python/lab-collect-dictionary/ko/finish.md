# 요약

이 챌린지에서는 고유하지 않은 해시 가능한 (hashable) 값을 가진 딕셔너리를 반전시키는 방법을 배웠습니다. 각 키에 대한 기본값으로 `list`를 사용하는 `collections.defaultdict`를 사용한 다음, `dict.append()`를 사용하여 딕셔너리의 값을 키에 매핑했습니다. 마지막으로, `dict()`를 사용하여 `collections.defaultdict`를 일반 딕셔너리로 변환했습니다.
