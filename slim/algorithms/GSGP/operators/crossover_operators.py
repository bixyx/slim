"""
Geometric crossover implementation for genetic programming trees.
"""

import torch


def geometric_crossover(tree1, tree2, random_tree, testing, new_data=False):
    """
    Performs geometric crossover between two trees using a random tree.

    Parameters
    ----------
    tree1 : Tree
        The first parent tree.
    tree2 : Tree
        The second parent tree.
    random_tree : Tree
        The random tree used for crossover.
    testing : bool
        Flag indicating whether to use test semantics or train semantics.
    new_data : bool
        Flag indicating whether the trees are exposed to new data. In this case, operations are performed on the inputs
        rather than semantics
    Returns
    -------
    torch.Tensor
        The result of the geometric crossover.
    """

    if new_data:
        return torch.add(
            torch.mul(tree1, random_tree),
            torch.mul(torch.sub(1, random_tree), tree2),
        )
    else:
        if testing:
            return torch.add(
                torch.mul(tree1.test_semantics, random_tree.test_semantics),
                torch.mul(torch.sub(1, random_tree.test_semantics), tree2.test_semantics),
            )
        else:
            return torch.add(
                torch.mul(tree1.train_semantics, random_tree.train_semantics),
                torch.mul(torch.sub(1, random_tree.train_semantics), tree2.train_semantics),
            )
