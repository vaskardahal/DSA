## Binary Representation: Unsigned Integer
If $x = [x_{w-1}x_{w-2}...x_0]$ is a w-bit computer word, then the unsigned integer value stored in $x$ is: 
$$x = \sum_{k=0}^{w-1}x_kx^k$$
Example:

$$ 
\begin{align*}
x & = 0b10011101 \\ 
 & = 128 + 0 + 0 + 16 + 8 + 4 + 0 + 1 \\
 & = 157
\end{align*}
$$


## One's Complement
One's complement is a word obtained by inverting all the bits of a word. One's complement is represented by $\sim x$. 
If 

$$
\begin{align*}
x & = 0b00000000 & ==> 0  \\
\text{Then,} \\
\sim x & = 0b11111111 & ==> 255\\ 
\end{align*}
$$

## Binary Representation: Signed Integer
In the w-bit computer word signed integer is represented by reserving the most significant bit to represent the sign of the value. 
$$x = -x_{w-1}2^{w-1} + \sum_{k=0}^{w-2}x_k2^k$$
Example:

$$ 
\begin{align*}
x & = 0b11111111 \\ 
 & = -128 + 0 + 0 + 16 + 8 + 4 + 0 + 1 \\
 & = -99
\end{align*}
$$


## Two's Complement
Now let's look at the following binary number:
 $$x = 0b00000000 ==>  0 $$
 It's One's Complement is: 
$$\sim x = 0b11111111$$

Calculating the value of $\sim x$:

$$
\begin{align*}
\sim x & = \sum_{k=0}^{w-2}x_kx^k-x_{w-1}2^{w-1} \\
 & =\sum_{k=0}^{w-2}2^k-2^{w-1} \\
 & = (2^{w-1} - 1 ) - 2^{w-1}  \\
 & = -1
\end{align*}
$$

And from this, we can infer an important identity: 
$$x + \sim x = -1$$

It follows that: 
$$ -x = \sim x +1$$

Thus, negative of $x$ is equal to One's Complement of $x$ plus $1$. And this is the Two's Complement of binary number system. 

## Logical Shift of Bit
Logical shift is a bitwise operation that shifts all the bits of the operand either to the left or to the right. For the purpose of shift, the combination of the bits is treated as a sequence rather than a number. Bits can be shifted to the left or to the right. 

### Left Shift
The left shift operation shifts all the bits to the left with the leading or the most significant bit being dropped out and the 0 added to the least significant position. In Python, *n* left shifts on a number *x* is executed as `x << n`. Example:\
If 
$$x = 0b00101001 ==> 32 + 8 + 1 = 41$$
Then, 
$$x << 1 = 0b01010010 ==> 64 + 16 + 2 = 82$$
It can be observed immediately that, shifting the bits left by $1$ multiplies the operand by $2$. 

### Right Shift
The right shift operation shifts all the bits to the right with the least significant bits being dropped out and the vacated most significant posotions being padded by 0. In Python, *n* right shifts on a number *x* is executed as `x >> n`. 
If

$$
\begin{align*}
x = 0b01010010 ==> 82 \\
x' = x >> 1 = 0b00101001 ==>  41
\end{align*}
$$

Carrying out one more right shift on $x'$ 
$$x'' = x' >> 1 = 0b00010100 ==> 20$$
It's intuitively evident that shifting the bits right by 1 returns the floor of the division of the operand by $2$. 

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
