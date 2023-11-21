---
title: "Building Pandas Dataframes From Ndarrays"
description: "How to convert multi-dimensional numpy arrays to pandas dataframe?"
date: 2021-09-28T10:06:23+05:30
categories:
  - "coding"
  - "python"
---

At work, I have to switch between numpy & pandas depending on the computational needs. Numpy is faster. Pandas is easier to work with.

One of the tasks I've faced often was to convert a 3-dimensional ndarray to a pandas dataframe. I will share my preferred technique in this post today.

For the purpose of this exercise, I'll generate dummy sales data for a retail company. The dimensions include products, locations, and sales.

# Convert ndarray to pandas dataframe

```python
import pandas as pd
import numpy as np
```

## 1d : dimension = sales

Let's start with 1d data. What if we only had sales info for all products and locations?

```python
arr_1d = np.random.randint(
    low=1,
    high=10,
    size=3,
)
print(arr_1d)
```

    [9 3 6]

That's easy. Ideally, 1-d information should be represented as a Series.

```python
df_1d = pd.DataFrame(arr_1d, columns=["sales"])
print(df_1d)
```

       sales
    0      9
    1      3
    2      6

## 2d: dimension = sales \* product

Let's move on to 2 dimensions. Now, we have data corresponding to different products.

```python
arr_2d = np.random.randint(
    low=1,
    high=10,
    size=(3, 2),
)
print(arr_2d)
```

    [[4 6]
     [8 1]
     [2 7]]

Pandas DataFrame can handle 2-D ndarrays out of the box.

```python
df_2d = pd.DataFrame(arr_2d, columns=["product", "sales"]).set_index("product")
print(df_2d)
```

             sales
    product
    4            6
    8            1
    2            7

## 3d : dimension = location x product x sales

Now, what if we have a ndarray corresponding to all products for several locations?

```python
# failure
arr_3d = np.random.randint(
    low=1,
    high=10,
    size=(5, 3, 1),
)
print(arr_3d)
```

    [[[9]
      [6]
      [2]]

     [[1]
      [4]
      [4]]

     [[2]
      [5]
      [6]]

     [[9]
      [6]
      [5]]

     [[1]
      [6]
      [1]]]

```python
# the following raises ValueError
# pandas DataFrame expects a 2-d input
df_3d = pd.DataFrame(arr_3d, columns=["location", "product", "sales"])
```

pandas won't work out of the box. It cannot handle more than 2 dimensions. So, it raises a `ValueError`.

```bas
    ---------------------------------------------------------------------------


    ValueError                                Traceback (most recent call last)

    /var/folders/jq/ksxbjg7d58g9v9rrcl0f38380000gn/T/ipykernel_12628/1531564731.py in <module>
          1 # the following raises ValueError
          2 # pandas DataFrame expects a 2-d input
    ----> 3 df_3d = pd.DataFrame(arr_3d, columns=["location", "product", "sales"])
    .
    .
    .
    ValueError: Must pass 2-d input. shape=(5, 3, 1)
```

The solution?

`MultiIndex`.

Assuming that the ndarray is ordered by location/products, we could prepare a multi-index, flatten our ndarray and let Pandas reshape it according to the provided index.

Sweet!

```python
index = pd.MultiIndex.from_product(
    [range(dim) for dim in arr_3d.shape[:-1]],
    names=["location", "product"],
)

df_3d = pd.DataFrame(arr_3d.flatten(), index=index, columns=["sales"])
print(df_3d)
```

                      sales
    location product
    0        0            9
             1            6
             2            2
    1        0            1
             1            4
             2            4
    2        0            2
             1            5
             2            6
    3        0            9
             1            6
             2            5
    4        0            1
             1            6
             2            1

We just have sales corresponding to each location and product. What if the final `sales` dimension includes sales for yesterday/today (or for every month, every week, etc.) ?

## 3d : dimension = location x product x sales (multi)

```python
arr_3d = np.random.randint(
    low=1,
    high=10,
    size=(5, 3, 2),
)
print(arr_3d)
index = pd.MultiIndex.from_product(
    [range(dim) for dim in arr_3d.shape],
    names=["location", "product", "sales"],
)
```

    [[[1 9]
      [8 6]
      [9 4]]

     [[4 9]
      [3 9]
      [1 8]]

     [[5 2]
      [9 9]
      [1 9]]

     [[4 5]
      [7 4]
      [7 7]]

     [[6 9]
      [4 2]
      [7 1]]]

No major changes. Pandas should handle it just like before. Just unstack the sales dimension and rename the columns for readability.

```python
df_3d = pd.DataFrame(
    arr_3d.flatten(),
    index=index,
    columns=["sales"],
)
df_3d = df_3d.unstack(-1).rename(
    columns={0: "yesterday", 1: "today"},
)
print(df_3d)
```

```
    sales            yesterday today
    location product
    0        0               1     9
             1               8     6
             2               9     4
    1        0               4     9
             1               3     9
             2               1     8
    2        0               5     2
             1               9     9
             2               1     9
    3        0               4     5
             1               7     4
             2               7     7
    4        0               6     9
             1               4     2
             2               7     1
```

Do you know of other ways to switch between ndarray and DataFrame? Comment below :)
