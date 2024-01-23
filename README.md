# VectorMath

A vector has 3 component values, such as (1, 3, 2) and is naturally storable as an array.
- Addition of vectors requires addition of the corresponding elements.
- A dot product is the sum of the products of corresponding elements.
- The norm of a single vector is the square root of the sum of the squares of the elements.
 
# ‘vectormath.py’ 

A function that can do basic vector calculations in 3 dimensions:

Suppose that we have 2 vectors: A=(1, 3, 2) and B=(2, 3, 0):
- Addition:
A+B = (1+2, 3+3, 2+0) = (3, 6, 2)
- Dot product:
A.B = 1.2 + 3.3 + 2.0 = 2 + 9 = 11
- Norm (of A):
|A| = Sqrt(1^2 + 3^2 + 2^2) = Sqrt(1+9+4) = Sqrt(14) = 3.74
- Norm (of B):
|B| = Sqrt(2^2 + 3^2 + 0^2) = Sqrt(4+9+0) = Sqrt(13) = 3.61