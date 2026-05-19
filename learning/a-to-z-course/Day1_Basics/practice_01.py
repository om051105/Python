"""
DAY 1: PRACTICAL PYTHON CHALLENGES
Topic: Variables, Input/Output, and Type Casting

INSTRUCTIONS:
1. Read the Challenge.
2. Code your solution under the 'YOUR CODE HERE' section.
3. Run this file using `python practice_01.py` to test (if applicable).
"""

# ==============================================================================
# CHALLENGE 1: The Personal Greeting (Basics)
# Task: Ask the user for their Name and their Favorite Color. 
#       Then print a message like "Hello [Name], your favorite color [Color] is cool!"
# Logic: Use input() and print() with f-strings or commas.
# ==============================================================================

# YOUR CODE HERE (CHALLENGE 1)
name = input("Enter your name: ")
color = input("Enter your favorite color: ")
print(f"Hello {name}, your favorite color {color} is cool!")


# ==============================================================================
# CHALLENGE 2: The Age Calculator (Type Casting)
# Task: Ask the user for their Birth Year. 
#       Calculate their current age (assume current year is 2026).
#       Print: "You are [Age] years old."
#
# LOGIC STEPS:
# 1. birth_year = input("What year were you born? ")
# 2. current_year = 2026
# 3. age = current_year - int(birth_year) 
# 4. print(f"You are {age} years old.")
# ==============================================================================

# YOUR CODE HERE (CHALLENGE 2)
birth_year = input("What year were you born? ")
current_year = 2026
age = current_year - int(birth_year)
print(f"You are {age} years old.")



# ==============================================================================
# CHALLENGE 3: Swap the Juice (Logic/Variables) - INTERVIEW STYLE
# Task: You have two variables: `glass_a` contains "Apple Juice" and `glass_b` 
#       contains "Orange Juice". 
#       Swap their contents so `glass_a` has Orange and `glass_b` has Apple.
# Restriction: Do NOT just re-assign them directly (e.g., glass_a = "Orange").
# Hint: Think about how you would swap two liquids in real life. You need a third glass!
# ============= CHALLENGE 3 CODE BELOW ==========================================

glass_a = "Apple Juice"
glass_b = "Orange Juice"

# YOUR CODE HERE (CHALLENGE 3)


# DO NOT TOUCH THIS PART - FOR VERIFICATION
print(f"Glass A: {glass_a}")
print(f"Glass B: {glass_b}")
glass_a = "Apple Juice"
glass_b = "Orange Juice"

# THE SWAP LOGIC:
temp = glass_a      # Step 1: Save Apple in temp
glass_a = glass_b   # Step 2: Move Orange to A
glass_b = temp      # Step 3: Move Apple (from temp) to B