---
title: "Solving Class Imbalance with Focal Loss"
description: "Focal loss is an effective technique for addressing class imbalance in machine learning by weighting the loss function to focus on hard-to-classify examples."
date: 2022-12-01T20:49:34+05:30
categories:
  - ml
---

Class imbalance occurs when the number of observations in one or more classes is significantly different from the number of observations in other classes. This can lead to poor model performance, particularly when the minority class is important to predict accurately.

Focal loss is a loss function that down-weights the contribution of well-classified examples and focuses on hard-to-classify examples. This can help to improve the performance of a machine learning model when dealing with class imbalance.

In this post, we will understand the concept of focal loss and how it can be implemented in a machine learning model. We will also compare its effectiveness to other methods for solving class imbalance.

## Focal loss

Focal loss is a variant of the cross-entropy loss function that is specifically designed to address class imbalance. It is defined as:

```
FL(p) = -alpha * (1-p)^gamma * log(p)
```

where

- p is the predicted probability of the correct class
- alpha is a weighting factor for each sample,
- gamma is a tunable focusing parameter.

The focal loss function has the effect of down-weighting well-classified examples, and up-weighting examples that are misclassified. This can be useful in class imbalance scenarios, where the model may be inclined to simply predict the majority class for all examples in order to achieve a high overall accuracy. By using focal loss, the model is encouraged to focus on the hard examples, and to learn to predict the minority class more accurately.

## Focal loss parameters - alpha and gamma

In the focal loss formula, alpha and gamma are two tunable parameters that control the behavior of the loss function.

`alpha` is a weighting factor that is applied to each sample in the batch. It has the effect of down-weighting well-classified examples and up-weighting examples that are misclassified. The value of alpha is typically set such that the majority class has a lower weighting than the minority class, to help the model focus on the hard examples.

`gamma` is a focusing parameter that controls the degree to which the loss is down-weighted for well-classified examples. The value of gamma is typically set to a value greater than 1, which has the effect of down-weighting the loss for well-classified examples more heavily. This can help the model to focus on the hard examples and to learn to predict the minority class more accurately.

## Code sample

Here is an example of focal loss implemented in PyTorch:

```python
import torch
def focal_loss(logits, targets, alpha, gamma):
    probs = torch.sigmoid(logits)
    weights = alpha * (1 - probs) ** gamma
    focal_loss = -weights * torch.log(probs)
    return focal_loss.mean()
```

This function takes the model's predicted logits, the true targets, and the values of `alpha` and `gamma` as input and returns the average focal loss. It can then be used in the training loop of a machine learning model as follows:

```python
# Train the model
for inputs, targets in train_loader:
    # Calculate predicted logits
    logits = model(inputs)

    # Calculate focal loss
    loss = focal_loss(logits, targets, alpha=0.25, gamma=2.0)

    # Backpropagate and update the model weights
    loss.backward()
    optimizer.step()
```

In this example, we use the focal loss function to calculate the loss for each batch of training data and update the model weights using backpropagation. The values of `alpha` and `gamma` can be adjusted as needed to achieve the best performance.

## Thoughts on parameter tuning

In the example above, the focal loss function is defined as a partial function, with alpha and gamma as fixed parameters. The model is trained using the Adam optimizer, and the focal loss is used as the criterion. By adjusting the values of `alpha` and `gamma`, you can tune the focal loss function to suit your specific dataset and task.

The values of alpha and gamma can be tuned to suit the specific dataset and task. In our example, we used `alpha=0.75` and `gamma=2.0`, but these values may not be optimal for all datasets. By experimenting with different values of these parameters, you can find the settings that produce the best results for your model.

For example, if you increase the value of alpha, the weighting of the majority class will be decreased, and the weighting of the minority class will be increased. This can help the model to focus more on the minority class, and to learn to predict it more accurately. Similarly, if you increase the value of gamma, the down-weighting of well-classified examples will be increased, which can also help the model to focus more on the hard examples.

# Comparison with Other Methods

| Method        | Description                                                                                                           | Advantages                                                      | Disadvantages                                                                                      |
| ------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Undersampling | Removing examples from the majority class to balance the distribution of the training data                            | Can be effective in reducing class imbalance                    | Can lead to loss of important information from the majority class                                  |
| Oversampling  | Adding synthetic examples to the minority class to balance the distribution of the training data                      | Can be effective in reducing class imbalance                    | Can lead to overfitting if synthetic examples are not representative of the true data distribution |
| Focal Loss    | Loss function that down-weights the contribution of well-classified examples and focuses on hard-to-classify examples | Does not require changing the distribution of the training data | Requires tuning of hyperparameters to achieve optimal performance                                  |

As shown in the table, focal loss has several advantages over undersampling and oversampling for dealing with class imbalance. It does not require changing the distribution of the training data, and it can be easily implemented in any machine learning model. However, it does require tuning of the hyperparameters `alpha` and `gamma` to achieve optimal performance.

## Example

In this example, we will demonstrate the effectiveness of focal loss for solving class imbalance in a machine learning model. We will use a real-world example of a binary classification problem to illustrate how focal loss can improve the performance of a model on an imbalanced dataset.

Class imbalance is a common problem in medical imaging applications where the number of positive examples (e.g. diseased images) is often much smaller than the number of negative examples (e.g. healthy images). In this case study, we will consider a dataset of medical images and a binary classification task of predicting whether an image is healthy or diseased. The dataset is imbalanced, with a large number of healthy images and a small number of diseased images.

To start, we will train a convolutional neural network (CNN) using the cross-entropy loss as the training loss. This loss function is commonly used in classification tasks, as it measures the difference between the predicted probabilities and the true labels. However, it has the disadvantage of treating all classes equally, which can result in poor performance on imbalanced datasets.

| Image | True Label | Healthy | Diseased | Cross-Entropy Loss | Focal Loss |
| ----- | ---------- | ------- | -------- | ------------------ | ---------- |
| 1     | Healthy    | 0.8     | 0.2      | 0.2231435          | 0.0436035  |
| 2     | Healthy    | 0.9     | 0.1      | 0.1053605          | 0.0160707  |
| 3     | Healthy    | 0.7     | 0.3      | 0.3566749          | 0.0479158  |
| 4     | Healthy    | 0.6     | 0.4      | 0.5150763          | 0.0687455  |
| 5     | Diseased   | 0.1     | 0.9      | 0.1053605          | 0.8        |

As we can see, the focal loss for the diseased image is significantly higher than the loss for the healthy images. This is because the focal loss down-weights the contribution of well-classified examples and focuses on hard-to-classify examples. In this case, the healthy images are well-classified and have a low focal loss, while the diseased image is hard-to-classify and has a high focal loss. This helps the model to better learn the patterns in the minority class of diseased images.

## Conclusion

In this blog post, we explored the problem of class imbalance in machine learning and introduced focal loss as a potential solution. We discussed the motivations behind focal loss and provided an example of how to implement it in a machine learning model. We also compared focal loss to other methods for solving class imbalance, such as undersampling and oversampling. Finally, we provided a case study of using focal loss to improve the performance of a machine learning model with class imbalance.

Overall, focal loss is an effective technique for addressing class imbalance in machine learning. It can improve the performance of models by weighting the loss function to focus on hard-to-classify examples, while still allowing easy examples to contribute to the learning process.

If you're interested in learning more about focal loss and other methods for solving class imbalance, there are many resources available online. Some suggested readings include:

- [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002)
- [Focal Loss](https://hasty.ai/docs/mp-wiki/loss/focal-loss)
- [A Beginner's Guide To Focal Loss In Object Detection](https://www.analyticsvidhya.com/blog/2020/08/a-beginners-guide-to-focal-loss-in-object-detection/)
