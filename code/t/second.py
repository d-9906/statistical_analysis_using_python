import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("Crime Head-wise Police Disposal of IPC Crime Cases (Crime Head-wise) during 2019.csv")
data=data[:-1] #removing the last total row for calculations

# Select columns
reported = data['Reported']
disposed = data['Disposed']

# 1. MEAN & MEDIAN
print("MEAN:")
print("Reported cases:", reported.mean())
print("Disposed cases:", disposed.mean())

print("\nMEDIAN:")
print("Reported cases:", reported.median())
print("Disposed cases:", disposed.median())

# 2. QUARTILES & PERCENTILES
print("\nQUARTILES (Reported cases):")
print("Q1:", reported.quantile(0.25))
print("Q2:", reported.quantile(0.50))
print("Q3:", reported.quantile(0.75))

print("\nPERCENTILES (Reported cases):")
print("25%:", reported.quantile(0.25))
print("50%:", reported.quantile(0.50))
print("75%:", reported.quantile(0.75))
print("90%:", reported.quantile(0.90))

# 3. STANDARD DEVIATION & VARIANCE
print("\nStandard Deviation:", reported.std())
print("Variance:", reported.var())

# 4. CORRELATION
print("\nCorrelation (Reported vs Disposed cases):")
print(reported.corr(disposed))

# 5. REGRESSION
print("\n REGRESSION")
x = reported
y = disposed
slope, intercept = np.polyfit(x, y, 1)
print("Slope:", slope)
print("Intercept:", intercept)
print("Regression equation: total disposed cases duting the year =",intercept ,"+", slope ,"total reported cases during the year")