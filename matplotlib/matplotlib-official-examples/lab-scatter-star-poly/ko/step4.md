# 마커 사용자 정의

다음과 같은 방법으로 마커를 사용자 정의합니다.

#### 방법 1: Matplotlib 마커 심볼

`marker` 매개변수를 사용하여 Matplotlib 마커 심볼을 지정합니다.

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### 방법 2: TeX 에서 마커

`marker` 매개변수를 사용하여 TeX 기호 이름을 $-기호로 묶어 TeX 에서 마커를 지정합니다.

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### 방법 3: 경로에서 마커

`marker` 매개변수를 사용하여 (N, 2) array-like 로 N 개의 정점의 사용자 정의 경로를 지정합니다.

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### 방법 4: 정규 다각형 마커

`marker` 매개변수를 사용하여 튜플 (N, 0) 을 사용하여 정규 다각형 마커를 지정합니다.

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### 방법 5: 정규 별 마커

`marker` 매개변수를 사용하여 튜플 (N, 1) 을 사용하여 정규 별 마커를 지정합니다.

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### 방법 6: 정규 별표 마커

`marker` 매개변수를 사용하여 튜플 (N, 2) 를 사용하여 정규 별표 마커를 지정합니다.

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
