from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Francieli Muniz',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
   dag_id='my_first_dag',
   default_args=default_args,
   description='This is my first dag that I write in this course',
   start_date=datetime(2025, 8, 1),
   schedule_interval='@daily',
   catchup=False

) as dag:
    task_1 = BashOperator(
        task_id='first_task',
        bash_command="echo 'Hello World, I am the first_task! :)'"
    )

    task_2 = BashOperator(
        task_id='second_task',
        bash_command="echo 'Hi, I am second_task and I will be running after first_task! :D'"
    )

    task_3 = BashOperator(
        task_id='third_task',
        bash_command="echo 'Hi, I am third_task and I will be running after first_task and at the same time as second_task! :O'"
    )

    task_1 >> [task_2, task_3]

