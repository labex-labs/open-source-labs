# 하이퍼링크가 있는 산점도 생성

이 단계에서는 산점도를 생성하고 마커에 하이퍼링크를 추가합니다. 산점도를 생성하는 코드는 다음과 같습니다.

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

하이퍼링크를 추가하려면 산점도 객체의 `set_urls()` 메서드를 사용해야 합니다. 이 메서드는 URL 목록을 인수로 받습니다. 업데이트된 코드는 다음과 같습니다.

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

처음 두 개의 마커는 각각 `https://www.bbc.com/news` 및 `https://www.google.com/`에 대한 하이퍼링크를 갖습니다. 세 번째 마커는 하이퍼링크가 없습니다. 마지막으로, `fig.savefig()`를 사용하여 플롯을 SVG 파일로 저장할 수 있습니다.

```python
fig.savefig('scatter.svg')
```
