# Graded

Modules for handling graded vector spaces, in conjuction with `numpy.einsum` and `torch.einsum`, specifically designed to keep track of the infamous signs.

Functions:

`signed_sort` - Take a list of integers or characters, or a string, as an input and returns as output the list sorted in ascending order, along with the sign of the permutation.

`anti_symmetrize` - Take a string as an input and return two lists as output. One list containing all permutations and the other containing the signs of the respective permutation.

`cyclic` - Take a string or list and returns the next cyclic permutation.

`anti_symmetrize_array` - Take a `numpy.array` as an input and return its anti-symmetrization if possible. Otherwise, it returns the input array.

`anti_symmetrize_tensor` - Take a `torch.tensor` as an input and return its anti-symmetrization. Otherwise, it returns the input tensor.
