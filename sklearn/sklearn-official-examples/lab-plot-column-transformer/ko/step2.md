# 변환기 생성

데이터셋에서 특징을 추출하는 변환기를 생성할 것입니다. 데이터 변환을 수행하는 두 개의 함수를 정의한 다음, Scikit-Learn 의 `FunctionTransformer`를 사용하여 변환기를 생성합니다.

```python
def subject_body_extractor(posts):
    # 두 열을 가진 object dtype 배열을 생성합니다.
    # 첫 번째 열 = '제목'이고 두 번째 열 = '본문'입니다.
    features = np.empty(shape=(len(posts), 2), dtype=object)
    for i, text in enumerate(posts):
        # 임시 변수 `_` 는 '\n\n'을 저장합니다.
        headers, _, body = text.partition("\n\n")
        # 본문 텍스트를 두 번째 열에 저장합니다.
        features[i, 1] = body

        prefix = "Subject:"
        sub = ""
        # 'Subject:' 뒤의 텍스트를 첫 번째 열에 저장합니다.
        for line in headers.split("\n"):
            if line.startswith(prefix):
                sub = line[len(prefix) :]
                break
        features[i, 0] = sub

    return features

subject_body_transformer = FunctionTransformer(subject_body_extractor)

def text_stats(posts):
    return [{"length": len(text), "num_sentences": text.count(".")} for text in posts]

text_stats_transformer = FunctionTransformer(text_stats)
```
