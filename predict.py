#!/usr/bin/env python3

import csv
import sys

def getTheta() -> tuple[float, float]:
	theta0, theta1 = 0, 0
	try:
		with open("thetas.csv", mode='r', encoding='utf-8') as f:
			print("attempting to read from thetas.csv")
			reader = csv.reader(f)
			row = next(reader)
			return float(row[0]), float(row[1])
	except:
		pass
	return theta0, theta1

while (True):
	mileage = input("Enter Mileage: ")
	try:
		value = float(mileage);
		if value < 0:
			raise ValueError
		break;
	except ValueError:
		print("Input a valid positive float.")

theta0, theta1 = getTheta();
estimation = theta0 + (theta1 * float(mileage))
print(f"Estimated Price of car given mileage is {estimation:.2f}")
