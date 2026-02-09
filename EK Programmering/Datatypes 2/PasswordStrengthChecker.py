#Make a program that:

#1. Calculates the total password strength score.

#2. Print the total score

#3. Then, use the modulus operator (%) to check if the score is divisible by 10 (hint: if score % 10 equals 0, it's divisible by 10).

#4. Print the result of the modulus operation.

# Points per character type
lowercase_letters = 5
uppercase_letters = 8
numbers = 10
special_characters = 15
points_per_length = 3

# Password composition
num_lowercase = 3
num_uppercase = 2
num_numbers = 4
num_special = 2

# 1. Calculate total strength score
strength_score = (
    num_lowercase * lowercase_letters +
    num_uppercase * uppercase_letters +
    num_numbers * numbers +
    num_special * special_characters
)

# Add length points
password_length = (
    num_lowercase +
    num_uppercase +
    num_numbers +
    num_special
)
strength_score += password_length * points_per_length

# 2. Print total score
print("Total password strength score:", strength_score)

# 3. Modulus check
modulus_result = strength_score % 10

# 4. Print modulus result
print("Score % 10 =", modulus_result)