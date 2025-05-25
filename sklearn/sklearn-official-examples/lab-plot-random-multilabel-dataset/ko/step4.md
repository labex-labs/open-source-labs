# 클래스 및 특징 확률 출력

마지막으로, `plot_2d` 함수에서 반환된 클래스 확률과 특징 확률을 사용하여 각 클래스에 대한 클래스 및 특징 확률을 출력합니다.

```python
print("The data was generated from (random_state=%d):" % RANDOM_SEED)
print("Class", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["red", "blue", "yellow"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```
