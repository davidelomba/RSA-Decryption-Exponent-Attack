# RSA Decryption Exponent Attack

![RSA Cryptography](https://img.shields.io/badge/Category-Cryptanalysis-blue) 
![Python](https://img.shields.io/badge/Language-Python-green)

An implementation of a cryptographic attack that factors the RSA modulus `n` using knowledge of the decryption exponent `d`.

## Table of Contents
- [Mathematical Background](#mathematical-background)
- [Implementation Details](#implementation-details)
- [Installation](#installation)
- [Usage](#usage)


## Mathematical Background

The attack exploits the relationship between RSA's public (`e`) and private (`d`) exponents:

1. Given `ed ≡ 1 mod φ(n)`
2. Factor `ed - 1` as `2ʳ × m`
3. Find non-trivial square roots of unity modulo `n`
4. Recover factors via GCD

## Implementation Details

### Core Functions

**Extended Euclidean Algorithm**:
```python
def euclide_esteso(a, b):
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
```

**Factorization Attack**:
```python
def decryptionexp(n, ed):
    m = ed - 1
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    # ... (full attack implementation)
    return p, q, iterations
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/davidelomba/RSA-Decryption-Exponent-Attack.git
   ```
2. Install dependencies:
   ```bash
   pip install sympy numpy
   ```

## Usage

### Basic Execution
```bash
python attacco_rsa.py
```

### Expected Output
```plaintext
[RESULTS]
Average time: 0.0523 ± 0.0017 sec
Iterations: 14.72 ± 3.21
Factors found:
p = 12345678901234567890...
q = 98765432109876543210...
```

### Advanced Options
Modify `test_decryptionexp()` in the code to:
- Change RSA bit-length (default: 1024)
- Adjust test iterations (default: 100)
- Enable verbose logging:
  ```python
  verbose = True  # in decryptionexp()
  ```
