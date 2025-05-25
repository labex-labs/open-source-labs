# 그림 및 이미지 생성

다음으로, 그림과 그 안에 배치하려는 이미지를 생성합니다. 이 예제에서는 100x100 크기의 임의 값 배열을 생성하고 이미지의 오른쪽 절반 값을 1 로 설정합니다. 그런 다음, 서로 다른 위치와 불투명도를 가진 두 개의 개별 이미지 인스턴스를 생성합니다.

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
