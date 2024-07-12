import sys

def fibonacci(n):
    if n <= 0:
        return "please enter a positive integer greater than 0."
    sequence = [0, 1]
    sequence.extend(sequence[-1] + sequence[-2] for _ in range(2, n))
    return sequence[:n]

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        print(fibonacci(n))
    except (IndexError, ValueError):
        print("Usage: python script.py <number_of_terms>")

