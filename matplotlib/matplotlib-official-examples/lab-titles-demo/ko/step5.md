# RCParams 를 사용한 전역 제목 위치 지정

이 마지막 단계에서는 Matplotlib 의 런타임 구성 매개변수 (RCParams) 를 사용하여 제목 위치 지정을 위한 전역 기본값을 설정하는 방법을 배우게 됩니다. 이는 개별적으로 각 플롯에 대해 지정할 필요 없이 노트북 또는 스크립트의 모든 플롯이 일관된 제목 위치 지정을 사용하도록 하려는 경우에 유용합니다.

## Matplotlib 에서 RCParams 이해

Matplotlib 의 동작은 `rcParams`이라는 딕셔너리 유사 변수를 사용하여 사용자 정의할 수 있습니다. 이를 통해 제목 위치 지정을 포함한 다양한 속성에 대한 전역 기본값을 설정할 수 있습니다.

## rcParams 를 사용하여 전역 제목 위치 지정 설정

제목 위치 지정을 위한 전역 기본값을 설정한 다음 이러한 설정을 자동으로 사용하게 될 몇 가지 플롯을 생성해 보겠습니다.

```python
# 현재 기본값 보기
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

셀을 실행하여 기본값을 확인합니다. 이제 이러한 설정을 수정해 보겠습니다.

```python
# 제목 위치 지정을 위한 새로운 전역 기본값 설정
plt.rcParams['axes.titley'] = 1.05     # 제목 y 위치를 더 높게 설정
plt.rcParams['axes.titlepad'] = 10     # 제목과 플롯 사이의 패딩 설정
plt.rcParams['axes.titlelocation'] = 'left'  # 기본 정렬을 왼쪽으로 설정

# 새로운 기본값을 사용할 플롯 생성
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Global RCParams Settings')
plt.show()
```

셀을 실행합니다. `title()` 함수에서 어떤 위치 지정 매개변수도 지정하지 않았음에도 불구하고 제목이 정의한 전역 설정에 따라 배치되는 것을 확인하세요.

## 동일한 설정으로 여러 플롯 생성

전역 설정을 모두 사용하는 여러 플롯을 생성해 보겠습니다.

```python
# 2x2 그리드의 서브플롯이 있는 figure 생성
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 더 쉬운 반복을 위해 축의 2D 배열을 평탄화합니다.
axes = axes.flatten()

# 전역 설정을 사용하는 제목으로 각 서브플롯에 데이터 플롯
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1} Using Global Settings')

plt.tight_layout()
plt.show()
```

셀을 실행합니다. 네 개의 모든 서브플롯 제목이 이전에 정의한 전역 설정에 따라 배치되어야 합니다.

## RCParams 를 기본값으로 재설정

RCParams 를 기본값으로 재설정하려면 `rcdefaults()` 함수를 사용할 수 있습니다.

```python
# 기본 설정으로 재설정
plt.rcdefaults()

# 기본 설정으로 플롯 생성
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Default Settings Again')
plt.show()
```

셀을 실행합니다. 이제 제목이 Matplotlib 의 기본 설정을 사용하여 배치되어야 합니다.

## 임시 RCParams 변경

코드의 특정 섹션에 대해서만 RCParams 를 일시적으로 변경하려면 컨텍스트 관리자를 사용할 수 있습니다.

```python
# 기본 설정으로 플롯 생성
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Default Settings')
plt.show()

# 이 섹션에 대해서만 RCParams 를 일시적으로 변경
with plt.rc_context({'axes.titlelocation': 'right', 'axes.titley': 1.1}):
    plt.figure(figsize=(8, 5))
    plt.plot(range(10))
    plt.grid(True)
    plt.title('Temporary Settings Change')
    plt.show()

# 다시 기본 설정을 사용할 다른 플롯 생성
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Back to Default Settings')
plt.show()
```

셀을 실행합니다. 세 개의 플롯이 표시되어야 합니다.

1. 기본 제목 위치 지정을 사용한 첫 번째 플롯
2. 오른쪽 정렬 및 더 높게 배치된 제목을 사용한 두 번째 플롯 (임시 설정으로 인해)
3. 다시 기본 제목 위치 지정을 사용한 세 번째 플롯 (임시 설정은 컨텍스트 관리자 내에서만 적용되므로)

이 접근 방식을 사용하면 나머지 플롯에 영향을 주지 않고 전역 설정에 대한 임시 변경을 수행할 수 있습니다.
