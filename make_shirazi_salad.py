def make_shirazi_salad(ingredients):
    required_ingredients = ['cucumber', 'tomato', 'onion', 'lemon juice']
    if all(ingredient in ingredients for ingredient in required_ingredients):
        print("diced all ingredients.")
        print("mixed all.")
        print('added salt.')
        print('poured lemon juice.')
        print('Your yummy shirazi salad is ready!')
        return
    print('lacks ingredients.')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])