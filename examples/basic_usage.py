"""Basic usage example for SupraZone Framework."""

from suprazone import example


def main():
    """Demonstrate basic usage of the SupraZone Framework."""
    # Print a greeting
    print(example.hello())
    
    # Use the add function
    result = example.add(10, 20)
    print(f"10 + 20 = {result}")
    
    # Add with floats
    result = example.add(3.14, 2.86)
    print(f"3.14 + 2.86 = {result}")


if __name__ == "__main__":
    main()
