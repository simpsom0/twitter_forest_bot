# import emoji
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
    'rock'                  :'🪨',
    'campsite'              :'🏕'
}

# 9x7 is a good mobile fit
# call make_tweet(message) in here after generating grid
if __name__ == '__main__':
    print('testing : 🌲')