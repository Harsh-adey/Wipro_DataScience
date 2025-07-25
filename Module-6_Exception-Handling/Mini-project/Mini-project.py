"""You had saved the items and their price details in a text file,
which you purchased yesterday from a nearby super market

You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after discount?

Help yourself by writing a python code to do this. Include necessary code
to handle the possible exceptions."""

try:
    name = input("Enter name: ")
    
    with open(name, 'r') as file:
        lines = file.readlines()

    total_items = 0
    free_items = 0
    total_amount = 0
    discount = 0

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 2:
            continue  # skip invalid lines

        item = " ".join(parts[:-1])
        price_str = parts[-1]

        total_items += 1

        try:
            if price_str.lower() == "free":
                free_items += 1
            else:
                price = float(price_str)

                if price < 0:
                    discount += abs(price)
                else:
                    total_amount += price

        except ValueError:
            print(f"Invalid price for item '{item}', skipping...")

    final_amount = total_amount - discount

    print("\n--- Purchase Summary ---")
    print("Total items purchased:", total_items)
    print("Free items:", free_items)
    print("Total amount before discount:", total_amount)
    print("Discount amount:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except Exception as e:
    print("An unexpected error occurred:", e)
