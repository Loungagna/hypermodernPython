# (generated with --quick)

import click.testing
from typing import Any, Type

CliRunner: Type[click.testing.CliRunner]
Mock: Any
MockFixture: Any
click: module
console: module
mock_requests_get: Any
mock_wikipedia_random_page: Any
pytest: Any
requests: module
runner: Any
test_main_succeeds_in_production_env: Any

def test_main_fails_on_request_error(runner: click.testing.CliRunner, mock_requests_get) -> None: ...
def test_main_invokes_requests_get(runner: click.testing.CliRunner, mock_requests_get) -> None: ...
def test_main_prints_message_on_request_error(runner: click.testing.CliRunner, mock_requests_get) -> None: ...
def test_main_prints_title(runner: click.testing.CliRunner, mock_requests_get) -> None: ...
def test_main_succeeds(runner: click.testing.CliRunner, mock_requests_get) -> None: ...
def test_main_uses_specified_language(runner: click.testing.CliRunner, mock_wikipedia_random_page) -> None: ...
