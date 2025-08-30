from calculator import Calculator


def main():
    calc = Calculator()

    while True:
        print("\nCalculator Menu:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = calc.add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"\nResult: {num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = calc.divide(num1, num2)
                    print(f"\nResult: {num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
            else:
                print("\nInvalid choice! Please select 1-5.")

        except ValueError:
            print("\nError: Please enter valid numbers!")


if __name__ == "__main__":
    main()