def calculator():
    user_input = input("Enter command: ").strip().split()

    if len(user_input) != 3:
        print("❌ Invalid input. Use format: <operation> <num1> <num2>")
        return

    command, num1, num2 = user_input
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    if command == "add":
        result = num1 + num2
    elif command == "sub":
        result = num1 - num2
    elif command == "mul":
        result = num1 * num2
    elif command == "div":
        if num2 == 0:
            print("❌ Division by zero not allowed.")
            return
        result = num1 / num2
    else:
        print(f"❌ Unknown command: {command}")
        return

    print(f"✅ Result: {result}")


calculator()
