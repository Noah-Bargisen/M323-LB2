from flask import Flask, request

app = Flask(__name__)

# A1G: Beschreibung von Funktionen und Unterschiede zu anderen Strukturen
@app.route('/add')
def add_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a + b
    return f"The sum of {a} and {b} is: {result}"

# A1F: Konzept von immutable values und Anwendung
PI = 3.14159

# A1E: Vergleich der Konzepte: Prozedural vs. Funktional
@app.route('/add_procedural')
def add_procedural():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a + b
    return f"The sum of {a} and {b} is: {result}"

@app.route('/add_functional')
def add_functional():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sum([a, b])
    return f"The sum of {a} and {b} is: {result}"

# B1G: Erklärung eines Algorithmus und Aufteilung in funktionale Teilstücke
def multiply_numbers(a, b):
    return a * b

@app.route('/multiply')
def multiply_endpoint():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = multiply_numbers(a, b)
    return f"The product of {a} and {b} is: {result}"

# B1F: Aufteilung von Algorithmen in funktionale Teilstücke
@app.route('/subtract')
def subtract_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = subtract(a, b)
    return f"The difference of {a} and {b} is: {result}"

def subtract(a, b):
    return a - b

# B1E: Implementierung von zusammenhängenden Funktionen
@app.route('/calculate')
def calculate_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    add_result = add(a, b)
    subtract_result = subtract(a, b)
    multiply_result = multiply_numbers(a, b)
    divide_result = divide(a, b)
    return f"Results: Addition={add_result}, Subtraction={subtract_result}, Multiplication={multiply_result}, Division={divide_result}"

def add(a, b):
    return a + b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

# B2G: Speicherung von Funktionen als Objekte in Variablen
power = lambda a, b: a ** b
square_root = lambda a: a ** 0.5 if a >= 0 else "Error: Imaginary number"

# B2F: Verwendung von Funktionen als Argumente für andere Funktionen
@app.route('/perform_operation')
def perform_operation():
    operation = request.args.get('operation')
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = execute_operation(operation, a, b)
    return f"The result of the operation is: {result}"

def execute_operation(operation, a, b):
    if operation == 'add':
        return add(a, b)
    elif operation == 'multiply':
        return multiply_numbers(a, b)
    # Weitere Operationen hinzufügen

# B2E: Verwendung von Funktionen als Objekte und Argumente, um komplexe Aufgaben auszuführen (Anwenden von Closures)
@app.route('/calculate_with_closure')
def calculate_with_closure():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    def create_calculator(operation):
        def calculate(a, b):
            return operation(a, b)
        return calculate

    add = lambda a, b: a + b
    subtract = lambda a, b: a - b

    cal_add = create_calculator(add)
    cal_subtract = create_calculator(subtract)

    add_result = cal_add(a, b)
    subtract_result = cal_subtract(a, b)

    return f"Results using closures - Addition: {add_result}, Subtraction: {subtract_result}"

# B3G: Implementierung einfacher Lambda-Ausdrücke
square = lambda x: x * x

@app.route('/calculate_square')
def calculate_square():
    number = int(request.args.get('number'))
    result = square(number)
    return f"Square of the number is: {result}"

# B3F: Schreiben von Lambda-Ausdrücken, die mehrere Argumente verarbeiten können
multiply = lambda a, b: a * b

@app.route('/multiply_numbers')
def multiply_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = multiply(a, b)
    return f"Multiplication result is: {result}"

# B3E: Verwendung von Lambda-Ausdrücken zur Steuerung des Programmflusses
numbers = [5, 10, 15, 20, 25]
sorted_list = sorted(numbers, key=lambda x: x % 3)


# B4G: Anwendung der Funktionen Map, Filter und Reduce einzeln auf Listen
@app.route('/squared_numbers')
def squared_numbers():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    return f"Squared numbers: {squared_numbers}"


# B4F: Kombinierte Verwendung von Map, Filter und Reduce für komplexe Datenmanipulation
@app.route('/sum_of_even_squared')
def sum_of_even_squared():
    numbers = [1, 2, 3, 4, 5]
    result = sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    return f"Sum of squares of even numbers: {result}"


# B4E: Verwendung von Map, Filter und Reduce für komplexe Datenverarbeitungsaufgaben
@app.route('/average_height')
def average_height():
    data = [{"name": "Alice", "height": 165}, {"name": "Bob", "height": 180}, {"name": "Charlie", "height": 175}]
    average_height = sum(map(lambda x: x["height"], data)) / len(data)
    return f"Average height: {average_height}"


# C1G: Beschreibung von Refactoring-Techniken für verbesserte Lesbarkeit
@app.route('/cylinder_volume')
def calculate_cylinder_volume():
    radius = int(request.args.get('radius'))
    height = int(request.args.get('height'))
    pi = 3.14159
    volume = pi * radius * radius * height
    return f"Volume of cylinder: {volume}"


# Refaktorierter Code
@app.route('/cylinder_volume_refactored')
def calculate_cylinder_volume_refactored():
    radius = int(request.args.get('radius'))
    height = int(request.args.get('height'))
    pi = 3.14159
    base_area = pi * radius * radius
    volume = base_area * height
    return f"Volume of cylinder (refactored): {volume}"


# C1F: Verbesserung der Lesbarkeit durch Refactoring
@app.route('/cylinder_volume_v2')
def calculate_cylinder_volume_v2():
    radius = int(request.args.get('radius'))
    height = int(request.args.get('height'))
    pi = 3.14159
    volume = pi * radius * radius * height
    return f"Volume of cylinder: {volume}"


# Refaktorierter Code
@app.route('/cylinder_volume_v2_refactored')
def calculate_cylinder_volume_v2_refactored():
    radius = int(request.args.get('radius'))
    height = int(request.args.get('height'))
    pi = 3.14159
    base_area = pi * radius * radius
    volume = base_area * height
    return f"Volume of cylinder (refactored): {volume}"


# C1E: Einschätzung der Auswirkungen des Refactorings
@app.route('/calculate_area')
def calculate_area():
    length = int(request.args.get('length'))
    width = int(request.args.get('width'))

    if length > 0 and width > 0:
        return f"Area of rectangle: {length * width}"
    else:
        return "Invalid dimensions"

if __name__ == "__main__":
    app.run(debug=True)
