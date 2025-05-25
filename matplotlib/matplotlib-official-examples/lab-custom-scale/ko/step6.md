# 사용자 정의 스케일 사용

이제 플롯에서 사용자 정의 스케일을 사용할 수 있습니다. 다음은 Mercator 투영법에서 위도 데이터에 사용자 정의 스케일을 사용하는 예입니다.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = np.radians(t)/2.

    plt.plot(t, s, '-', lw=2)
    plt.yscale('mercator')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Mercator projection')
    plt.grid(True)

    plt.show()
```
