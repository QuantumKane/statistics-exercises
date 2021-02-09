
import pandas as pd
import numpy as np
from pydataset import data
from math import sqrt

# 1. How likely is it that you roll doubles when rolling two dice?

first_die = np.random.choice([1, 2, 3, 4, 5, 6], size=100_000)
second_die = np.random.choice([1, 2, 3, 4, 5, 6], size=100_000)
first_die, second_die

doubles = (first_die == second_die)
doubles.mean()

# Answer is 0.16736

# 2 If you flip 8 coins, what is the probability of getting exactly 3 heads? 

outcomes = [1, 0]
flips = np.random.choice(outcomes, size=(100_000, 8))
flips

three_heads = (flips.sum(axis=1) == 3)
three_heads.mean()

# Answer is 0.21772

# What is the probability of getting more than 3 heads?

outcomes = [1, 0]
flips = np.random.choice(outcomes, size=(100_000, 8))

more_than_three_heads = (flips.sum(axis=1) > 3)
more_than_three_heads.mean()

# Answer is 0.63597

# 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# wedev = 1, ds = 0
outcomes = [1, 1, 1, 0]

alumni = np.random.choice(outcomes, size=(100_000, 2))
alumni
ds_billboards = alumni.sum(axis=1)
(ds_billboards == 0).mean()

# Answer is 0.06179

# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on Monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

np.random.normal(loc = 3.0, scale = 1.5, size = 5)

# 5. Compare Heights: Men have an average height of 178 cm and standard deviation of 8cm. Women have a mean of 170, sd = 6cm. If a man and woman are chosen at random, P(woman taller than man)?




# 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?

What is the probability that we observe an installation issue within the first 150 students that download anaconda?

How likely is it that 450 students all download anaconda without an issue?


# 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?



# 8. If 23 people are in the same room, what are the odds that two of them share a birthday? 



# What if it's 20 people? 



# 40?