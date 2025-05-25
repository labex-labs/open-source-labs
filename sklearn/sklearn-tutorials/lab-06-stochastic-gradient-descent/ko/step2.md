# 데이터 로드

다음으로, scikit-learn 에서 아이리스 (iris) 데이터셋을 로드합니다. 이 데이터셋은 붓꽃 (iris) 꽃의 측정값과 종 분류 레이블로 구성된, 머신 러닝 분야에서 전통적으로 사용되는 데이터셋입니다.

```python
iris = load_iris()
X = iris.data
y = iris.target
```
