# Function to check if the input age is valid
def check_age(age):
    try:
        # Convert input to integer
        age = int(age)
        
        # Check if the age is positive
        if age <= 0:
            return "Error: Age must be a positive number."
        
        # Check if age is even or odd
        if age % 2 == 0:
            return f"The age {age} is valid and it is an even number."
        else:
            return f"The age {age} is valid and it is an odd number."
    
    except ValueError:
        return "Error: Please enter a valid integer for age."

# Get age input from the user
user_age = input("Enter your age: ")

# Call the function and print the result
result = check_age(user_age)
print(result)
