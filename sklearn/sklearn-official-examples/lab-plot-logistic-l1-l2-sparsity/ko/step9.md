# 결과 출력

각 모델의 희소성 (sparsity) 과 점수 (score) 를 출력합니다.

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("L1 페널티를 사용한 희소성:", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("탄성 네트 페널티를 사용한 희소성:", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("L2 페널티를 사용한 희소성:", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("L1 페널티를 사용한 점수:", score_l1_LR))
    print("{:<40} {:.2f}".format("탄성 네트 페널티를 사용한 점수:", score_en_LR))
    print("{:<40} {:.2f}".format("L2 페널티를 사용한 점수:", score_l2_LR))
```
