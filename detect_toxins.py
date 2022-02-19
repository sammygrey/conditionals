def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

toxins = {'sodium nitrate':0,
'sodium benzoate':0, 'sodium oxide':0} #dictionary instead of array because O(1) lookup time ingrained in my brain

ingredients = ['sodium benzoate']
for ingredient in ingredients:
    if toxins.get(ingredient):
        print('!!!')
        print('there is a toxin in the food!')    
        print('!!!')
        make_alert_sound()
print('***')
print('Toxin Free')
print('***')
make_accept_sound()