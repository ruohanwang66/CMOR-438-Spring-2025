# Overview of K-Nearest Neighbors Method

![KNN pic 1](./knn_pic1.png)

K-Nearest Neighbors (KNN) is a non-parametric, instance-based supervised learning algorithm used for both classification and regression. For classification tasks, it assigns a label to a test point based on the majority vote of its *k* nearest neighbors in the training set.

Instead of learning an explicit mapping function, KNN simply stores the training data and delays computation until prediction time, making it a type of lazy learning algorithm that doesnt rely on training. The underlying assumption is that similar input features should produce similar outcomes.

Distance metrics—typically Euclidean—are used to identify the nearest neighbors, and the number of neighbors (*k*) is a critical hyperparameter. Too small a *k* may overfit, while too large a k may smooth over decision boundaries too much.

![KNN pic 2](./knn_pic2.png)


# Strengths

- No Training Step; KNN is trivially simple to implement and doesn’t require a model-fitting step, making it quick to set up for initial testing.

- Non-linear Boundaries: It can capture complex decision boundaries without requiring transformations of the feature space.

- Intuitive: The logic behind the algorithm is straightforward—label points by their closest examples.


# Weaknesses

- Prediction Time Since all computations are deferred to inference, KNN is computationally expensive when predicting, especially on large datasets.

- Feature Scaling Sensitivity As it relies on distances, feature scaling (e.g., standardization) is critical. Unscaled features lead to misleading neighbor proximity.

- Storage Cost KNN stores the entire dataset in memory, making it space-inefficient.

- No Model Interpretability Unlike linear models, KNN offers no insights into feature importance or relationships.

KNN is most appropriate when:

* The dataset is small to medium in size.
* The relationship between features and class labels is complex or highly non-linear.
* Real-time prediction speed is not a priority.




# Implementation

Our KNN implementation involved:

* Standardizing the dataset using `StandardScaler` to ensure all features contribute equally to distance calculations.
* Reducing dimensionality using PCA for more effective distance-based classification.
* Evaluating model performance across a range of *k* values from 1 to 19 using classification error as the metric.
* Selecting the *k* value with the lowest error (k = 9), and analyzing predictions using a confusion matrix.

We visualized:

* Error rates across k values.
* Model predictions vs. actual diagnoses in a table.
* The final confusion matrix showing true/false positives and negatives.


# Overview of the Dataset

* As with logistic regression, this project uses the [Wisconsin Breast Cancer](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) dataset.
* Each observation includes features like radius, concavity, texture, and area, alongside a diagnosis label (0 = Malignant, 1 = Benign).
* Feature selection and standardization were performed before applying PCA and fitting the model.



# To Replicate Results - 

- Just as all other methods, code blocks are implemented in the exact order that they should be executed, with instructions if applicable. I've ran the program from top to bottom, your results should be close to what I have written in the remarks. 
