import requests
from prefect import flow, task


@flow
def my_favorite_function():
    print("What is your favorite number")
    return 42


@task
def call_api(url):
    response = requests.get(url)
    return requests.get(url).json()


@task
def parse_fact(response):
    fact = response["fact"]
    return fact


@flow
def api_flow(url):
    fact_json = call_api(url)
    fact_text = parse_fact(fact_json)
    return fact_text


@task
def printer(obj):
    print(f"Received a {type(obj)} with value {obj}")

# note that we define the flow with type hints


@flow(name="Validation Flow",
      description="This flow is a way to validate the flow. It will also coerce the argument into the types specificed in the args")
def validation_flow(x: int, y: str):
    """
    This flow is a way to validate the flow. It will also coerce the arguments 
    into the types specificed in the args
    """
    printer(x)  # Received a <class 'int'> with value 42
    printer(y)  # Received a < class 'str' > with value 100


validation_flow(x="42", y=100)
