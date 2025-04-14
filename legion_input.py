import describe_astartes

prompt = "\nEnter the name of a legion. "
prompt += "\nEnter 'printall' to print all legion details,"
prompt += "\n\tor enter 'quit' to exit: "
repeat = True
while repeat:
    user_input = input(prompt)
    if user_input == 'quit':
        repeat = False
    elif user_input == 'printall':
        describe_astartes.detail_astartes()
    else:
        describe_astartes.get_primarch(user_input)
        describe_astartes.get_allegiance(user_input)
