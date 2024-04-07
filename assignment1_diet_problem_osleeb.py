#!/usr/bin/env python
# coding: utf-8

# In[21]:


from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize


# In[22]:


### Initial Linear Programming Model for the Diet Problem 

# declare your variables
protein_shake = LpVariable("x1", 0, None) 
salad_chicken = LpVariable("x2", 0, None) 
chick_broc_rice = LpVariable("x3", 0, None) 
mac_n_cheese = LpVariable("x4", 0, None) # 
gnocchi_sausage = LpVariable("x5", 0, None) 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += (90*protein_shake) + (1118*salad_chicken) + (450.6*chick_broc_rice) + (636*mac_n_cheese) + (1536*gnocchi_sausage) <= (5000*7)
prob += (195*protein_shake) + (598*salad_chicken) + (528*chick_broc_rice) + (319*mac_n_cheese) + (371*gnocchi_sausage)  >= (2000*7)
prob += (34*protein_shake) + (69.92*salad_chicken) + (63.87*chick_broc_rice) + (17.57*mac_n_cheese) + (21.3*gnocchi_sausage) >= (50*7)
prob += (25*protein_shake) + (1.1*salad_chicken) + (2*mac_n_cheese) >= (20*7)                           
prob += (567*protein_shake) + (147.9*salad_chicken) + (74*chick_broc_rice) + (228*mac_n_cheese) + (378.192*gnocchi_sausage) >= (1300*7)
prob += (0.38*protein_shake) + (3.54*salad_chicken) + (3.39*chick_broc_rice) + (3.69*mac_n_cheese) + (8.29*gnocchi_sausage) >= (18*7)
prob += (170*protein_shake) + (1697*salad_chicken) + (1164.7*chick_broc_rice) + (630*mac_n_cheese) + (1788.8*gnocchi_sausage) >= (4700*7)
#prob += protein_shake >= 1
#prob += salad_chicken >= 1
#prob += chick_broc_rice >= 1
#prob += mac_n_cheese >= 1
#prob += gnocchi_sausage >= 1


# defines the objective function to maximize
prob += 1.85*protein_shake + 4.32*salad_chicken + 1.75*chick_broc_rice + 1.51*mac_n_cheese + 5.59*gnocchi_sausage

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Number of Servings per Meal")
print('Protein Shake:', value(protein_shake))
print('Salad with Chicken:', value(salad_chicken))
print('Mac n Cheese:', value(mac_n_cheese))
print('Chicken, Broccoli, Rice:', value(chick_broc_rice))
print('Gnocchi Chicken Sausage:', value(gnocchi_sausage))


# In[23]:


### Total Weekly Cost
weekly_cost = 1.85*value(protein_shake) + 4.32*value(salad_chicken) + 1.75*value(chick_broc_rice) + 1.51*value(mac_n_cheese) + 5.59*value(gnocchi_sausage)
weekly_cost


# In[24]:


### Diet Problem with one serving minimum for each meal

# declare your variables
protein_shake = LpVariable("x1", 0, None) 
salad_chicken = LpVariable("x2", 0, None) 
chick_broc_rice = LpVariable("x3", 0, None) 
mac_n_cheese = LpVariable("x4", 0, None) # 
gnocchi_sausage = LpVariable("x5", 0, None) 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += (90*protein_shake) + (1118*salad_chicken) + (450.6*chick_broc_rice) + (636*mac_n_cheese) + (1536*gnocchi_sausage) <= (5000*7)
prob += (195*protein_shake) + (598*salad_chicken) + (528*chick_broc_rice) + (319*mac_n_cheese) + (371*gnocchi_sausage)  >= (2000*7)
prob += (34*protein_shake) + (69.92*salad_chicken) + (63.87*chick_broc_rice) + (17.57*mac_n_cheese) + (21.3*gnocchi_sausage) >= (50*7)
prob += (25*protein_shake) + (1.1*salad_chicken) + (2*mac_n_cheese) >= (20*7)                           
prob += (567*protein_shake) + (147.9*salad_chicken) + (74*chick_broc_rice) + (228*mac_n_cheese) + (378.192*gnocchi_sausage) >= (1300*7)
prob += (0.38*protein_shake) + (3.54*salad_chicken) + (3.39*chick_broc_rice) + (3.69*mac_n_cheese) + (8.29*gnocchi_sausage) >= (18*7)
prob += (170*protein_shake) + (1697*salad_chicken) + (1164.7*chick_broc_rice) + (630*mac_n_cheese) + (1788.8*gnocchi_sausage) >= (4700*7)
prob += protein_shake >= 1
prob += salad_chicken >= 1
prob += chick_broc_rice >= 1
prob += mac_n_cheese >= 1
prob += gnocchi_sausage >= 1


# defines the objective function to maximize
prob += 1.85*protein_shake + 4.32*salad_chicken + 1.75*chick_broc_rice + 1.51*mac_n_cheese + 5.59*gnocchi_sausage

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Number of Servings per Meal")
print('Protein Shake:', value(protein_shake))
print('Salad with Chicken:', value(salad_chicken))
print('Mac n Cheese:', value(mac_n_cheese))
print('Chicken, Broccoli, Rice:', value(chick_broc_rice))
print('Gnocchi Chicken Sausage:', value(gnocchi_sausage))


# In[25]:


weekly_cost = 1.85*value(protein_shake) + 4.32*value(salad_chicken) + 1.75*value(chick_broc_rice) + 1.51*value(mac_n_cheese) + 5.59*value(gnocchi_sausage)
weekly_cost


# In[26]:


### ChatGPT Code Output

from pulp import *

# Create a LP minimization problem
prob = LpProblem("Weekly Diet Problem", LpMinimize)

# Decision variables
x1 = LpVariable("Protein Shake", lowBound=0, cat='Continuous')
x2 = LpVariable("Salad with Chicken", lowBound=0, cat='Continuous')
x3 = LpVariable("Mac n Cheese with Broccoli", lowBound=0, cat='Continuous')
x4 = LpVariable("Chicken, Broccoli, and Rice", lowBound=0, cat='Continuous')
x5 = LpVariable("Cauliflower Gnocchi with Chicken Sausage", lowBound=0, cat='Continuous')

# Objective function
prob += 7 * (1.85 * x1 + 4.32 * x2 + 1.51 * x3 + 1.75 * x4 + 5.59 * x5), "Total Cost"  # Adjusted for a week

# Constraints
prob += 7 * (90 * x1 + 1118 * x2 + 450.6 * x4 + 636 * x3 + 1536 * x5) <= 5000 * 7, "Sodium"  # Adjusted for a week
prob += 7 * (195 * x1 + 598 * x2 + 528 * x4 + 319 * x3 + 371 * x5) >= 2000 * 7, "Energy"  # Adjusted for a week
prob += 7 * (34 * x1 + 69.92 * x2 + 63.87 * x4 + 17.57 * x3 + 21.3 * x5) >= 50 * 7, "Protein"  # Adjusted for a week
prob += 7 * (25 * x1 + 1.1 * x2 + 2 * x3) >= 20 * 7, "Vitamin D"  # Adjusted for a week
prob += 7 * (567 * x1 + 147.9 * x2 + 74 * x4 + 228 * x3 + 378.192 * x5) >= 1300 * 7, "Calcium"  # Adjusted for a week
prob += 7 * (0.38 * x1 + 3.54 * x2 + 3.69 * x3 + 3.39 * x4 + 8.29 * x5) >= 18 * 7, "Iron"  # Adjusted for a week
prob += 7 * (170 * x1 + 1697 * x2 + 1164.7 * x4 + 630 * x3 + 1788.8 * x5) >= 4700 * 7, "Potassium"  # Adjusted for a week

# Solve the problem
prob.solve()

# Print the results
print("Status:", LpStatus[prob.status])
print("Total Cost = $", value(prob.objective))
print("Optimal Servings:")
for v in prob.variables():
    print(v.name, "=", v.varValue)


# In[ ]:




