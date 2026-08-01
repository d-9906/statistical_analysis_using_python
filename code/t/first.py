import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
data = pd.read_csv("City, Age Group and Gender-wise Persons Arrested under IPC Crimes in Metropolitan Cities during 2019.csv")
data=data[:-1]  #removing the last total row for calculations

#columns 
total = 'Total  - Arrested'
male = 'Total   - Male'
female = 'Total   - Female'

# 1. MEAN, MEDIAN 

print("Mean of total persons arrested:", data[total].mean())
print("Median of total persons arrested:", data[total].median())

# 2. QUARTILES,PERCENTILES 

print("\nQUARTILES of total persons arrested:-")
print("1st quartile:",data[total].quantile(0.25))
print("2nd quartile:",data[total].quantile(0.5))
print("3rd quartile:",data[total].quantile(0.75))
print("\nPERCENTILES of total persons arrested:-")
print("25th Percentile:", data[total].quantile(0.25))
print("50th Percentile:", data[total].quantile(0.50))
print("75th Percentile:", data[total].quantile(0.75))
print("90th Percentile:", data[total].quantile(0.90))

# 3. STANDARD DEVIATION & VARIANCE 

print("\nStandard Deviation of total persons arrested:", data[total].std())
print("Variance of total persons arrested:", data[total].var())

# 4. CORRELATION 

print("\nCorrelation between male and female arrests:")
print(data['Total   - Male'].corr(data['Total   - Female']))

# 5. REGRESSION 

print("\nREGRESSION (female vs male)")
x = data[male]
y = data[female]
slope, intercept = np.polyfit(x, y, 1)
print("Slope:", slope)
print("Intercept:", intercept)
print("Regression equation: Female arrests=",intercept ,"+", slope ,"Male arrests")

# 6. T-Test (two sample test)

#Null Hypothesis: There is no significant difference between the average number of male and female arrests.
#Alternative Hypothesis: there is a significant difference between the average number of male and female arrests.

t_stat, p_value = stats.ttest_ind(data[male], data[female])

print("\nT-TEST:-")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Result: Since P-value is LESS than 0.05, the difference is statistically significant.")
else:
    print("Result: Since P-value is GREATER than 0.05, the difference is not significant.")