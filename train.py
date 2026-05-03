#!/usr/bin/env python3

import csv
import sys
from pydantic import BaseModel, ValidationError 
import numpy as np

file_path = "data.csv"
thetas_path = "thetas.csv"

class PriceEstimation(BaseModel):
	km: float
	price: float

def get_price_history():
	mileages, prices = [], []
	try:
		with open(file_path, mode='r', encoding='utf-8') as f:
			print("attemting to read from data.csv")
			reader = csv.DictReader(f)
			invalidCount = 0;
			for row in reader:
				try:
					estimation = PriceEstimation(**row)
					mileages.append(estimation.km)
					prices.append(estimation.price)
				except ValidationError:
					invalidCount += 1
			print(f"number of lines skipped due to ValidationError: {invalidCount}")
	except (PermissionError, FileNotFoundError):
		sys.exit("no read and write permission given for data.csv")
	return mileages, prices;

def normalize_mileage(mileages: list[float]):
	normalized_mileage = []
	for mileage in mileages:
		normalized = (mileage - np.mean(mileages)) / np.std(mileages)
		normalized_mileage.append(normalized)
	return normalized_mileage

def write_thetas(theta0: float, theta1: float):
	try:
		with open(thetas_path, mode='w', encoding='utf-8') as f:
			f.write(f"{theta0}, {theta1}\n")
			print(f"theta0: {theta0} and theta1: {theta1} written to thetas.csv")
	except PermissionError:
		sys.exit("no write permission given for thetas.csv")
	return 

# script here

mileages, prices = get_price_history()
learning_rate, iterations = 0.1, 1000
theta0, theta1 = 0, 0
m = len(prices)

if m == 0:
	sys.exit("no training data available")
if np.std(mileages) == 0:
	sys.exit("mileages has no meaningful variation")

normalized_mileage = normalize_mileage(mileages)

for _ in range(iterations):
	theta0error, theta1error = 0,0

	for mileage, price in zip(normalized_mileage, prices):
		estimate = theta0 + theta1 * mileage
		error = estimate - price

		theta0error += error
		theta1error += error * mileage
	
	tempTheta0 = learning_rate * theta0error / m
	tempTheta1 = learning_rate * theta1error / m

	theta0 -= tempTheta0
	theta1 -= tempTheta1

realTheta1 = theta1 / np.std(mileages)
realTheta0 = theta0 - realTheta1 * np.mean(mileages)

write_thetas(realTheta0, realTheta1)