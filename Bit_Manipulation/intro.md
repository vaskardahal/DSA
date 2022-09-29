## Binary Representation
If $x = [x_{w-1}x_{w-2}...x_0]$ is a w-bit computer word, then the unsigned integer value stored in $x$ is: 
$$x = \sum_{k=0}^{w-1}x_kx^k$$
And the signed integer value stored in x is: 
$$x = \sum_{k=0}^{w-2}x_k2^k-x_{w-1}2^{w-1}$$

## One's Complement
One's complement is nothing but all the bits of a word flipped. One's complement is represented by $\sim x$. 

## Two's Complement
What is the value of $x = 0b00000000$? $0$

What is the value of $x = 0b11111111$? 
$$x = \sum_{k=0}^{w-2}x_kx^k-x_{w-1}2^{w-1}$$

$$x =\sum_{k=0}^{w-2}2^k-2^{w-1}$$

$$x = (2^{w-1} - 1 ) - 2^{w-1} $$

$$x = -1$$

And from this, we can infer an important identity: 
$$x + \sim x = -1$$

It follows that: 
$$ -x = \sim x +1$$

Thus, negative of $x$ is equal to One's Complement of $x$ plus $1$. 

## Setting the kth Bit
Problem: Set the kth bit in a word x to 1 \
Solution: Shift 1 by k bits, and then OR with x:

$$ y = x | (1 << k) $$


## Clearing the kth Bit
Problem: Clear the kth bit in a word x (change it to 0) \
Solution: Shift 1 by k bits, One's complement and AND with x:

```math
y = x  \&  \sim (1 << k)
```

## Toggling the kth Bit
Problem: Toggle the kth bit in a word x \
Solution: Shift 1 by k bits, XOR: 

$$ y = x \wedge (1 << k) $$

## Extract a Bit Field
Problem: Extract a contiguous bit field from a word x \
Solution: Mask at the window, and then right shift:

```math
(x \& mask) >> shift
``` 

## Set a Bit Field
Problem: Set a continguous bit field in a word x to a value y
Solution: Invert the mask to clear the field first, and then OR the shifted value to the field: 

```math
(x \& ~mask) | (y << shift)
``` 
For safety purpose, it is a good idea to mask the shifted value of y too before its OR with x. 

## Ordinary Swap
