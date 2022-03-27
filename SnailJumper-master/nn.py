import numpy as np

class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        # TODO (Implement FCNNs architecture here)
        self.layer_sizes = layer_sizes
        self.network_size = len(layer_sizes)
        self.weights = {}
        self.biases = {}

        for layer_number in range(1, self.network_size):
            self.weights[layer_number] = np.random.randn(layer_sizes[layer_number], layer_sizes[layer_number - 1])
            self.biases[layer_number] = np.zeros((layer_sizes[layer_number], 1))

        pass

    def activation(self, x, activ):
        """
        The activation function of our neural network, e.g., Sigmoid, ReLU.
        :param x: Vector of a layer in our network.
        :return: Vector after applying activation function.
        """
        # TODO (Implement activation function here)
        if(activ == "Sigmoid"):
            return 1 / (1 + np.exp(-x))
        else: #softmax
            return np.exp(x) / sum(np.exp(x))
        pass

    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        # TODO (Implement forward function here)
        layers = {}
        layers[0] = x
        for layer_number in range(1, self.network_size):
            layers[layer_number] = self.activation(
                np.matmul(self.weights[layer_number], layers[layer_number - 1]) + self.biases[
                    layer_number], "Sigmoid")
        return layers[self.network_size - 1]

        pass


