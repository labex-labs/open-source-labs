# Train predictive models with partial observations

We train a predictive model again, but this time we omit the ability feature, which is not observed or is only estimated from proxies that inadvertently measure education as well (e.g. by IQ tests). We predict the hourly wages again using features like experience, parent hourly wage, and college degree. We then check if the coefficient of the model are different from the true generative model. To compensate for the omitted variable, the model inflates the coefficient of the college degree feature. Therefore, interpreting this coefficient value as a causal effect of the true generative model is incorrect.


