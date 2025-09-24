import os
import uuid
import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE

def setup_module():
    print()
    print("Roda antes dos testes desse modulo \n")

def teardown_module():
    print()
    print("Roda apos os testes desse modulo \n")

@pytest.fixture(scope="function")
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso é sujeira...")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function"""
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))

    with open (filepath,"w") as file_:
        file_.write("DAdos uteis somente para o teste")
    assert len(load(PEOPLE_FILE))==2
 