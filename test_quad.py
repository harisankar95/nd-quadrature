from nd_quad import integrateQuad
import numpy as np
from scipy import integrate

# write a pytest test function that tests the integrateQuad
# for a 1D function and compares the result to the scipy result
def test_integrateQuad_1D():
    # Define function to be integrated
    def f(x: np.ndarray) -> np.ndarray:
        return x**2
    # Define limits
    limits = [[-1., 1]]
    # Calculate integral
    res = integrateQuad(f, limits, 2)
    # Compare with scipy result
    res_scipy = integrate.quad(f, -1, 1)[0]
    assert np.isclose(res, res_scipy)

# write a pytest test function that tests the integrateQuad
# for a 2D function and compares the result to the scipy result
def test_integrateQuad_2D():
    # Define function to be integrated
    def f(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        return x**2 + y**2
    # Define limits
    limits = [[-1., 1], [-1, 1]]
    # Calculate integral
    res = integrateQuad(f, limits, 2)
    # Compare with scipy result
    res_scipy = integrate.dblquad(f, -1, 1, lambda x: -1, lambda x: 1)[0]
    assert np.isclose(res, res_scipy)

# write a pytest test function that tests the integrateQuad
# for a 3D function and compares the result to the scipy result
def test_integrateQuad_3D():
    # Define function to be integrated
    def f(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
        return x**2 + y**2 + z**2
    # Define limits
    limits = [[-1., 1], [-1, 1], [-1, 1]]
    # Calculate integral
    res = integrateQuad(f, limits, 2)
    # Compare with scipy result
    res_scipy = integrate.tplquad(f, -1, 1, lambda x: -1, lambda x: 1, lambda x, y: -1, lambda x, y: 1)[0]
    assert np.isclose(res, res_scipy)

# write a pytest test function that tests the integrateQuad
# for a 4D function and compares the result to the scipy result
def test_integrateQuad_4D():
    # Define function to be integrated
    def f(x: np.ndarray, y: np.ndarray, z: np.ndarray, w: np.ndarray) -> np.ndarray:
        return x**2 + y**2 + z**2 + w**2
    # Define limits
    limits = [[-1., 1], [-1, 1], [-1, 1], [-1, 1]]
    # Calculate integral
    res = integrateQuad(f, limits, 2)
    # Compare with scipy result
    res_scipy = integrate.nquad(f, limits)[0]
    assert np.isclose(res, res_scipy)