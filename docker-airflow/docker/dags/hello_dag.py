data_sources = [
    's3://bucket/data_source1.csv',
    '/usr/local/data/file.csv',
    '/usr/local/',
]

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


def python_fun(number, **kwargs):
    # Process the data source (e.g., load data, perform transformations)
    print(f"number: {number}")
    return number

    # Define the task for the data source


def add_fn():
    print("addition")


def createDag(dag_name):
    with DAG(dag_name, default_args=default_args, schedule=None) as dag:
        tasks = []
        for i in range(1, 5):
            task = PythonOperator(
                task_id=f'free_{i}',
                python_callable=python_fun,
                op_kwargs={'number': i},
                provide_context=True,
                dag=dag
            )
            tasks.append(task)

        end_task = PythonOperator(
            task_id='end_task',
            python_callable=add_fn,
            dag=dag
        )

        tasks >> end_task


createDag("dynamic_dag_1")
createDag("dynamic_dag_2")