# 데이터셋

20 개의 주제에 대한 뉴스그룹 게시물로 구성된 20 뉴스그룹 데이터셋을 사용할 것입니다. 이 데이터셋은 특정 날짜 이전과 이후에 게시된 메시지 기준으로 학습 및 테스트 서브셋으로 분할됩니다. 실행 시간을 단축하기 위해 2 개의 카테고리 게시물만 사용할 것입니다.

```python
categories = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```
