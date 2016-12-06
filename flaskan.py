from flask import Flask, render_template
from food import Food


app = Flask(__name__)

# Load config file
app.config.from_pyfile('settings.cfg', silent=False)

# Tuple with objects of Food
foods = (
    Food('Banana', 200, 'Southeast Asia', 'Is a herb.'),
    Food('Watermelon', 30, 'Southern Africa', 'Worlds biggest berry.'),
    Food('Kale', 50, 'Greece', 'The closest relative to wild cabbage.')
)


# Display 'Hello World!'
@app.route('/hello')
def hello_world():
    return 'Hello World!'


# Display 'Hello <username>!'
@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello %s!' % username


# Render template displaying all foods in tuple
@app.route('/food/')
def show_foods():
    return render_template('show_foods.html', foods=foods)


# Render template displaying a specific food
@app.route('/food/<int:index>')
def show_food(index):
    # Check if index is 0 or greater and shorter than tuple length
    # if true generate template else return not found
    if (index >= 0) and (index < len(foods)):
        return render_template('show_food.html', food=foods[index])
    else:
        return 'No food with index %s was found!' % index


if __name__ == '__main__':
    app.run()
