# import emoji
import random as rand
from twitter import *

# greens: 🍃 🌱 🌿 ☘️ 🍀
greens = {
    'pine_tree'             : '🌲',
    'falling_leaves'        : '🍃',
    'sprout'                : '🌱',
    'fern'                  : '🌿',
    'clover_3'              : '☘️',
    'clover_4'              : '🍀'
}

# weather: ☀️ 🌤 ⛅️ 🌥 ☁️ 🌧 ⛈ 🌩 🌨 💧 
weather = {
    'sun'                   :'☀️',
    'partly_cloudy_1'       :'🌤',
    'partly_cloudy_2'       :'⛅️',
    'partly_cloudy_3'       :'🌥',
    'cloudy'                :'☁️',
    'rain'                  :'🌧',
    'pour'                  :'🌨',
    'thunderstorm'          :'⛈',
    'thunderstorm_no_rain'  :'🌩'
}

# animals: 🐿 🦝 🐇 🦔 
animals = {
    'chipmunk'              :'🐿',
    'raccoon'               :'🦝',
    'rabbit'                :'🐇',
    'hedghog'               :'🦔'
}

# flowers: 🌸 🌻 🌺 🌷 🌼
flowers = {
    'cherry_blossum'        :'🌸',
    'sunflower'             :'🌻',
    'hibiscus'              :'🌺',
    'tulip'                 :'🌷',
    'daisy'                 :'🌼'
}


# etc: 🪨 🏕
etc = {
    'rock'                  :'🪨'
}

def choose_emoji(row, col):
    emoji = ' '
    main_option = rand.randrange(0,14)
    extra_option = rand.randrange(1,6)

    if main_option <= 1:
        if extra_option == 1:
            return rand.choice(list(etc.values()))
        elif extra_option == 2:
            return rand.choice(list(flowers.values()))
        else:
            return rand.choice(list(animals.values()))
    
    elif main_option <= 8:
        if extra_option == 1:
            return rand.choice(list(greens.values()))
        else:
            return greens.get('pine_tree')
    
    return ' '

# 9x7 is a good mobile fit
# call make_tweet(message) in here after generating grid
if __name__ == '__main__':
    col = 9
    row = 7
    output = ''
    for i in range(row):
        for j in range(col):
            output += choose_emoji(i, j) + ' '
        output += '\n'

    make_tweet(output)