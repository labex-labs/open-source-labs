# Figure 및 Axes 객체 생성

이제 `add_subplot()` 메서드를 사용하여 figure 및 axes 객체를 생성합니다. 3D 플롯을 생성하기 위해 `projection` 매개변수를 `'3d'`로 설정합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```
