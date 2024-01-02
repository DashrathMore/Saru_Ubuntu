from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/trigger_dag', methods=['POST'])
def trigger_dag():
    dag_id = 'aa'  # Replace with your DAG ID
    trigger_url = f'http://localhost:8080/dags/{dag_id}/dag_runs'

    response = requests.post(trigger_url, json={}, headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        return 'DAG triggered successfully!'
    else:
        return f'Error triggering DAG: {response.text}', 500

if __name__ == '__main__':
    app.run(debug=True)