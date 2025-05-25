# 자기 상관 관계 플롯

이제 Matplotlib 의 `acorr` 함수를 사용하여 `x` 배열의 자기 상관 관계를 플롯합니다.

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

`acorr` 함수는 다음과 같은 매개변수를 사용합니다:

- `x`: 자기 상관 관계를 계산할 데이터 배열
- `usevlines`: 부울 (boolean), 상관 값에서 수직선을 그릴지 여부
- `normed`: 부울, 상관 값을 정규화할지 여부
- `maxlags`: 정수, 상관 관계를 계산할 최대 래그 (lag) 수
- `lw`: 정수, 플롯의 선 너비
