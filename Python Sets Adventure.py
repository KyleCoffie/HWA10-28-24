# 1. Python Sets Adventure
# Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
#1.
shared_routes = our_routes & competitor_routes
print(shared_routes)
#2.
our_unique_routes = our_routes - competitor_routes
print(our_unique_routes)

#3.
diff_routes = our_routes ^ competitor_routes
print(diff_routes)




