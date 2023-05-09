# SIR model for epidemic prediction
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math
import statistics

# SIR model parameters
N = 1000  # population size
beta = 0.3  # infection rate
gamma = 0.1  # recovery rate
I0 = 1  # initial number of infected individuals
R0 = 0  # initial number of recovered individuals
S0 = N - I0 - R0  # initial number of susceptible individuals

# Simulation parameters
num_days = 100  # number of days to simulate
num_trials = 1000  # number of simulation trials

# SIR model simulation function
def sir_simulate(N, beta, gamma, I0, R0, S0, num_days):
    S = np.zeros(num_days+1)
    I = np.zeros(num_days+1)
    R = np.zeros(num_days+1)

    S[0] = S0
    I[0] = I0
    R[0] = R0

    for t in range(num_days):
        # Compute the number of new infections and recoveries
        new_infections = np.random.binomial(S[t], beta * I[t] / N)
        new_recoveries = np.random.binomial(I[t], gamma)

        # Update the number of susceptible, infected, and recovered individuals
        S[t+1] = S[t] - new_infections
        I[t+1] = I[t] + new_infections - new_recoveries
        R[t+1] = R[t] + new_recoveries

    return S, I, R

# Run multiple trials of the simulation and plot the results
S_mean = np.zeros(num_days+1)
I_mean = np.zeros(num_days+1)
R_mean = np.zeros(num_days+1)

for i in range(num_trials):
    S, I, R = sir_simulate(N, beta, gamma, I0, R0, S0, num_days)
    S_mean += S
    I_mean += I
    R_mean += R

S_mean /= num_trials
I_mean /= num_trials
R_mean /= num_trials

plt.plot(S_mean, label='Susceptible')
plt.plot(I_mean, label='Infected')
plt.plot(R_mean, label='Recovered')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Number of Individuals')
plt.title('SIR Model Simulation')
plt.show()