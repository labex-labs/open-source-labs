# Interpret Calibration Curves

The calibration curves show the relationship between predicted probabilities and actual outcomes for each model. Well-calibrated models produce curves that follow the diagonal line, indicating that predicted probabilities match actual outcomes. The four models produce different results:

- Logistic regression produces well-calibrated predictions as it directly optimizes log-loss.
- Gaussian Naive Bayes tends to push probabilities to 0 or 1, mainly because the naive Bayes equation only provides a correct estimate of probabilities when the assumption that features are conditionally independent holds.
- Random Forest Classifier shows the opposite behavior: the histograms show peaks at approx. 0.2 and 0.9 probability, while probabilities close to 0 or 1 are very rare.
- Linear SVM shows an even more sigmoid curve than the Random Forest Classifier, which is typical for maximum-margin methods.


