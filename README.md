# RandomFunction
Runs a random function between the given list. The ratio of possibility can be used.

## Installation
This module consists of only one file([rfpy.py](https://github.com/jym0404/RandomFunction/blob/main/rfpy.py)).

So there are ways to import it by **copying that single file**, or by **cloning or downloading the repository**.

## Usage
This module only contains one function.

    random_execute(functions, ratios[Optional])

Functions and ratios **must be iterable**,** and it is **recommended to use tuples**.

Functions must contain **the names of the function**, and the functions **must not receive any parameters**.

If any **function takes parameters**, this will **cause an error**. However, if default values ​​are defined for all parameters of the all functions, it will be operated with those default values.

Ratios must be composed of **numeric objects**, and it is **recommended that they be composed of int**.

## Example

The codes below execute a and b with a 25% probability, and c with a 50% probability.

    random_execute((a, b, c), (1, 2, 1))

    random_execute((a, b, c), (25, 50, 25))

    random_execute((a, b, c), ratios=(25, 50, 25))

If the function is executed without ratios as shown below, a, b, and c are executed with equal probability.

    random_execute((a,b,c))

## License
This repository is licensed under the [MIT license](https://github.com/jym0404/RandomFunction/blob/main/LICENSE).