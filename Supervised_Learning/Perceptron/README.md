# Overview of Perceptron method - 
The perceptron is a basic function that can perform tasks such as binary classification by mimicing the human neuron. It takes in n inputs each representing a feature, and assigns a weight to each one to reflect its importance. These weighted inputs are then summed and passed through an activation function, typically a step function, to produce a binary output.

The perceptron functions as a binary classifier, learning to separate data into two classes by adjusting the weights during training. Training is done using labeled examples: the model compares its prediction to the known label and updates the weights using the Perceptron Learning Rule, which minimizes classification error over time.

For training, we provide the network with inputs with known binary classifications. We apply the Perceptron Learning Rules to force the model to adapt to the dataset and "Learn".

- The core components of a perceptron are:

Summation function: Computes the weighted sum of given inputs.

Activation function: Applies a threshold to decide the final output (e.g., 0 or 1, -1 or 1).

** A single-layer perceptron can only classify linearly separable data. For more complex tasks, multi-layer versions (i.e., neural networks) are required. **




# Overview of the Dataset - 
- Here we will implement perceptron on survival data of passengers aboard the Titanic. Each passenger includes their survivorship status(0 - didn't survive, 1 - survived), and various attributes such as PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked. 

- Based on some choice/combinations of the attributes, we'll try to predict the survival of the passengers

- Stored in the 'data' folder in the main Repo and referenced automatically


# To Replicate Results - 
- Methods are implemented in the exact order that they should be executed, and I have left instructions and remarks at every step. I've ran the program from top to bottom, your results should be exactly what I got. 

- Since I ran the analysis on two seperate parts of the data, clearing the cache and rerunning from the beginning should resolve any issues that may arise