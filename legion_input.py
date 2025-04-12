legions = {
    'sons of horus' : {
        'primarch' : 'horus',
        'traitor' : True,
        'number' : 16
    },
    'ultramarines' : {
        'primarch' : 'guilliman',
        'traitor' : False,
        'number' : 13
    },
    'world eaters' : {
        'primarch' : 'angron',
        'traitor' : True,
        'number' : 12
    },
    'iron warriors' : {
        'primarch' : 'perturabo',
        'traitor' : True,
        'number' : 10
    },
    'salamanders' : {
        'primarch' : 'vulkan',
        'traitor' : False,
        'number' : 18
    },
    'raven guard' : {
        'primarch' : 'corax',
        'traitor' : False,
        'number' : 19
    },
    'imperial fists' : {
        'primarch' : 'dorn',
        'traitor' : False,
        'number' : 7
    },
    'night lords' : {
        'primarch' : 'konrad curze',
        'traitor' : True,
        'number' : 8
    },
    'white scars' : {
        'primarch' : 'jaghatai khan',
        'traitor' : False,
        'number' : 5
    },
    'iron hands' : {
        'primarch' : 'ferrus manus',
        'traitor' : False,
        'number' : 10
    },
    'blood angels' : {
        'primarch' : 'sanguinius',
        'traitor' : False,
        'number' : 9
    },
    'death guard' : {
        'primarch' : 'mortarion',
        'traitor' : True,
        'number' : 14
    },
    'dark angels' : {
        'primarch' : 'lion el jonson',
        'traitor' : False,
        'number' : 1
    },
    'thousand sons' : {
        'primarch' : 'magnus the red',
        'traitor' : True,
        'number' : 15
    },
    'space wolves' : {
        'primarch' : 'leman russ',
        'traitor' : False,
        'number' : 6
    },
    'word bearers' : {
        'primarch' : 'lorgar',
        'traitor' : True,
        'number' : 17
    },
    'alpha legion' : {
        'primarch' : 'alfarius',
        'traitor' : True,
        'number' : 11
    },
    'emperor\'s children' : {
        'primarch' : 'fulgrim',
        'traitor' : True,
        'number' : 4
    },
}

def query_legions(legion):
    for legion, primarch in legions.items():
        if user_input == legion:
            print(f"\n\tThe primarch of {user_input.title()} is {primarch['primarch'].title()}\n")
        else:
            print(f"User input does not match key {legion.title()} ")

prompt = "\nEnter the name of a legion. "
prompt += "\nEnter quit to exit: "
repeat = True
while repeat:
    user_input = input(prompt)
    if user_input == 'quit':
        repeat = False
    else:
        query_legions(user_input)
