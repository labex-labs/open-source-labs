# 이미지를 경계의 기울기 값을 가진 그래프로 변환

이미지를 경계의 기울기 값을 가진 그래프로 변환합니다. 베타 값이 작을수록 분할이 실제 이미지에 덜 의존적입니다. 베타=1 일 경우, 분할은 볼로노이 (Voronoi) 에 가깝습니다.

```python
# 이미지를 경계의 기울기 값을 가진 그래프로 변환합니다.
graph = image.img_to_graph(rescaled_coins)

# 기울기의 감소 함수 (지수 함수) 를 적용합니다.
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```
