import math
import csv
import random

def generate_values(line_type, num_points=10, **kwargs):
    """Generate values based on the selected line type and parameters."""
    x_values = list(range(num_points))  # The range of x values
    
    if line_type == "linear":
        slope = kwargs.get('slope', 1)
        intercept = kwargs.get('intercept', 0)
        return {x: slope * x + intercept for x in x_values}
    
    elif line_type == "exponential":
        base = kwargs.get('base', 2)
        return {x: base**x for x in x_values}
    
    elif line_type == "sine":
        amplitude = kwargs.get('amplitude', 1)
        frequency = kwargs.get('frequency', 1)
        return {x: amplitude * math.sin(frequency * x) for x in x_values}
    
    elif line_type == "quadratic":
        a = kwargs.get('a', 1)
        b = kwargs.get('b', 0)
        c = kwargs.get('c', 0)
        return {x: a * x**2 + b * x + c for x in x_values}
    
    else:
        raise ValueError("Invalid line type selected.")

def randomize_values(data, lower_range, upper_range):
    """Randomize the generated values within a specified range."""
    randomized_data = {}
    for key, values in data.items():
        randomized_data[key] = {x: v + random.uniform(lower_range, upper_range) for x, v in values.items()}
    return randomized_data

def save_to_csv(data, filename):
    """Save the generated dictionary to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row with attribute names
        header = ['X'] + list(data.keys())
        writer.writerow(header)
        
        # Find the number of data points (assuming all attributes have the same number of points)
        num_points = len(next(iter(data.values())))  # Get the length of the first attribute's values
        
        # Write the rows with the generated values
        for i in range(num_points):
            row = [i]  # Start with the X value
            for key in data:
                row.append(data[key][i])
            writer.writerow(row)

def main():
    # Ask for the number of attributes
    num_attributes = int(input("How many attributes do you want? "))
    
    # Initialize the result dictionary
    result = {}
    
    # Collect attribute names and their line types
    for i in range(num_attributes):
        attr = input(f"Enter name for attribute {i + 1}: ")
        
        # Ask for the line type for this attribute
        print("What type of line do you want for this attribute? Options: linear, exponential, sine, quadratic")
        line_type = input("Enter your choice: ").strip().lower()
        
        # Validate the line type
        while line_type not in {"linear", "exponential", "sine", "quadratic"}:
            print("Invalid line type. Please choose one of the options: linear, exponential, sine, quadratic")
            line_type = input("Enter your choice: ").strip().lower()
        
        # Ask for the number of values to generate for this attribute
        num_values = int(input(f"How many values do you want for attribute '{attr}'? "))
        
        # Get parameters specific to the line type
        params = {}
        if line_type == "linear":
            params['slope'] = float(input("Enter the slope (default 1): ") or 1)
            params['intercept'] = float(input("Enter the intercept (default 0): ") or 0)
        elif line_type == "exponential":
            params['base'] = float(input("Enter the base (default 2): ") or 2)
        elif line_type == "sine":
            params['amplitude'] = float(input("Enter the amplitude (default 1): ") or 1)
            params['frequency'] = float(input("Enter the frequency (default 1): ") or 1)
        elif line_type == "quadratic":
            params['a'] = float(input("Enter coefficient a (default 1): ") or 1)
            params['b'] = float(input("Enter coefficient b (default 0): ") or 0)
            params['c'] = float(input("Enter coefficient c (default 0): ") or 0)
        
        # Generate values for this attribute and store in the dictionary
        result[attr] = generate_values(line_type, num_points=num_values, **params)
    
    # Print the generated dictionary
    print("\nGenerated dictionary:")
    for key, values in result.items():
        print(f"{key}: {values}")
    
    # Ask if the user wants to randomize the values
    randomize_choice = input("\nDo you want to randomize the values? (y/n): ").strip().lower()
    if randomize_choice == 'y':
        lower_range = float(input("Enter the lower bound for randomization: "))
        upper_range = float(input("Enter the upper bound for randomization: "))
        result = randomize_values(result, lower_range, upper_range)
        print("\nRandomized dictionary:")
        for key, values in result.items():
            print(f"{key}: {values}")
    
    # Ask if the user wants to save to a CSV file
    save_choice = input("\nDo you want to save the results to a CSV file? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter the filename (e.g., 'data.csv'): ").strip()
        save_to_csv(result, filename)
        print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()
