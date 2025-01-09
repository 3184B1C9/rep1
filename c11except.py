class AgeRestrictionError(Exception):

    def __init__(self, message="Age must be 18 or older"):
        super().__init__(message)

def validate_age(age):
    if age < 18:
        raise AgeRestrictionError(f"Invalid age: {age}. You must be at least 18.")
    else:
        print(f"Age {age} is valid. Access granted.")


try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)

except AgeRestrictionError as e:
    print(f"Error: {e}")
    
except ValueError:
    print("Error: Please enter a valid integer for age.")
