from datetime import datetime



def get_timestamp():
	
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))



PEOPLE = {
    'Farrell': {
        'fname': 'Doug',
        'lname': 'Farrell',
        'timestamp': get_timestamp()
    },
    'Brockman': {
        'fname': 'Kent',
        'lname': 'Brockman',
        'timestamp': get_timestamp()
    },
    'Easter': {
        'fname': 'Bunny',
        'lname': 'Easter',
        'timestamp': get_timestamp()
    }
}



def read():
    '''
    This function responds to a request for /api/people
    with the complete lists of people

    :return: sorted list of people
    '''
    # Create the list of people from our data using Python list comprehension
    peoples = [PEOPLE[key] for key in sorted(PEOPLE.keys())]
    print(type(peoples))
    print(peoples)
    
    return peoples