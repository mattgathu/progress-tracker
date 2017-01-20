

def show_progress(data):
    completed = [key for key in data if key]
    not_completed = [key for key in data if not key]

    print('---------------------------------------------')
    print('\t SKILL   | \t STATUS')
    print('---------------------------------------------')
    print('')

    for key in data:
        if data[key]:
            print('\t {}   | \t {}'.format(key, "COMPLETED"))
        else:
            print('\t {}   | \t {}'.format(key, "NOT COMPLETED"))
        print('---------------------------------------------')
