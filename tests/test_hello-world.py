import py
from typing import Generator

from flask import Flask
import pytest

from hello_kubernetes.hello_kubernetes import create_app


@pytest.fixture()
def counter_filename(tmpdir: py.path.local) -> Generator[str, None, None]:
    tmpfn = tmpdir.join("testcounter.txt")
    tmpfn.write("5")
    yield str(tmpfn)


@pytest.fixture()
def app(counter_filename: str) -> Generator[Flask, None, None]:
    app = create_app(counter_filename)
    app.config.update({
        "TESTING": True,
    })

    yield app


def test_hello_world_responds(app: Flask):
    client = app.test_client()
    response = client.get("/")

    assert (b"Raspberry Pi" in response.data)
    assert (b"You are visitor 6" in response.data)


def test_hello_world_increments(app: Flask):
    client = app.test_client()

    response = client.get("/")
    assert (b"visitor 6" in response.data)

    response = client.get("/")
    assert (b"visitor 7" in response.data)

    response = client.get("/")
    assert (b"visitor 8" in response.data)
