from application.celery import app
from application import CustomTask


@app.task(name='test_1', base=CustomTask)
def test_1():
    print("hello from test 1")


@app.task(name='test_2', base=CustomTask)
def test_2():
    print("hello from test 2")


@app.task(name='test_3', base=CustomTask)
def test_3():
    print("hello from test 3")
