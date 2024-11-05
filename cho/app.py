from flask import Flask, render_template, request, redirect, url_for
from models import ChocolateHouseDB

# Initialize Flask app
app = Flask(__name__)

# Initialize the database
db = ChocolateHouseDB()

# Route for the home page
@app.route('/')
def index():
    flavors = db.get_flavors()
    ingredients = db.get_ingredients()
    feedback = db.get_customer_feedback()
    
    # Debugging: Print data to verify content
    print("Flavors:", flavors)
    print("Ingredients:", ingredients)
    print("Feedback:", feedback)

    return render_template('index.html', flavors=flavors, ingredients=ingredients, feedback=feedback)


# Route for adding a new flavor
@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        season = request.form['season']
        
        db.add_flavor(name, description, season)
        return redirect(url_for('index'))

    return render_template('add_flavor.html')

# Route for adding a new ingredient
@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        name = request.form['name']
        stock_quantity = request.form['stock_quantity']
        
        db.add_ingredient(name, stock_quantity)
        return redirect(url_for('index'))

    return render_template('add_ingredient.html')

# Route for adding customer feedback
@app.route('/add_feedback', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        flavor_id = request.form['flavor_id']
        suggestion = request.form['suggestion']
        allergy_concern = request.form['allergy_concern']

        db.add_customer_feedback(flavor_id, suggestion, allergy_concern)
        return redirect(url_for('index'))

    # Fetch the available flavors to show in the form
    flavors = db.get_flavors()
    return render_template('add_feedback.html', flavors=flavors)

# Run the app
if __name__ == '__main__':
    db.create_tables()  # Create tables if they don't exist
    app.run(host='0.0.0.0', port=5000, debug=True)


