import random

def generate_random_numbers(count=10, start=1, end=100):
    """Generate a list of random numbers."""
    return [random.randint(start, end) for _ in range(count)]

def save_to_file(numbers, filename="random_numbers.txt"):
    """Save the generated numbers to a file."""
    try:
        with open(filename, "w") as file:
            for num in numbers:
                file.write(f"{num}\n")
        print(f"Numbers saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    numbers = generate_random_numbers()
    print("Generated Numbers:", numbers)
    save_to_file(numbers)

if __name__ == "__main__":
    main()
