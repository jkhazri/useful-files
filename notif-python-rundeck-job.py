from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.before_request
def log_request_info():
    logging.info(f"Request: {request.method} {request.path}")
    logging.info(f"Headers: {dict(request.headers)}")
    try:
        data = request.get_json(silent=True)  # Accept JSON input
        if data:
            logging.info(f"JSON Payload: {data}")
    except Exception as e:
        logging.error(f"Error parsing JSON: {e}")

@app.after_request
def log_response_info(response):
    logging.info(f"Response: {response.status}")
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled Exception: {e}")
    return jsonify({"error": str(e)}), 500

@app.route('/v1/api/job-status', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def job_status():
    data = request.get_json(silent=True)  # Accept JSON input
    return jsonify({"message": "Request received", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
