# 요약

이 실험에서는 두 가지 방법인 `FeatureHasher`와 `DictVectorizer` 그리고 네 가지 특수 목적 텍스트 벡터화기인 `CountVectorizer`, `HashingVectorizer`, `TfidfVectorizer`를 비교하여 텍스트 벡터화를 탐색했습니다. 벡터화 방법들을 벤치마킹하고 결과를 플롯했습니다. 결론적으로 `HashingVectorizer`는 해시 충돌로 인한 변환의 역변환 불가능성에도 불구하고 `CountVectorizer`보다 성능이 더 좋았습니다. 또한, `DictVectorizer`와 `FeatureHasher`는 내부 토큰화 단계가 문서 전체에 대해 정규 표현식을 한 번 컴파일하고 재사용하기 때문에 수동으로 토큰화된 문서에서 동등한 텍스트 벡터화기보다 성능이 더 좋았습니다.
