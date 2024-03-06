# Define basic astronomy data
astronomy_data = {
    'planets': {
        'mercury': 'Mercury is the smallest planet in our solar system and the closest to the Sun.',
        'venus': 'Venus is the second planet from the Sun and is often called Earth’s "sister planet" because of their similar size, mass, proximity to the Sun, and bulk composition.',
        'earth': 'Earth is the third planet from the Sun and is the only astronomical object known to harbor life.',
        'mars': 'Mars is often called the "Red Planet" due to its reddish appearance, caused by iron oxide prevalent on its surface.',
        'jupiter': 'Jupiter is the largest planet in our solar system and is primarily composed of hydrogen and helium.',
        'saturn': 'Saturn is known for its prominent ring system, which is made up of ice particles, rocky debris, and dust.',
        'uranus': 'Uranus is the seventh planet from the Sun and is known for its unique tilt, which causes it to rotate on its side.',
        'neptune': 'Neptune is the eighth planet from the Sun and is known for its deep blue coloration, caused by methane in its atmosphere.'
    },
    'stars': {
        'sun': 'The Sun is the star at the center of our solar system and is the most important source of energy for life on Earth.',
        'proxima centauri': 'Proxima Centauri is the closest known star to the Sun and is part of the Alpha Centauri star system.',
        'sirius': 'Sirius, also known as the "Dog Star", is the brightest star in the night sky.',
        'betelgeuse': 'Betelgeuse is a red supergiant star and one of the largest stars known.',
        'rigel': 'Rigel is a blue supergiant star located in the constellation of Orion.'
    },
    'missions': {
        'apollo 11': 'Apollo 11 was the first manned mission to land on the Moon, led by astronauts Neil Armstrong, Buzz Aldrin, and Michael Collins.',
        'voyager 1': 'Voyager 1 is a space probe launched by NASA in 1977. It has traveled farther from Earth than any other human-made object.',
        'curiosity rover': 'The Curiosity rover is a car-sized rover exploring Gale Crater on Mars as part of NASA\'s Mars Science Laboratory mission.'
    }
}


def generate_response(intent, entity):
    if intent == 'planet':
        return get_planet_info(entity)
    elif intent == 'star':
        return get_star_info(entity)
    elif intent == 'mission':
        return get_mission_info(entity)
    else:
        return "I'm sorry, I'm not sure how to answer that."



def parse_user_message(user_message):
    user_message = user_message.lower()
    if 'planet' in user_message:
        intent = 'planet'
        entity = user_message.split('planet ')[-1].strip()
    elif 'star' in user_message:
        intent = 'star'
        entity = user_message.split('star ')[-1].strip()
    elif 'mission' in user_message:
        intent = 'mission'
        entity = user_message.split('mission ')[-1].strip()
    else:
        intent = 'unknown'
        entity = None
    return intent, entity


def get_planet_info(planet):
    if planet in astronomy_data['planets']:
        return astronomy_data['planets'][planet]
    else:
        return "I'm sorry, I don't have information about that planet."


def get_star_info(star):
    if star in astronomy_data['stars']:
        return astronomy_data['stars'][star]
    else:
        return "I'm sorry, I don't have information about that star."


def get_mission_info(mission):
    if mission in astronomy_data['missions']:
        return astronomy_data['missions'][mission]
    else:
        return "I'm sorry, I don't have information about that mission."


# Example usage
# while(True):
#     user_input = input("Ask me about a planet, star, or space mission: ")
#     intent, entity = parse_user_message(user_input)
#     response = generate_response(intent, entity)
#
#     print(response)
#


from flask import Flask, render_template, request

app = Flask(__name__)

# Define basic astronomy data
# (your astronomy_data dictionary and functions go here)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_input = request.form['user_input']
    intent, entity = parse_user_message(user_input)
    response = generate_response(intent, entity)
    return render_template('result.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)

