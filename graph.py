#!/usr/bin/env python3

import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def get_thetas():
	try:
		with open("thetas.csv", mode='r', encoding='utf-8') as f:
			print("attempting to read from thetas.csv")
			reader = csv.reader(f)
			row = next(reader)
			return float(row[0]), float(row[1])
	except (FileNotFoundError, PermissionError):
		sys.exit("Unable to read thetas.csv")

def get_data():
	try:
		with open("data.csv", mode='r', encoding='utf-8') as f:
			print("attempting to read from data.csv")
			reader = csv.reader(f)
			mileages, prices = [], []
			next(reader)
			for row in reader:
				try:
					mileages.append(float(row[0]))
					prices.append(float(row[1]))
				except (ValueError, IndexError):
					print(f"Skipping invalid row: {row}")
			return mileages, prices
	except (FileNotFoundError, PermissionError):
		sys.exit("Unable to read data.csv")

# Calculate residuals and RMSE (root mean squared error)
def print_precision(theta0, theta1, mileages, prices):
	predictions = [theta0 + theta1 * mileage for mileage in mileages]
	mean_price = np.mean(prices)
	ss_total = sum((price - mean_price) ** 2 for price in prices)
	ss_res = sum((price - prediction) ** 2 for price, prediction in zip(prices, predictions))
	rmse = np.sqrt(ss_res / len(prices))
	if ss_total == 0:
		print("R²: Undefined (all prices are the same)")
	else:
		r_squared = 1 - (ss_res / ss_total)
		if r_squared >= 0.90:
			accuracy = "very accurate"
		elif r_squared >= 0.75:
			accuracy = "mildly accurate"
		elif r_squared >= 0.50:
			accuracy = "fair"
		elif r_squared >= 0.25:
			accuracy = "mildly inaccurate"
		else:
			accuracy = "very inaccurate"
		print(f"R²: {r_squared:.4f}")
		print(f"Accuracy: {accuracy}")
	print(f"RMSE: {rmse:.4f}")

theta0, theta1 = get_thetas()
mileages, prices = get_data()
if not mileages or not prices:
	sys.exit("No data available to calculate")

plt.scatter(mileages, prices, color='blue', label='Data Points')

# regression line
min_km = min(mileages)
max_km = max(mileages)
line_x = [min_km, max_km]
line_y = [theta0 + theta1 * min_km, theta0 + theta1 * max_km]

plt.plot(line_x, line_y, color='red', label='Regression Line')

plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Car Price vs Mileage')
plt.legend()
plt.grid()

print_precision(theta0, theta1, mileages, prices)
plt.show()
