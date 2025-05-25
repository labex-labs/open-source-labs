# 3D figure 및 데이터 생성

이 단계에서는 3D figure 를 생성하고 표면 플롯에 대한 테스트 데이터를 가져오겠습니다.

```python
# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Get test data for the surface plot
X, Y, Z = axes3d.get_test_data(0.05)
```
