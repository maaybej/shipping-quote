# Welcome message that introduces the user to the program
print("Welcome to Package Express. Please follow the instructions below.")

# Prompt the user to enter the weight of the package
weight = float(input("Please enter the package weight: "))

# Check if the weight exceeds the limit of 50
if weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
else:
    # If the weight is within the limit, prompt for the package dimensions
    width = float(input("Please enter the package width: "))
    height = float(input("Please enter the package height: "))
    length = float(input("Please enter the package length: "))

    # Check if the total dimensions (width + height + length) exceed 50
    if width + height + length > 50:
        print("Package too big to be shipped via Package Express.")
    else:
        # Calculate the shipping quote based on the dimensions and weight
        volume = width * height * length  # Multiply width, height, and length to get the volume
        quote = (volume * weight) / 100  # Multiply the volume by weight and divide by 100

        # Display the shipping quote
        print(f"Your estimated total for shipping this package is: ${quote:.2f}")
        print("Thank you!")
