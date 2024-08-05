import argparse
import os
import time

import mlflow


def main(inp1, inp2):
    mlflow.set_experiment("Demo Experiment")
    # with mlflow.start_run(run_name='Example_Demo'):
    with mlflow.start_run():
      mlflow.log_param("param1", inp1)
      mlflow.log_param("param2", inp2)
      metric = eval(p1=inp1, p2=inp2)
      mlflow.log_metric("Eval_Metric", metric)
      os.makedirs("dummy", exist_ok=True)
      with open("C:/Users/sushant.raj/PycharmProjects/MLOPS_Training/MLFlow-Manage-ML-Experiments/dummy/example.txt",
          "wt") as f:
       f.write(f"Artifact Created {time.asctime()}")
       mlflow.log_artifact("dummy")


def eval(p1, p2):
    output_metric = p1 ** p2 + p2 ** 2
    return output_metric


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--param1", "-p1", type=int, default=0)
    args.add_argument("--param2", "-p2", type=int, default=10)
    parsed_args = args.parse_args()
    # parsed_args.param1
    main(parsed_args.param1, parsed_args.param2)
