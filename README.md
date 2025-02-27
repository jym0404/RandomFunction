[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjym0404%2FRandomFunction&count_bg=%238FE1E6&title_bg=%23949494&icon=&icon_color=%23FFFFFF&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
# RandomFunction
Runs a random function between the given list. The ratio of possibility can be used.

## Installation
This module consists of only one file([rfpy.py](https://github.com/jym0404/RandomFunction/blob/main/rfpy.py)).

So there are ways to import it by **copying that single file**, or by **cloning or downloading the repository**.

## Usage
This module only contains one function.

    random_execute(functions, ratios[Optional], args[Optional])

Functions and ratios **must be iterable**,** and it is **recommended to use tuple**.
Args **must be iterable**, and it is **recommended to use list**.
The objects inside the Args **must be iterable**, and it is **recommended to use list or dictionary**.

Functions must contain **the names of the function**.

Ratios must be composed of **numeric objects**, and it is **recommended that they be composed of int**.

Args must contain **The iterable objects that contain arguments of the functions**.

The length of the args **must be equal to the that of the functions or 1**

If the length of the args equals to the that of the functions, The object inside args will be selected **according to its index and passed to the function**.

If the length of the args equals to 1, the **same arguments will be used for all functions**.

>**Caution**<br>
>String is also iterable, the code below splits the string into characters and passes them to the function.
>```python
>random_execute((a,b), args=["Hello, World!"])
>```

## Example

The codes below execute a and b with a 25% probability, and c with a 50% probability.
```python
random_execute((a, b, c), (1, 2, 1))

random_execute((a, b, c), (25, 50, 25))

random_execute((a, b, c), ratios=(25, 50, 25))
```
If the function is executed without ratios as shown below, a, b, and c are executed with equal probability.
```python
random_execute((a, b, c))
```
The code below executes a and b with a 50% probability, passing `"a"` to a and `"b1","b2"` to b.
```python
random_execute((a, b), (1, 1), [["a"], ["b1", "b2"]])
```
## License
This repository is licensed under the [MIT license](https://github.com/jym0404/RandomFunction/blob/main/LICENSE).