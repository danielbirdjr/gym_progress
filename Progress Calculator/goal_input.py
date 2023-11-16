#iterate through preset lifts, and get the user input of goal lift (weight and reps) for each lift
#store completed lifts in dictionary with their goal weight and reps




#correct version
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
