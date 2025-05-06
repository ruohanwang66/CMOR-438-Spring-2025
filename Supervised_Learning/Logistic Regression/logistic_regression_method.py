import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class SingleNeuron(object):
    """
    A class used to represent a single artificial neuron. 

    ...

    Attributes
    ----------
    activation_function : function
        The activation function applied to the preactivation linear combination.
    
    cost_function : function
        The cost function used to measure model performance.

    w_ : numpy.ndarray
        The weights and bias of the single neuron. The last entry being the bias. 
        This attribute is created when the train method is called.

    errors_: list
        A list containing the mean sqaured error computed after each iteration 
        of stochastic gradient descent per epoch. 

    Methods
    -------
    train(self, X, y, alpha = 0.005, epochs = 50)
        Iterates the stochastic gradient descent algorithm through each sample 
        a total of epochs number of times with learning rate alpha. The data 
        used consists of feature vectors X and associated labels y. 

    predict(self, X)
        Uses the weights and bias, the feature vectors in X, and the 
        activation_function to make a y_hat prediction on each feature vector. 
    """
    def __init__(self, activation_function, cost_function):
        self.activation_function = activation_function
        self.cost_function = cost_function

    def train(self, X, y, alpha = 0.005, epochs = 50):
   
        self.w_ = np.random.rand(1 + X.shape[1])
        self.errors_ = []
        N = X.shape[0]

        for _ in range(epochs):
            errors = 0
            for xi, target in zip(X, y):
                error = (self.predict(xi) - target)
                self.w_[:-1] -= alpha*error*xi
                self.w_[-1] -= alpha*error
                #errors += .5*((self.predict(xi) - target)**2)
                errors += self.cost_function(self.predict(xi), target)
            self.errors_.append(errors/N)
        return self

    def predict(self, X):
        preactivation = np.dot(X, self.w_[:-1]) + self.w_[-1]
        return self.activation_function(preactivation)

    def plot_cost_function(self):
        fig, axs = plt.subplots(figsize = (10, 8))
        axs.plot(range(1, len(self.errors_) + 1), 
                self.errors_,
                label = "Cost function")
        axs.set_xlabel("epochs", fontsize = 15)
        axs.set_ylabel("Cost", fontsize = 15)
        axs.legend(fontsize = 15)
        axs.set_title("Cost Calculated after Epoch During Training", fontsize = 18)
        plt.show()

    def plot_decision_regions(self, X, y, clf, resolution=0.02):
        # Set up marker generator and color map
        markers = ('s', 'x')
        colors = ('magenta', 'lightseagreen')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        # Only works for 1 or 2 features
        if X.shape[1] == 1:
            x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
            xx = np.arange(x_min, x_max, resolution).reshape(-1, 1)
            Z = clf.predict(xx)  # This will give class labels, not probabilities
            plt.plot(xx, Z, color='black', linewidth=2)
        elif X.shape[1] == 2:
            x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
            x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
            xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                                np.arange(x2_min, x2_max, resolution))
            grid = np.array([xx1.ravel(), xx2.ravel()]).T
            
            # Get predictions (class labels) for the grid
            Z = clf.predict(grid)  # This should give class labels
            Z = Z.reshape(xx1.shape)  # Reshape to match grid shape
            
            # Use contourf to fill the regions based on predicted class
            plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        else:
            raise ValueError("Only 1D or 2D input is supported for visualization")

        # Plot class samples
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y == cl, 0],
                        y=np.zeros_like(X[y == cl, 0]) if X.shape[1] == 1 else X[y == cl, 1],
                        alpha=0.8,
                        c=[cmap(idx)],
                        marker=markers[idx],
                        label=f"Class {cl}")
                    
    def plot_decision_boundary(self, X, y, xstring="x", ystring="y"):
        plt.figure(figsize=(10, 8))
        self.plot_decision_regions(X, y, clf=self)
        plt.title("Neuron Decision Boundary", fontsize=18)
        plt.xlabel(xstring, fontsize=15)
        plt.ylabel(ystring, fontsize=15)
        plt.show()
