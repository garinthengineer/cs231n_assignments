from builtins import range
import numpy as np

def affine_forward(x, w, b):
    """
    Computes the forward pass for an affine (fully-connected) layer.
    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.
    Inputs:
    - x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    - w: A numpy array of weights, of shape (D, M)
    - b: A numpy array of biases, of shape (M,)
    
    Returns a tuple of:
    - out: output, of shape (N, M)
    - cache: (x, w, b)
    """
    # first solution:
    number_of_examples = x.shape[0]
#     output_shape = b.shape[0]
#     out = []
#     for i in range(number_of_examples):
#         next_layer = []
#         for j in range(output_shape):
#             activation = np.multiply(x[i].flatten(), w[:,j]).sum() + b[j]
#             next_layer.append(activation)
#         out.append(next_layer)
#     out = np.asarray(out)

    # second solution:
    x_temp = x.reshape((number_of_examples, -1)) # -1 allows the reshape function
                                                 # to calculate the last dimention
                                                 # itself
    out = np.dot(x_temp, w) + b
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b)
    return out, cache


def affine_backward(dout, cache):
    """
    Computes the backward pass for an affine layer.

    Inputs:
    - dout: Upstream derivative, of shape (N, M)
    - cache: Tuple of:
      - x: Input data, of shape (N, d_1, ... d_k)
      - w: Weights, of shape (D, M)
      - b: Biases, of shape (M,)

    Returns a tuple of:
    - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    - dw: Gradient with respect to w, of shape (D, M)
    - db: Gradient with respect to b, of shape (M,)
    """
    x, w, b = cache
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Implement the affine backward pass.                               #
    ###########################################################################
    x_shape = x.shape
    N = x.shape[0]
    
    x_temp = x.reshape((N, -1))
    
    dx = np.dot(dout, w.T).reshape(x_shape)
    dw = np.dot(x_temp.T, dout)
    db = np.sum(dout, axis=0)
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db
