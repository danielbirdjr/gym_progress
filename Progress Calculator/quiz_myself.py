# make a list with the different lifts, name it preset_lifts
# correct
preset_lifts = [
    "bench press",
    "weighted pull up",
    "seated OHP", 
    "squat", 
    "SLDL"
]

# attempt
preset_lifts = [
    'lift 1',
    'lift 2',
    'lift 3'
]



# make an empty dictionary that will eventually store the completed lifts
completed_lifts = {}

# attmept
completed_lifts = {}

# iterate through preset lifts, and get the user input of goal lift (weight and reps) for each lift
# store completed lifts in dictionary with their goal weight and reps

# correct
for lift_name in preset_lifts:
    while True:
        goal_lift = input(f"Goal {lift_name}: ").lower()
        goal_lift_weight, goal_lift_reps = parse_input(goal_lift)

        if goal_lift_weight is None:
            print("\nTry again. Enter 'weight x reps'\n")
        else:
            completed_lifts[lift_name] = {
                "goal_weight": goal_lift_weight,
                "goal_reps": goal_lift_reps,
                "current_weight": None,
                "current_reps": None
            }
            break
        
# attmept
for lift_name in preset_lifts:
    while True:
        goal_lift = input(f"Goal {lift_name}: ").lower()
        goal_lift_weight, goal_lift_reps = parse_input(goal_lift)

        if goal_lift_weight is None:
            print("Try again, weight x reps")
        
        elif goal_lift_reps < 1 or goal_lift_reps > 30:
            print("Enter reps 1-30")
        
        else:
            completed_lifts[lift_name] = {
                "goal_weight": goal_lift_weight,
                "goal_reps": goal_lift_reps,
                "current_weight": None,
                "current_reps": None
            }
            break




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

preset_lifts = [
    "bench press", 
    "pull up", 
    "OHP"
]

completed_lifts = {}

# iterate through preset lifts, and get the user input of goal lift (weight and reps) for each lift
# store completed lifts in dictionary with their goal weight and reps

for lift_name in preset_lifts:
    while True: 
        goal_lift = input(f"Goal {lift_name}: ").lower()
        goal_lift_weight, goal_lift_reps = parse_input(goal_lift)

        if goal_lift_weight is None:
            print("Enter weight x reps")
        elif goal_lift_reps < 1 or goal_lift_reps > 30:
            print("Enter reps 1-30")
        else: 
            completed_lifts[lift_name] = {
                "goal weight": goal_lift_weight,
                "goal reps": goal_lift_reps, 
                "current weight": None, 
                "current reps": None
            }
            break