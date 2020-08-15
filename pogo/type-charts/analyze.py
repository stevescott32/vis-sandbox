import json

def starting_analysis():
    with open('type-data.json') as json_file:
        data = json.load(json_file)
        for one_type in data:
            t = one_type['type']
            print('-----------------')
            print(t)
            print('-----------------')
            for weakness in one_type['weak-against']:
                print(t + ' weakness: ' + weakness)
                for other_type in data:
                    for strength in other_type['strong-against']:
                        for resist in other_type['resistant-to']:
                            if strength == weakness and resist == weakness:
                                print('-- Ideal counter: ', other_type['type'])
                        

def best_compliment():
    '''
    Find the best compliment for each type
    '''
    print('-------------------------------------')
    print('--- Running a compliment analysis ---')
    print('-------------------------------------')
    with open('type-data.json') as json_file:
        data = json.load(json_file)
        for one_type in data:
            one_type['potential-compliments'] = {}
            for other_type in data:
                one_type['potential-compliments'][other_type['type']] = calculate_compliment_score(one_type, other_type)
            best_compliment = {}
            best_compliment_score = 0
            for compliment in one_type['potential-compliments']:
                s = one_type['potential-compliments'][compliment]
                if s > best_compliment_score:
                    best_compliment_score = s
                    best_compliment = compliment
            print('A good compliment for ' + one_type['type'] + ' is: ')
            print(best_compliment)

 

def calculate_compliment_score(target, compliment):
    score = 0
    for weakness in target['weak-against']:
        for strength in compliment['strong-against']:
            for resist in compliment['resistant-to']:
                if strength == weakness and resist == weakness:
                    score = score + 3
                elif strength == weakness or resist == weakness:
                    score = score + 1
    return score


best_compliment()
