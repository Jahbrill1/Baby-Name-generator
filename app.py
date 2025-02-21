from flask import Flask, render_template, request
from babynames import load_ssa_data, get_names_by_gender  # Import from your main script

app = Flask(__name__)

@app.route('/')
def index():
    print("Index page accessed")  # Debug statement
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    gender = request.form.get('gender')
    print(f"Gender received: {gender}")  # Debug statement
    data_directory = "data"
    filenames = ["yob2023.txt"]
    name_data = load_ssa_data(data_directory, filenames)  # Call the function from baby_names.py

    if name_data is not None:
        # ...logic to filter and generate names...
        names = get_names_by_gender(name_data, gender)  # Use the gender from the form
        print(f"Names generated: {names[:5]}")  # Debug statement (print first 5 names)
        return render_template('names.html', names=names)
    else:
        print("Could not load name data.")  # Debug statement
        return "Could not load name data."

if __name__ == "__main__":
    print("Starting Flask server...")  # Debug statement
    app.run(debug=True)
