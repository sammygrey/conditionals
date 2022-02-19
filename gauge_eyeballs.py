import math

eye_size = 0.47    # [cm^2]
eye_width = 24.2   # [mm]
eye_height = 23.7  # [mm]

iris_width = 20.2  # [mm]
iris_height = 19.7 # [mm]

if eye_size > 0.45 and (math.pi*iris_width/2*iris_height/2) / eye_size >= 0.69 and \
        eye_height/eye_width >= 0.59:
    print("I'm sorry I wasn't part of your past, can I make it up by being in your future?")