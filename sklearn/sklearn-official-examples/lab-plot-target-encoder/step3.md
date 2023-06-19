# Native Categorical Feature Support

In this section, we build and evaluate a pipeline that uses native categorical feature support in `HistGradientBoostingRegressor`, which only supports up to 255 unique categories. We group the categorical features into low cardinality and high cardinality features. The high cardinality features will be target encoded and the low cardinality features will use the native categorical feature in gradient boosting.


