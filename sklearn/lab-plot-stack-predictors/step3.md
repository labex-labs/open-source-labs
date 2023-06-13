# Step  3: Stack of predictors on a single data set

Now we can use Ames Housing dataset to make the predictions. We check the performance of each individual predictor as well as of the stack of the regressors. We combine 3 learners (linear and non-linear) and use a ridge regressor to combine their outputs together. The stacked regressor will combine the strengths of the different regressors. However, we also see that training the stacked regressor is much more computationally expensive.


