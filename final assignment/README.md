## RNN Classifier

### Data specifications

The training data has 1138 input samples (integers), and every input has a label from the set {0,1}. The testing data has 394 input samples. The maximum length of an input is set to 2948, and 0 padding is done to the inputs that are of lesser length.
### RNN implementation

The RNN is implemented using the keras library in the tensorflow framework. The dimension of output of the RNN is set to 32, and the input same is of dimension (1,2948). A tanh activation is used.

This output is then fed to a sigmoid, which performs the classification. The loss function used is a standard cross-entropy loss.

This is then trained on 10 epochs.

Accuracy: 65.68%

### Running the code

To run the notebook, install python3 followed by  installation of  compatible versions of numpy, pandas, and keras (tensorflow).