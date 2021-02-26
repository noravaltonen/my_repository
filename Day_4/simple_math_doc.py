def simple_add(a,b):
	"""
	Sums a and b. Returns a+b
	Parameters
	---------
	a : integer
	b : integer

	Examples:
	--------
	simple_add(2,1) = 3
	"""
    return a+b

def simple_sub(a,b):
	  """
        Subtracts b from a. Returns a-b
        Parameters
        ---------
        a : integer
        b : integer

        Examples:
        --------
        simple_sub(3,2) = 1
        """
    return a-b

def simple_mult(a,b):

 	 """
        Multiplies a and b. Returns a*b
        Parameters
        ---------
        a : integer
        b : integer

        Examples:
        --------
        simple_mult(3,2) = 6
        """
    return a*b

def simple_div(a,b):
 	 """
        Divides a and b. Returns a/b
        Parameters
        ---------
        a : integer
        b : integer

        Examples:
        --------
        simple_div(10,2)  = 5
        """
    return a/b

def poly_first(x, a0, a1):
  	"""
        Computes the polynomial of first degree.
        Parameters
        ---------
        x : integer
        a0 : integer
	a1 : integer

        Examples:
        --------
        poly_first(2,1,1)  = 3
        """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
	"""
        Computes the polynomial of second degree.
        Parameters
        ---------
        x : integer
        a0 : integer
        a1 : integer
	a2 : integer

        Examples:
        --------
        poly_second(2,1,1,2)  = 11
        """
    return poly_first(x, a0, a1) + a2*(x**2)
