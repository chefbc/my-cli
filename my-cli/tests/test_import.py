"""Test my-cli."""

import my_cli


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(my_cli.__name__, str)
