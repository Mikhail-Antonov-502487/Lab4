def knapsack_all_combinations(items, CAP):
    def backtrack(index, Name, Weight, Value, Items, results):
        results.append({
            'Name' : Name,
            'weight': Weight,
            'value': Value,
            'items': Items.copy(),
            'items_indexes': [i for i, includ in enumerate(Items) if includ]
        })
        
        for i in range(index, len(items)):
            name, weight, value = items[i]
            if Weight + weight <= CAP:
                Items[i] = True
                backtrack(i + 1, 
                        Name + [name] * weight,
                         Weight + weight, 
                         Value + value, 
                         Items, 
                         results)
                Items[i] = False
    
    results = []
    backtrack(0, [], 0, 15, [False] * len(items), results)
    return results

if __name__ == '__main__':
    items = [('r', 3, 25), 
            ('p', 2, 15), 
            ('a', 2, 15),
            ('m', 2, 20),
            ('i', 1, 5),
            ('k', 1, 15),
            ('x', 3, 20),
            ('t', 1, 25),
            ('f', 1, 15),
            ('d', 1, 10),
            ('s', 2, 20),
            ('c', 2, 20)]   
    ABS_value = 205    
    CAP = int(input())  
    EXP = 15
    maxi = 0
    
    for i in knapsack_all_combinations(items, CAP):
        if (i['value'] + EXP) > (ABS_value - i['value']):
            print(i['Name'], (i['value'] + EXP - (ABS_value - i['value'])))
        if (i['value'] + EXP - (ABS_value - i['value'])) >= maxi:
            maxi = (i['value'] + EXP - (ABS_value - i['value']))

    print(maxi)

