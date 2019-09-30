import os
import re

import pytest
import sh
from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        "project_name": "my_click_project",
        "package_name": "click_project",
        "cli_name": "click_project",
        "project_version": "0.0.1",
        "project_description": "A click command-line app.",
        "python_version": "3.6",
        "sphinx_theme": "alabaster",
        "author_name": "my_name",
        "author_email": "my_email@gmail.com",
        "license": "MIT",
        "github_user": "my_github_username",
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "rb"):
            match = RE_OBJ.search(str(line))
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)


def test_project_generation(cookies, context):
    """
    Test that project is generated and fully rendered.
    """
    result = cookies.bake(context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_name"]
    assert result.project.isdir()
    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


@pytest.mark.black
def test_black_passes(cookies):
    """
    Generated project should pass black.
    """
    result = cookies.bake()

    try:
        sh.black(
            "--verbose",
            "--check",
            "--diff",
            "--exclude",
            "venv|docs/source/conf.py|setup.py",
            str(result.project),
        )
    except sh.ErrorReturnCode as e:
        pytest.fail(e)


@pytest.mark.flake8
def test_flake8_passes(cookies, context):
    """
    Generated project should pass flake8.
    """
    result = cookies.bake()

    try:
        sh.flake8("--config=.flake8", str(result.project))
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
