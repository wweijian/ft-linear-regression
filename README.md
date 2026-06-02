# Car Price Linear Regression

This project implements a simple linear regression model from scratch using gradient descent to predict the price of a car based on its mileage.

## Project Structure

- `train.py`: Trains the model using data from `data.csv`. It performs feature normalization, executes gradient descent, and saves the resulting parameters (thetas) to `thetas.csv`.
- `predict.py`: An interactive script that loads the trained parameters and allows users to input a mileage to receive an estimated car price.
- `graph.py`: A visualization tool that displays the dataset points alongside the calculated regression line. It also provides performance metrics like $R^2$ and RMSE.
- `data.csv`: The dataset containing mileage and corresponding prices.
- `thetas.csv`: Generated file containing the intercept ($\theta_0$) and slope ($\theta_1$).

## Prerequisites

You will need Python 3 installed along with the following libraries:

```bash
pip install numpy matplotlib pydantic
```

## How to Use

### 1. Training the Model
First, generate the model parameters by training on your dataset:

```bash
python3 train.py
```
This will read `data.csv`, normalize the mileage values, and iterate to find the optimal line of best fit.

### 2. Making Predictions
Once trained, you can predict the price of a car by providing its mileage:

```bash
python3 predict.py
```
The script will prompt you for a mileage value and output the estimated price.

### 3. Data Visualization
To see the data distribution and how well the regression line fits the data:

```bash
python3 graph.py
```
This script outputs statistical metrics (Accuracy/Precision) and opens a window showing the scatter plot and the regression line.

## Methodology
- **Feature Scaling**: The training script uses Mean Normalization to ensure the gradient descent converges efficiently.
- **Gradient Descent**: The parameters are updated iteratively using a specified learning rate.
- **Evaluation**: The model quality is evaluated using the Coefficient of Determination ($R^2$) and Root Mean Square Error (RMSE).