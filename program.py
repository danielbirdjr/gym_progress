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
    "weighted pull up",
    "seated OHP", 
    "squat", 
    "SLDL"
]

completed_lifts = {}

print()

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

print()

for lift_name in preset_lifts:
    while True:
        current_lift = input(f"Current {lift_name}: ").lower()
        current_lift_weight, current_lift_reps = parse_input(current_lift)

        if current_lift_weight is None:
            print("\nTry again. Enter 'weight x reps'\n")
        else:
            completed_lifts[lift_name]["current_weight"] = current_lift_weight
            completed_lifts[lift_name]["current_reps"] = current_lift_reps
            break

print()

rep_multipliers = {
    1: 1,
    2: 0.9722,
    3: 0.9444,
    4: 0.9166,
    5: 0.8888,
    6: 0.861,
    7: 0.8332,
    8: 0.8054,
    9: 0.7767,
    10: 0.75,
    11: 0.7317,
    12: 0.7143,
    13: 0.6977,
    14: 0.6818,
    15: 0.66665,
    16: 0.6522,
    17: 0.6383,
    18: 0.625,
    19: 0.61225,
    20: 0.6,
    21: 0.58825,
    22: 0.5769,
    23: 0.56605,
    24: 0.55555,
    25: 0.54545,
    26: 0.5357,
    27: 0.5263,
    28: 0.51725,
    29: 0.50845,
    30: 0.5
}

def calculate_progress(current_weight, current_reps, goal_weight, goal_reps):
    current_multiplier = rep_multipliers.get(current_reps, None)
    goal_multiplier = rep_multipliers.get(goal_reps, None)
    
    if current_multiplier is not None and goal_multiplier is not None:
        current_1RM = current_weight / current_multiplier
        goal_1RM = goal_weight / goal_multiplier
        
        progress = (current_1RM / goal_1RM) * 100
        return progress
    else:
        return None

lift_progress = {}
for lift_name, lift_data in completed_lifts.items():
    progress = calculate_progress(
        lift_data['current_weight'],
        lift_data['current_reps'],
        lift_data['goal_weight'],
        lift_data['goal_reps']
    )
    lift_progress[lift_name] = progress

sorted_lifts = sorted(lift_progress.items(), key = lambda x: x[1])

print("Lift Progress")

for lift_name, progress in sorted_lifts:
    if progress is not None:
        formatted_lift_name = lift_name.upper() if lift_name == "SLDL" else lift_name.capitalize()
        print(f"{formatted_lift_name}: {progress:.0f}%")
    else:
        print(f"{lift_name.capitalize()}: Progress calculation not possible due to invalid reps.")

print("\nAll lifts completed!")
