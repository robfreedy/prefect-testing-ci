from prefect import flow
import pytest
from prefect.testing.utilities import prefect_test_harness
from prefect.artifacts import create_table_artifact, Artifact

@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    with prefect_test_harness():
        yield

@flow
def my_favorite_flow():
    highest_churn_possibility = [
       {'customer_id':'12345', 'name': 'John Smith', 'churn_probability': 0.85 }, 
       {'customer_id':'56789', 'name': 'Jane Jones', 'churn_probability': 0.65 } 
    ]

    create_table_artifact(
        key="test-artifact-in-ci",
        table=highest_churn_possibility,
        description= "# Marvin, please reach out to these customers today!"
    )

def test_my_favorite_flow():
    my_favorite_flow()
    assert Artifact.get("test-artifact-in-ci") is not None