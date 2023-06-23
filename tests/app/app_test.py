import pytest
from src.app.app import App


def test_load_ini_file():
    app = App()
    assert app._App__load_ini_file("app.ini")
    assert app.config is not None


def test_load_files():
    app = App()
    assert app._App__load_files()
    assert len(app.files) > 0


def test_run(capsys):
    app = App()
    app._App__run()
    captured = capsys.readouterr()
    assert "Textual Clustering Analysis" in captured.out


if __name__ == "__main__":
    pytest.main([__file__])
