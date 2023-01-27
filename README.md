# nd-quadrature

Generate n-Dimensional gaussian quadrature points and weights. Integrate n-Dimensional functions using the generated quadrature points and weights. This is a python implementation of the algorithm described in [1] for educational purposes. The algorithm is not optimized for speed. Please use a more optimized implementations for production like [scipy.integrate.nquad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.nquad.html).

## Usage

```python
from nd_quad import getQuad, integrateQuad

# Get the Legendre-Gauss quadrature points and weights for a 2D function
# with 2nd order accuracy in each dimension
# order = 2n - 1, where n is the number of quadrature points
# so order = 2 for 2 points, 4 for 3 points, 6 for 4 points, etc.

points, weights = getQuad(2, 2)

# Integrate a function using the integrateQuad function
# Define function to be integrated
def f(x: np.ndarray, y: np.ndarray, z: np.ndarray, w: np.ndarray) -> np.ndarray:
    return x**2 + y**4 + z**3 + w

# Define limits
limits = [[-1., 4], [-3, -1], [0, 3], [2, 5]]

# Integrate function
result = integrateQuad(f, limits, 3)
```

## Development

```bash
git clone https://github.com/harisankar95/nd-quadrature.git path/to/nd-quadrature
cd path/to/nd-quadrature
```

## Testing

```bash
cd path/to/nd-quadrature
pytest
```

## References

1. [Gauss-Legendre quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature)