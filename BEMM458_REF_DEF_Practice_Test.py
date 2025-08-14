
#######################################################################################################################################################
# 
# Name: Shraddha Abhay Thakre
# SID: 740100657
# Exam Date: 14-08-2025
# Module: BEMM458J - Test 2 Programming for business Analytics 
# Github link for this assignment:  https://classroom.github.com/a/Q77v9B5

#
########################################################################################################################################################
# Instruction 1. Carefully read each question before attempting the solution. Complete all tasks in the script provided.

# Instruction 2. Only ethical and minimal use of AI tools is allowed. This includes help in syntax, documentation look-up, or debugging only.
#                You must not use AI to generate the core logic or full solutions.
#                Clearly indicate where and how AI support was used.

# Instruction 3. Paste the output of each code section directly beneath it as a comment (e.g., # OUTPUT: (34, 90))

# Instruction 4. Add sufficient code comments to demonstrate your understanding of each solution.

# Instruction 5. Save your file, commit it to GitHub, and upload to ELE. GitHub commit must be done before the end of the exam session.

########################################################################################################################################################
# Question 1 - List Comprehension and String Manipulation
# You are analysing customer reviews collected from a post-service survey.
# Your SID will determine the two allocated keywords from the dictionary below. Use the **second** and **second-to-last** digits of your SID.
# For each selected keyword, identify all positions (start and end) where the word occurs in the customer_review string.
# Store each occurrence as a tuple in a list called `location_list`.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

# Dictionary of keywords
feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# Write your code here to populate location_list
location_list = []

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# SID: 740100657
# Second digit: 4 → "tutorials"
# Second-to-last digit: 5 → "responsive"
kw1 = feedback_keywords[4]
kw2 = feedback_keywords[5]

location_list = []
for kw in [kw1, kw2]:
    start = 0
    while True:
        idx = customer_review.lower().find(kw.lower(), start)
        if idx == -1:
            break
        location_list.append((idx, idx + len(kw)))
        start = idx + 1

print("Q1 location_list:", location_list)


########################################################################################################################################################
# Question 2 - Metrics Function for Business Intelligence
# You work in a startup focused on digital health. Your manager wants reusable functions to calculate key performance metrics:
# Gross Profit Margin, Churn Rate, Customer Lifetime Value (CLV), and Cost Per Acquisition (CPA).
# Use the **first** and **last** digits of your student ID as sample numerical values to test your function outputs.

# Insert first digit of SID here: 7
# Insert last digit of SID here: 7

# Write a function for Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100

# Write a function for Churn Rate (%) = (Customers Lost / Customers at Start) * 100

# Write a function for Customer Lifetime Value = Average Purchase Value × Purchase Frequency × Customer Lifespan

# Write a function for CPA = Marketing Cost / Number of Acquisitions

# Test your functions here

# First digit: 7, Last digit: 7

def gross_profit_margin(revenue, cogs):
    return (revenue - cogs) / revenue * 100

def churn_rate(customers_lost, customers_start):
    return (customers_lost / customers_start) * 100

def customer_lifetime_value(avg_purchase_value, purchase_frequency, customer_lifespan):
    return avg_purchase_value * purchase_frequency * customer_lifespan

def cost_per_acquisition(marketing_cost, acquisitions):
    return marketing_cost / acquisitions

# Test functions with SID-based numbers
print("Q2 Gross Profit Margin:", gross_profit_margin(77, 7))
print("Q2 Churn Rate:", churn_rate(7, 77))
print("Q2 CLV:", customer_lifetime_value(7, 7, 7))
print("Q2 CPA:", cost_per_acquisition(77, 7))



########################################################################################################################################################
# Question 3 - Linear Regression for Pricing Strategy
# A bakery is studying how price affects cupcake demand. Below is a table of past pricing decisions and customer responses.
# Using linear regression:
# 1. Estimate the best price that maximises demand.
# 2. Predict demand if the bakery sets price at £25.

"""
Price (£)    Demand (Units)
---------------------------
8            200
10           180
12           160
14           140
16           125
18           110
20           90
22           75
24           65
26           50
"""

# Write your linear regression solution here 

import numpy as np
from sklearn.linear_model import LinearRegression

prices = np.array([8, 10, 12, 14, 16, 18, 20, 22, 24, 26]).reshape(-1, 1)
demand = np.array([200, 180, 160, 140, 125, 110, 90, 75, 65, 50])

model = LinearRegression()
model.fit(prices, demand)

# 1. Best price that maximises demand = lowest price (linear decrease)
best_price = prices[np.argmax(demand)][0]

# 2. Predict demand at £25
pred_25 = model.predict(np.array([[25]]))[0]

print("Q3 Best Price:", best_price)
print("Q3 Predicted Demand at £25:", pred_25)



########################################################################################################################################################
# Question 4 - Debugging and Chart Creation
# The following code is intended to generate 100 random integers between 1 and your SID, and plot them as a scatter plot.
# However, the code contains bugs and lacks contextual annotations. Correct the code and add appropriate comments and output.

import random
import matplotlib.pyplot as plt

# Accept student ID as input
sid_input = input("Enter your SID: 740100657 ")
sid_value = int(sid_input)

# Generate 100 random values
random_values = [random.randint(1, sid_value) for _ in range(100)]

# Plotting as scatter plot
plt.figure(figsize=(10,5))
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values')
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

#code:
import random
import matplotlib.pyplot as plt

# Use given SID directly (no need for input in this solution)
sid_value = 740100657

# Generate 100 random integers between 1 and SID
random_values = [random.randint(1, sid_value) for _ in range(100)]

# Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values')
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

########################################################################################################################################################
