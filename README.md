# README.md

## HC-128 Algorithm Implementation

This repository contains Python code implementing the HC-128 stream cipher algorithm. HC-128 is a stream cipher designed by Hongjun Wu, which was one of the final candidates of the eSTREAM project by the European Union's ECRYPT network.

### Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [References](#references)

### Introduction

The HC-128 algorithm is a software-efficient stream cipher that operates on 32-bit words. It provides high security with low computational cost and is suitable for various applications that require encryption, such as secure communications and data protection.

### Usage

To use this implementation, follow these steps:

1. **Initialization**: Initialize the algorithm by calling the `init(K, IV)` function, where `K` is the encryption key and `IV` is the initialization vector.
   
   ```python
   init("0123456789ABCDEF0123456789ABCDEF", "FEDCBA9876543210FEDCBA9876543210")
   ```

2. **Key Generation**: Generate a key stream by calling the `keygen()` function.

   ```python
   key_stream = keygen()
   ```

3. **Encryption/Decryption**: XOR the plaintext/ciphertext with the generated key stream to perform encryption or decryption.

### Implementation Details

The implementation includes the following components:

- **Initialization**: The `init(K, IV)` function initializes the algorithm with a given encryption key `K` and initialization vector `IV`.
- **Key Generation**: The `keygen()` function generates a key stream for encryption or decryption.
- **Helper Functions**: Various helper functions are provided for conversion between hexadecimal, bytes, and integers, as well as for bitwise operations.
- **HC-128 Functions**: The HC-128 algorithm consists of several functions (`f1`, `f2`, `g1`, `g2`, `h1`, `h2`) used in the key generation process.
- **Global Variables**: Global variables `P`, `Q`, and `i` are used to maintain the state of the algorithm.

### References

- Hongjun Wu, "The Stream Cipher HC-128," *The ECRYPT Stream Cipher Project*, 2008. [PDF](https://www.ecrypt.eu.org/stream/p3ciphers/hc/hc128_p3.pdf)
- eSTREAM: The ECRYPT Stream Cipher Project. [Website](https://www.ecrypt.eu.org/stream/)
- Wikipedia contributors. "HC-128." *Wikipedia, The Free Encyclopedia.* [Link](https://en.wikipedia.org/wiki/HC-128)

For more details on the HC-128 algorithm and its implementation, refer to the provided code and the referenced materials.
