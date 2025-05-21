# 사용자 정의 제목 세로 위치 지정

때로는 제목의 세로 위치를 조정하고 싶을 수 있습니다. 이 단계에서는 플롯 제목의 세로 (y 축) 위치를 수동으로 제어하는 방법을 배우게 됩니다.

## 제목의 Y 위치 이해

제목의 세로 위치는 `title()` 함수의 `y` 매개변수를 사용하여 조정할 수 있습니다. `y` 매개변수는 정규화된 좌표 값을 허용하며, 여기서:

- `y=1.0` (기본값) 은 제목을 플롯 상단에 배치합니다.
- `y>1.0`은 제목을 플롯 상단 위에 배치합니다.
- `y<1.0`은 제목을 플롯 상단 아래에 배치하여 플롯 내용에 더 가깝게 이동합니다.

## 사용자 정의 제목 Y 위치가 있는 플롯 생성

기본값보다 높게 배치된 제목이 있는 플롯을 생성해 보겠습니다. 새 셀에 다음 코드를 입력합니다.

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # 제목을 더 높게 배치
plt.show()
```

셀을 실행합니다. 이제 제목이 기본 위치에 비해 플롯 위 약간 더 높게 표시되는 것을 확인하세요.

이제 기본값보다 낮게 배치된 제목이 있는 플롯을 생성해 보겠습니다.

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # 제목을 더 낮게 배치
plt.show()
```

셀을 실행합니다. 이제 제목이 플롯 내용에 더 가깝게 표시되어야 합니다.

## 다른 Y 위치 비교

다양한 세로 제목 위치를 비교하기 위해 여러 플롯을 나란히 생성해 보겠습니다.

```python
# 가로로 정렬된 3 개의 서브플롯이 있는 figure 생성
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 플롯 1: 기본 Y 위치
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# 플롯 2: 더 높은 Y 위치
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# 플롯 3: 더 낮은 Y 위치
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # 서브플롯 간 간격 조정
plt.show()
```

세 가지 세로 위치를 나란히 보려면 셀을 실행합니다. 이 비교는 `y` 매개변수가 제목의 세로 위치에 미치는 영향을 이해하는 데 도움이 됩니다.

## 가로 및 세로 위치 결합

`loc` 매개변수 (가로 정렬용) 를 `y` 매개변수 (세로 위치용) 와 결합하여 원하는 위치에 제목을 정확하게 배치할 수 있습니다.

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # 오른쪽 정렬 및 더 높게
plt.show()
```

셀을 실행합니다. 이제 제목이 플롯의 오른쪽 가장자리에 정렬되고 기본값보다 높게 배치되어야 합니다.
