# create a function to take the input (weight x reps) 
# and seperate them values using 'x' or 'for'
# allow CAP letters and spaces before and after

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


#make a list with the different lifts

preset_lifts = [
  "bench press", 
  'weighted pull up', 
  'seated OHP', 
  'squat', 
  'SLDL'
]

#make an empty dictionary that will eventually store the completed lifts

completed_lifts = {}


#iterate through preset lifts, and get the user input of goal lift (weight and reps) for each lift
#store completed lifts in dictionary with their goal weight and reps

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
    #correct version
    # else:
    #         completed_lifts[lift_name] = {
    #             "goal_weight": goal_lift_weight,
    #             "goal_reps": goal_lift_reps,
    #             "current_weight": None,
    #             "current_reps": None
    #         }
    #         break



print()

#iterate through preset_lifts with lift_name
#get user input for current_lift and seperate them into weight and reps
#make sure weight is valid, reps is valid and if so, store current weight and reps in completed_lifts dictionary under lift_name
for lift_name in preset_lifts:
  while True: 
    current_lift = input(f"Current {lift_name}: ").lower()
    current_lift_weight, current_lift_reps = parse_input(current_lift)

    if current_lift_weight is None: 
      print("Try again, weight x reps")
    elif current_lift_reps < 1 or current_lift_reps > 30: 
      print("Enter reps 1-30")
    else: 
      completed_lifts[lift_name] = {
        "Goal weight": goal_lift_weight, 
        "Goal reps": goal_lift_reps, 
        "Current weight": current_lift_weight, 
        "Current reps": current_lift_reps
      }

      completed_lifts[lift_name]["current_weight"] = current_lift_weight
      completed_lifts[lift_name]["current_reps"] = current_lift_reps
      break
      #correct version
      # else:
      #   completed_lifts[lift_name]["current_weight"] = current_lift_weight
      #   completed_lifts[lift_name]["current_reps"] = current_lift_reps
      #   break

#found these myself
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

#create a function called calculate_progress when given current_weight, current_reps, goal_weight, goal_reps
#I DONT FULLY UNDERSTAND GOAL AND CURRENT MULTIPLIER
#find multipliers for goal and current reps; goal_multiplier and current_multiplier
#use if statement and find current_1RM and goal_1RM
#find progress and make it a percentage
def calculate_progress(current_weight, current_reps, goal_weight, goal_reps):
    goal_multiplier = rep_multipliers.get(goal_reps, None)
    current_multiplier = rep_multipliers.get(current_reps, None)

    if goal_multiplier and current_multiplier is not None:
        goal_1RM = goal_weight / goal_multiplier
        current_1RM = current_weight / current_multiplier

        progress = (current_1RM / goal_1RM) * 100
        return progress #ask why you have to do this line
    else: 
        return None
    

    