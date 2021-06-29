

def max_value(dicto):
    max_value = -1
    key_ = ''
    for key in dicto.keys():
        if dicto[key] >= max_value:
            max_value = dicto[key]
            key_ = key
    return key_,max_value


best = {'dio':12., 'cane': 124,'porco':124151}
key, max = max_value(best)
del best[key]
key, max = max_value(best)
print(key, max)