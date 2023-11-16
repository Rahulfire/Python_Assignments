def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and int(age) >= 18:  # Compare after converting to int
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age is not None:  # Check for None explicitly
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()

