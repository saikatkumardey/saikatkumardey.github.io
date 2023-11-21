---
title: "Accuracy Is a Poor evaluation Metric"
description: "Issues with using accuracy as an evaluation metric and what you should use instead"
date: 2022-06-07T10:25:15+05:30
categories:
  - ml
---

For classification problems, something like Cross-entropy is a good metric for minimizing your model's loss.
However, we need something easier to convey to the stakeholders.
Accuracy is a very easy way to show our model performances. The caveat? Accuracy would be misleading for imbalanced classes.

Here's why.

Let's say that you've built a model for detecting cancer.
Here's how the confusion matrix would look like for a dataset on cancer cases.

|                          | Predicted Cancer | Predicted cancer-free |
| ------------------------ | ---------------- | --------------------- |
| Actual cancer cases      | 10 (TP)          | 5 (FN)                |
| Actual cancer-free cases | 150 (FP)         | 800 (TN)              |

The dataset has 950 cancer-free patients and 15 patients with cancer.
The accuracy of the model = fraction of correct predictions = (10 + 800) / (10 + 5 + 150 + 800) = 0.84.

Well, the cancer cases are quite rare, so it barely has any effect on the accuracy.

If the model had predicted every case as cancer-free, the confusion matrix would look like the following:

|                          | Predicted Cancer | Predicted cancer-free |
| ------------------------ | ---------------- | --------------------- |
| Actual cancer cases      | 0 (TP)           | 15 (FN)               |
| Actual cancer-free cases | 0 (FP)           | 950 (TN)              |

Accuracy = 950/(950 + 15) = 0.984%.

That is not what we want to report to our stakeholders.

What are our options?

In such cases with class imbalance, we usually look at _precision_ and _recall_.

**Precision**

```
precision = TP/(TP + FP)
```

Precision is _out of all the cancer diagnosis made by the model, how many of them actually have cancer_. In the first case, model predicted 165 cases as having cancer but only 15 of them actually had cancer. So, the precision is 15/165 which is quite low!

**Recall**

```
recall = TP/(TP+FN)
```

Recall is _out of all the actual cancer cases, how many could the model detect?_
In the first case, model detected 15 out of 20 cancer cases. So, the recall is 15/20 = 0.75. That's not bad!

Our objective is to detect as many cancer cases as we can (TP) while minimizing the false diagnosis of cancer (FP). In other words, we want to have high recall with high precision.

All of these metrics rely on the probability threshold chosen to classify each sample as having cancer or not. If prediction probability > threshold, predict cancer.

For example, if you choose 0.9 as the threshold, you might only classify cases where the model is highly confident ie, high precision. However, you might miss out on many cases at that threshold ie, low recall. Instead, if you keep 0.1 as the threshold, you might capture all the cancer cases but you'd be scaring a lot of other cancer-free patients with misdiagnosis as well.

By varying the probability threshold, you could check the trade-off between precision & recall, also called the precision-recall curve.

Sometimes, precision & recall are combined together into one metric, called F1 score.

```
F1 = 2 / (1/precision + 1/recall)
```

There's another variant of the precision-recall curve which is agnostic to the probability threshold selected. It's called the ROC curve (Receiver Operating Characteristics). The area under the curve (AUC) is demonstrative of the overall model performance. AUC is useful to know how well the model is in classifying both the classes.

**Conclusion**

- Do not use accuracy metric when there's a class imbalance.
- Use F1 or ROC-AUC instead.

---

**Reference**

1. [Practical Machine Learning for Computer Vision](https://www.oreilly.com/library/view/practical-machine-learning/9781098102357/)

2. [Precision Recall](https://en.wikipedia.org/wiki/Precision_and_recall)

3. [ROC Curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
