# create a function to take the input (weight x reps) 
# and seperate them values using 'x' or 'for'
# allow CAP letters and spaces before and after



#correct version
seperator_options = ['x', 'for']

def parse_input(input_str):
    lower_input_str = input_str.lower()
    for seperator in seperator_options:
        if seperator in lower_input_str:
            weight_str, reps_str = lower_input_str.split(seperator)
            try:
                weight = float(weight_str)
                reps = int(reps_str)
                return weight, reps
            except ValueError:
                return None, None
    return None, None