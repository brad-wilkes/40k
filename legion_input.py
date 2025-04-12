import describe_astartes

prompt = "\nEnter the name of a legion. "
prompt += "\nEnter quit to exit: "
repeat = True
while repeat:
    user_input = input(prompt)
    if user_input == 'quit':
        repeat = False
    else:
        describe_astartes.get_primarch(user_input)
        describe_astartes.get_allegiance(user_input)
