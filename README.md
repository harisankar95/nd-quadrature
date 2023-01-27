# nd-quadrature

Generate n-Dimensional gaussian quadrature points and weights.

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
git clone
cd nd-quadrature
```

## References

1. [Gauss-Legendre quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature)