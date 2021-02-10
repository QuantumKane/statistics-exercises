
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

# heads = 1, tails = 0

outcomes = [1, 0]
flips = np.random.choice(outcomes, size=(100_000, 8))
flips

three_heads = (flips.sum(axis=1) == 3)
three_heads.mean()

# Answer is 0.21772

# What is the probability of getting more than 3 heads?

outcomes = [1, 0]
flips = np.random.choice(outcomes, size=(100_000, 8))

more_than_three_heads = (flips.sum(axis=1) >= 3)
more_than_three_heads.mean()

# Answer is 0.85752

# 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# webdev = 1, ds = 0
outcomes = [1, 1, 1, 0]

alumni = np.random.choice(outcomes, size=(100_000, 2))
alumni
ds_billboards = alumni.sum(axis=1)
(ds_billboards == 0).mean()

# Answer is 0.06179

# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on Monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

n_poptarts = np.random.normal(loc = 3.0, scale = 1.5, size = (100_000, 5))
p_tarts = (n_poptarts.sum(axis = 1) < 17)
p_tarts.mean()
# Answer is 0.72257

# 5. Compare Heights: Men have an average height of 178 cm and standard deviation of 8cm. Women have a mean of 170, sd = 6cm. If a man and woman are chosen at random, P(woman taller than man)?

men_avg = 178
men_std = 8
wmn_avg = 170
wmn_std = 6

s_men = np.random.normal(men_avg, men_std, 100_000)
s_wmn = np.random.normal(wmn_avg, wmn_std, 100_000)

prob = (s_wmn > s_men).mean()
prob

# 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 

# no issues = 0, issues = 1
installs = np.random.choice([0, 1], size = (100_000, 50), p=[.996, .004])
good_install = installs.sum(axis = 1)
(good_install == 0).mean()
# Answer is 0.81928

# 100 students?

installs = np.random.choice([0, 1], size = (100_000, 100), p=[.996, .004])
good_install = installs.sum(axis = 1)
(good_install == 0).mean()
# Answer is 0.66796

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?

installs = np.random.choice([0, 1], size = (100_000, 150), p=[.996, .004])
good_install = installs.sum(axis = 1)
(good_install > 0).mean()
# Answer is 0.44968

# How likely is it that 450 students all download anaconda without an issue?

installs = np.random.choice([0, 1], size = (100_000, 450), p=[.996, .004])
good_install = installs.sum(axis = 1)
(good_install == 0).mean()
# Answer is 0.16503

# 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?

# ftruck = 0, no_ftruck = 1 
truck = np.random.choice([0, 1], size = (100_000, 3), p=[.7, .3])
food_truck = installs.sum(axis = 1)
(food_truck != 3).mean()
# Answer is 0.98086

# 8. If 23 people are in the same room, what are the odds that two of them share a birthday? 

outcomes = range(0, 365)
n_simulations = 100_000
n_trials = 23

classrooms = np.random.choice(outcomes, size = (n_simulations, n_trials))

same_day = [len(np.unique(classrooms[n])) for n in range(0, n_simulations-1) if len(np.unique(classrooms[n])) < 23]

same_bday = len(same_day) / n_simulations
same_bday
# Answer is 0.50642

# What if it's 20 people? 

outcomes = range(0, 365)
n_simulations = 100_000
n_trials = 20

classrooms = np.random.choice(outcomes, size = (n_simulations, n_trials))

same_day = [len(np.unique(classrooms[n])) for n in range(0, n_simulations-1) if len(np.unique(classrooms[n])) < 20]

same_bday = len(same_day) / n_simulations
same_bday
# Answer is 0.41037

# 40?

outcomes = range(0, 365)
n_simulations = 100_000
n_trials = 40

classrooms = np.random.choice(outcomes, size = (n_simulations, n_trials))

same_day = [len(np.unique(classrooms[n])) for n in range(0, n_simulations-1) if len(np.unique(classrooms[n])) < 40]

same_bday = len(same_day) / n_simulations
same_bday
# Answer is 0.89267