calc_data = {}

# open calc.txt file
with open('calc.txt', 'r') as calc_file:
    # read contents of file
    calc_contents = calc_file.read()

# execute calculations from file using exec() function
exec(calc_contents, calc_data)

def calculate_1RM(weight, reps):
    # look up corresponding variable based on reps
    reps_var_name = f"reps_{reps}"
    if reps_var_name in calc_data:
        reps_value = calc_data[reps_var_name]
        estimated_1RM = weight / reps_value
        return estimated_1RM
    else:
        return None

while True:
    input_str = input("Enter weight x reps (e.g., 200x5): ")
    
    # Remove spaces and split the input string into weight and reps parts
    input_str = input_str.replace(" ", "")
    parts = input_str.split('x')
    
    if len(parts) != 2:
        print("Invalid input format. Please use weight x reps format.")
        continue
    
    weight_str, reps_str = parts
    
    if not (weight_str.isdigit() and reps_str.isdigit()):
        print("Both weight and reps should be whole numbers.")
        continue
    
    weight = float(weight_str)
    reps = int(reps_str)
    
    estimated_1RM = calculate_1RM(weight, reps)
    
    if estimated_1RM is not None:
        print("Estimated 1RM:", round(estimated_1RM))
    else:
        print("No calculation for that amount of reps")
    
    repeat = input("Type quit to exit or press Enter to continue: ")
    if repeat.lower() == "quit":
        break
