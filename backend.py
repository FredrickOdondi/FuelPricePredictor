from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    crude_oil_price = float(data['crudeOilPrice'])
    
    # Example conversion rates (adjust as necessary)
    diesel_ratio = 0.12
    petrol_ratio = 0.15
    paraffin_ratio = 0.1

    # Calculate the prices
    diesel_price = round(crude_oil_price * diesel_ratio, 2)
    petrol_price = round(crude_oil_price * petrol_ratio, 2)
    paraffin_price = round(crude_oil_price * paraffin_ratio, 2)

    return jsonify({
        'dieselPrice': diesel_price,
        'petrolPrice': petrol_price,
        'paraffinPrice': paraffin_price
    })

if __name__ == '__main__':
    app.run(debug=True)
