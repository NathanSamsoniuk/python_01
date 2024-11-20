# Constant for the base bonus value
BONUS_CONSTANT = 1000

def get_positive_float(prompt: str) -> float:
    """
    Prompt the user for a positive float value. Repeats until a valid input is provided.
    
    Args:
        prompt (str): The input prompt for the user.
        
    Returns:
        float: A positive floating-point number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("The value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_bonus(salary: float, bonus_percentage: float) -> float:
    """
    Calculate the total bonus based on salary and bonus percentage.
    
    Args:
        salary (float): The user's salary.
        bonus_percentage (float): The bonus percentage as a decimal.
        
    Returns:
        float: The total bonus value.
    """
    return BONUS_CONSTANT + salary * bonus_percentage

def print_welcome_message():
    """
    Print a welcome message to the user.
    """
    print("============================================")
    print("       Welcome to the 2024 Bonus Calculator")
    print("============================================\n")

def main():
    """
    Main function to run the bonus calculator program.
    """
    print_welcome_message()

    # Step 1: Gather user inputs
    user_name = input("Please enter your name: ").strip()
    user_salary = get_positive_float("Please enter your salary: ")
    user_bonus_percentage = get_positive_float(
        "Please enter your bonus percentage (e.g., 10 for 10%): "
    ) / 100

    # Step 2: Calculate the bonus
    total_bonus = calculate_bonus(user_salary, user_bonus_percentage)

    # Step 3: Display the result
    print(f"\nHello, {user_name}! Based on your salary and bonus percentage, "
          f"your total bonus amount is ${total_bonus:.2f}.\n")
    print("Thank you for using the Bonus Calculator!")

if __name__ == "__main__":
    main()

