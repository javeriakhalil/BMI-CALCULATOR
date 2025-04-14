def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / height (m)^2
    """
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """
    Determine the BMI category based on WHO standards.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Example usage
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")