"""
.. module:: average
   :platform: Unix, Windows
   :synopsis: A simple averaging function.

.. moduleauthor:: Ferdinand van Wyk <ferdinandvwyk@gmail.com>

"""

def avg(vec):
    """This function prints calculates the average of a vector.

    :param array vec: An input vector. 
    :returns: float
    :raises: AttributeError, KeyError

    """
    return float(sum(vec))/len(vec)
