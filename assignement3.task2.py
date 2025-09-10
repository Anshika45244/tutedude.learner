import math

def main():
    try:
        # Step 1: Get user input
        number = float(input("Enter a number: "))

        if number < 0:
            print("Error: Square root and logarithm are undefined for negative numbers.")
            return

        # Step 2: Perform calculations
        sqrt_result = math.sqrt(number)
        log_result = math.log(number)
        sine_result = math.sin(number)

        # Step 3: Display results
        print(f"\nResults for input: {number}")
        print(f"Square Root: {sqrt_result:.4f}")
        print(f"Natural Logarithm (base e): {log_result:.4f}")
        print(f"Sine (in radians): {sine_result:.4f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
