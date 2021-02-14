
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from env import host, user, password

# 1 A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. What is the probability that no cars drive up in the noon hour?

λ = 2
stats.poisson(λ).pmf(0)
# Answer is 0.1353352832366127

# What is the probability that 3 or more cars come through the drive through?

λ = 2
stats.poisson(λ).sf(2)
# Answer is 0.32332358381693654

# How likely is it that the drive through gets at least 1 car?

λ = 2
1 - stats.poisson(λ).pmf(0)
# Answer is 0.8646647167633873

# simulation
λ = 2

x = np.arange(0,10)
y = stats.poisson(λ).pmf(x)

plt.bar(x,y, width = 0.9)
plt.xlabel('Number of Cars')
plt.ylabel('probability P(X)')
plt.xticks(np.arange(0,10,1))
plt.title('Poisson distrbution with $\lambda$ = 2', fontsize = 14);


# 2 Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following: What grade point average is required to be in the top 5% of the graduating class?

mean = 3
sd = .3

grades = stats.norm(mean, sd)
grades.isf(0.05)


# What GPA constitutes the bottom 15% of the class?

grades = stats.norm(mean, sd)
grades.ppf(0.15)

# simulation
np.quantile(np.random.normal(3, 0.3, 10_000), 0.15)

# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

stats.norm(3, .3).ppf([.2,.3])

# simulation
np.quantile(np.random.normal(3, 0.3, 10_000), [0.2, 0.3])

# If I have a GPA of 3.5, what percentile am I in?

stats.norm(3, .3).cdf(3.5)

# simulation
(np.random.normal(3, 0.3, 10_000) < 3.5).mean()

# 3 A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. How likely is it that this many people or more click through?

n_trials = 4326
prob = 0.02

stats.binom(n_trials, prob).sf(96)

# simulation
clicks = np.random.choice([0,1], (100_000, 4326), p = [0.98, 0.02])

# 4 You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question. What is the probability that at least one of your first 60 answers is correct?

n_trials = 60
prob = .01

stats.binom(n_trials, prob).sf(0)

# simulation
answers = np.random.choice([0,1], (10_000, 60), p = [0.99, 0.01])

# 5 Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned up each day? 

n_trials = 59
prob = .03

stats.binom(n_trials, prob).sf(0) 

# How likely is it that it goes two days without getting cleaned up? 

stats.binom(n_trials * 2, prob).pmf(0)

# All week?

stats.binom(n_trials * 5, prob).pmf(0)


# simulation
x = np.arange(0,9)
y = stats.binom(n, p).pmf(x)
plt.bar(x,y, width = 0.9)
plt.xlabel('Number of times area is cleaned per day')


# 6 You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

mean = 30
sd = 6

stats.norm(mean, sd).cdf(35)


# simulation
(np.random.normal(30, 6, 100_000) < 35).mean()


# 7 Connect to the employees database and find the average salary of current employees, along with the standard deviation. For the following questions, calculate the answer based on modeling the employees salaries with a normal distribution defined by the calculated mean and standard deviation then compare this answer to the actual values present in the salaries dataset.
# What percent of employees earn less than 60,000?

mean_df = df.salary.mean()
sd_df = df.salary.std()

mean_df, sd_df
stats.norm(mean_df, sd_df).cdf(60000)

# What percent of employees earn more than 95,000

stats.norm(mean_df, sd_df).sf(95000)

# What percent of employees earn between 65,000 and 80,000?

stats.norm(mean_df, sd_df).sf(65000) - stats.norm(mean_df, sd_df).sf(80000)

# What do the top 5% of employees make?

stats.norm(mean_df, sd_df).isf(0.05)