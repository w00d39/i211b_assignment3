# Iris Data Analysis
Uses the pandas library 
## Overview

This project analyzes the Iris dataset by calculating various statistical measures such as the average, median, standard deviation, and correlation for different species of irises. The dataset consists of measurements of petal and sepal lengths and widths for three species of irises: setosa, versicolor, and virginica.

## Files

- `assignment3.py`: The main script that performs the data analysis.
- `Petal_Data.csv`: The CSV file containing petal measurements.
- `Sepal_Data.csv`: The CSV file containing sepal measurements.


## Usage

1. Place the [Petal_Data.csv](http://_vscodecontentref_/0) and [Sepal_Data.csv](http://_vscodecontentref_/1) files in the same directory as [assignment3.py](http://_vscodecontentref_/2).
2. Run the [assignment3.py](http://_vscodecontentref_/3) script:
    ```bash
    python assignment3.py
    ```

## Functions

### [corr_iris()](http://_vscodecontentref_/4)
Calculates the correlation between variables for each iris species.

### [avg_iris()](http://_vscodecontentref_/5)
Calculates the average of each variable for all species in the dataset.

### [median_iris()](http://_vscodecontentref_/6)
Calculates the median of each variable for all species in the dataset.

### [sd_iris()](http://_vscodecontentref_/7)
Calculates the standard deviation of each variable for all species in the dataset.

## Output

The script prints the following:
- Average values for each variable grouped by species.
- Median values for each variable grouped by species.
- Standard deviation values for each variable grouped by species.
- Correlation matrix for each species.

## Analysis

Based on the calculated statistics and correlation matrices, the versicolor and virginica irises are the most similar, especially when looking at the petal measurements. The setsosa irises are the least similar to the other two species, although they are closer to the versicolor irises in terms of sepal width.

## Conclusion

The analysis shows that while all three species of irises are similar, the versicolor and virginica irises are more closely related to each other compared to the setsosa irises.
