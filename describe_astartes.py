
legions = {
    'sons of horus' : {
        'primarch' : 'horus',
        'traitor' : True,
        'number' : 16,
        'battlecry' : 'For the Warmaster'
    },
    'ultramarines' : {
        'primarch' : 'guilliman',
        'traitor' : False,
        'number' : 13,
        'battlecry' : 'For Macragge'
    },
    'world eaters' : {
        'primarch' : 'angron',
        'traitor' : True,
        'number' : 12,
        'battlecry' : 'For Khorne'
    },
    'iron warriors' : {
        'primarch' : 'perturabo',
        'traitor' : True,
        'number' : 10,
        'battlecry' : 'For the Iron Cage'
    },
    'salamanders' : {
        'primarch' : 'vulkan',
        'traitor' : False,
        'number' : 18,
        'battlecry' : 'For Nocturne'
    },
    'raven guard' : {
        'primarch' : 'corax',
        'traitor' : False,
        'number' : 19,
        'battlecry' : 'For Deliverance'
    },
    'imperial fists' : {
        'primarch' : 'dorn',
        'traitor' : False,
        'number' : 7,
        'battlecry' : 'For Terra'
    },
    'night lords' : {
        'primarch' : 'konrad curze',
        'traitor' : True,
        'number' : 8,
        'battlecry' : 'For the Night'
    },
    'white scars' : {
        'primarch' : 'jaghatai khan',
        'traitor' : False,
        'number' : 5,
        'battlecry' : 'For Chogoris'
    },
    'iron hands' : {
        'primarch' : 'ferrus manus',
        'traitor' : False,
        'number' : 10,
        'battlecry' : 'For Medusa'
    },
    'blood angels' : {
        'primarch' : 'sanguinius',
        'traitor' : False,
        'number' : 9,
        'battlecry' : 'For Baal'
    },
    'death guard' : {
        'primarch' : 'mortarion',
        'traitor' : True,
        'number' : 14,
        'battlecry' : 'For Nurgle'
    },
    'dark angels' : {
        'primarch' : 'lion el jonson',
        'traitor' : False,
        'number' : 1,
        'battlecry' : 'For Caliban'
    },
    'thousand sons' : {
        'primarch' : 'magnus the red',
        'traitor' : True,
        'number' : 15,
        'battlecry' : 'For Tzeentch'
    },
    'space wolves' : {
        'primarch' : 'leman russ',
        'traitor' : False,
        'number' : 6,
        'battlecry' : 'For Fenris'
    },
    'word bearers' : {
        'primarch' : 'lorgar',
        'traitor' : True,
        'number' : 17,
        'battlecry' : 'For Chaos'
    },
    'alpha legion' : {
        'primarch' : 'alfarius',
        'traitor' : True,
        'number' : 11,
        'battlecry' : 'For the Hydra'
    },
    'emperor\'s children' : {
        'primarch' : 'fulgrim',
        'traitor' : True,
        'number' : 4,
        'battlecry' : 'For Slaanesh'
    },
}

# Prints legion, primarch, and traitor status based on the dictionary attributes
def detail_astartes():
    for legion, primarch in legions.items():
        print(f"The primarch of {legion} is {primarch['primarch'].title()}")
        if primarch['traitor']:
            print(f"\tDeath to the Anathema. {primarch['battlecry']}")
        else:
            print(f"\tFor the Emperor of Mankind. {primarch['battlecry']}")

# Separates the traitor and loyalist legions into two lists
def get_allegiance(user_astartes):
    # create two empty lists to hold each group
    loyalists = []
    traitors = []
    for legion, allegiance in legions.items():
        if allegiance['traitor']:
            traitors.append(legion)
        else:
            loyalists.append(legion)
    if user_astartes in traitors:
        print(f"\n\tThe {user_astartes.title()} are a traitor legion")
    elif user_astartes in loyalists:
        print(f"\n\tThe {user_astartes.title()} are a loyalist legion")
    else:
        print(f"\n\t{user_astartes} not found")

# Match parameter (user input) to the dictionary keys (legions)
def get_primarch(user_input):
    for legion, primarch in legions.items():
        if user_input == legion:
            print(f"\nThe primarch of {user_input.title()} is {primarch['primarch'].title()}")
        else:
            continue
