# 이미지 로드

`cbook`에서 `get_sample_data` 메서드를 사용하여 샘플 이미지를 로드합니다. 이 메서드는 파일과 유사한 객체를 반환하며, 이를 `imshow`에 전달하여 이미지를 표시할 수 있습니다.

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
