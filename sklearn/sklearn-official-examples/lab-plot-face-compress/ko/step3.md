# 메모리 사용량

이제 압축된 이미지의 메모리 사용량을 확인합니다. 압축된 이미지는 원본 이미지보다 메모리를 8 배 적게 사용할 것으로 예상됩니다.

```python
print(f"RAM 에서 차지하는 바이트 수는 {compressed_raccoon_kmeans.nbytes}입니다.")
print(f"압축률: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
