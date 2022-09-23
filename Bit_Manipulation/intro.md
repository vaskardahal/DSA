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

And this leads to important identity: 
$$x + \sim x = -1$$
It follows that: 
$$ -x = \sim x +1$$

Thus, negative of $x$ is equal to One's Complement of $x$ plus $1$. 