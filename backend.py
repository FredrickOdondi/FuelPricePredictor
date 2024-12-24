from flask import Flask, request, jsonify
import boto3
import json

app = Flask(__name__)

# AWS SageMaker client
sagemaker_client = boto3.client('sagemaker-runtime', region_name='your-region')

# Endpoint name
SAGEMAKER_ENDPOINT = "your-sagemaker-endpoint-name"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get data from the frontend
        payload = json.dumps(data)  # Convert data to JSON string
        
        # Invoke SageMaker endpoint
        response = sagemaker_client.invoke_endpoint(
            EndpointName=SAGEMAKER_ENDPOINT,
            ContentType='application/json',
            Body=payload
        )
        
        # Decode response
        result = json.loads(response['Body'].read().decode())
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
