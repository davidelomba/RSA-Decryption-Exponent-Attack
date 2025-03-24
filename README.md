# RSA Decryption Exponent Attack

This project implements an attack on RSA using the decryption exponent, based on modular arithmetic and prime factorization.

## Project Description

The code demonstrates how to:
1. Generate RSA parameters (`n`, `e`, `d`, `p`, `q`)
2. Perform the extended Euclidean algorithm
3. Recover prime factors from the decryption exponent
4. Measure attack performance

## Key Features

### Extended Euclidean Algorithm
```python
def euclide_esteso(a, b):
    # Implementation details...
    return gcd, x, y
```

### Decryption Exponent Attack
```python
def decryptionexp(n, ed):
    # Attack implementation...
    return p, q, iterations
```

## Requirements
- Python 3.x
- Libraries:
  ```bash
  pip install sympy numpy
  ```

## Usage

1. Save the main code as `attacco_rsa.py`
2. Run the attack:
   ```bash
   python rsa_attack.py
   ```

## Mathematical Basis
The attack exploits:
1. Factorization of `ed - 1 = 2^r * m`
2. Modular square roots properties:
   ```math
   x^(2^j * m) ≡ 1 mod n
   ```
