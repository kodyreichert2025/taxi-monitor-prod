How to Run the Project Locally


Installation Requirements

Docker 

Git

Python


1. Clone the repository

git clone https://github.com/kodyreichert2025/taxi-monitor-prod.git
cd taxi-monitor-prod


2: Start the application stack

Run the following command from the project folder:

docker compose up --build

This starts three services:

Flask app on http://localhost:8080

Prometheus on http://localhost:9090

Grafana on http://localhost:3000



3. Verify the Flask application

Open terminal 

curl http://localhost:8080

Expected response:

{"prediction":0,"status":"ok"}


4: Verify the metrics endpoint

curl http://localhost:8080/metrics

This should return Prometheus metrics text.


5: Open Prometheus


http://localhost:9090


Try the following:

taxi_requests_total



6: Open Grafana



http://localhost:3000

Default login:

Username: admin

Password: admin



7: Add Prometheus as a Grafana data source


In Grafana:

Open Connections

Select Data Sources

Add Prometheus

Use this URL:

http://prometheus:9090

Click Save & Test


8: Generate traffic

To create visible data in Prometheus and Grafana, send requests to the app:

curl http://localhost:8080
curl http://localhost:8080
curl http://localhost:8080



9: Verify monitoring in Grafana

Create panels using the following Prometheus queries:

taxi_requests_total

taxi_predictions_total

rate(taxi_requests_total[1m])

taxi_request_latency_seconds_count

These metrics should update as traffic is generated.


10. Verify Cloud Monitoring 


Open Google Cloud Console

Go to Observability > Monitoring > Metrics Explorer


Cloud Run Revision

View metrics such as:

Request count, Request latency, CPU utilization, Memory utilization, Instance count


11. GitHub Actions

To verify the workflow:

Open the repo in GitHub

Go to the Actions tab

Review the latest workflow runs


How to Stop the Project

When finished, stop the containers with:

docker compose down
