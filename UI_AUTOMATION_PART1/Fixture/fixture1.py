import  pytest

@pytest.fixture
def sample_data():
    return {"name": "Srishti", "role": "QA"}

def data(sample_data):
    print(sample_data["name"])
    assert sample_data["name"] == "Srishti"

@pytest.mark.usefixtures("sample_data")
def test_example():
    print("Fixture will run before this test")
