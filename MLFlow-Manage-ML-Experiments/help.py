import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

with mlflow.start_run(run_name="Test 2") as run:
    mlflow.set_tag("version", "1.0.0")

mlflow.end_run()
