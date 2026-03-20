def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys

    print("Running main.py...")
    print("Sum:", add(10, 10))

    # Force flush so Jenkins shows output immediately
    sys.stdout.flush()
