# 이미지 로드 및 검사

이제 라이브러리를 가져왔으므로 플롯에 오버레이할 이미지를 로드해야 합니다. Matplotlib 은 연습에 사용할 수 있는 몇 가지 샘플 이미지를 제공합니다.

1. 노트북에 새 셀을 만들고 다음 코드를 입력합니다.

```python
# Load the sample image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Display information about the image
print(f"Image shape: {im.shape}")
print(f"Image data type: {im.dtype}")

# Display the image
plt.figure(figsize=(4, 4))
plt.imshow(im)
plt.axis('off')  # Hide axis
plt.title('Matplotlib Logo')
plt.show()
```

이 코드는 다음을 수행합니다.

- `cbook.get_sample_data()`를 사용하여 Matplotlib 의 샘플 데이터 컬렉션에서 'logo2.png'라는 샘플 이미지를 로드합니다.
- `image.imread()`를 사용하여 이미지 파일을 NumPy 배열로 읽습니다.
- 이미지 치수 및 데이터 유형에 대한 정보를 출력합니다.
- 그림을 만들고 `plt.imshow()`를 사용하여 이미지를 표시합니다.
- `plt.axis('off')`로 축 눈금과 레이블을 숨깁니다.
- 그림에 제목을 추가합니다.
- `plt.show()`를 사용하여 그림을 표시합니다.

2. Shift+Enter 를 눌러 셀을 실행합니다.

출력은 이미지에 대한 정보를 표시하고 Matplotlib 로고를 표시해야 합니다. 이미지 모양은 이미지의 치수 (높이, 너비, 색상 채널) 를 나타내고 데이터 유형은 이미지 데이터가 저장되는 방식을 알려줍니다.

![image-info](../assets/screenshot-20250306-cqkw4mpg@2x.png)

이 단계는 오버레이로 사용할 이미지를 이해하는 데 도움이 되므로 중요합니다. 모양과 치수를 볼 수 있으며, 이는 플롯에 이미지를 배치하는 방법을 결정할 때 유용합니다.
