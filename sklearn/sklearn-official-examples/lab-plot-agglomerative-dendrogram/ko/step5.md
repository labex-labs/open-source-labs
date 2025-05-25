# 데ンドログラム 시각화

`scipy.cluster.hierarchy` 모듈의 `dendrogram()` 함수와 원본 코드에서 정의된 `plot_dendrogram()` 함수를 사용하여 데ンドログラム을 시각화합니다.

```python
plt.title("계층적 군집 데ンドログラム")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("노드 내 점의 개수 (괄호 없으면 점의 인덱스).")
plt.show()
```
