import time

output_file = open("new.py", "a")

try:
    num1 = int(input("Enter Dividend: "))
    num2 = int(input("Enter Divisor: "))

    result = num1 / num2
    print("Divided value is", result)

    execution_time = time.ctime()
    print(execution_time)
    output_file.write(f"Dividend: {num1}\n")
    output_file.write(f"Divisor: {num2}\n")
    output_file.write(f"Result: {result}\n")
    output_file.write(f"Execution Time: {execution_time}\n")

except Exception as e:
    print("Rectify the error:", e)
    output_file.write(f"Error: {e}\n")

else:
    print("No error occurred")
    output_file.write("No error occurred\n")

finally:
    print("Code is executed successfully")
    output_file.write("Code is executed successfully\n")
    output_file.write("\n")

output_file.close()