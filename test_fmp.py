#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

import fmp
from fmp import main
import pytest


def test_default_process_constant():
    assert fmp.PROCESSES == 0


def test_missing_args(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main([])

    out, err = capsys.readouterr()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_missing_file_name_badpath(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main([".ufo"])

    out, err = capsys.readouterr()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_not_ufo_path_badpath(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(["bogus.dir"])

    out, err = capsys.readouterr()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_not_existing_ufopath_badpath(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(["bogus.ufo"])

    out, err = capsys.readouterr()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_single_font_build(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(["tests/Hack-Regular.ufo"])

    out, err = capsys.readouterr()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
    assert os.path.exists("master_ttf") and os.path.isdir("master_ttf")
    assert os.path.exists("master_otf") and os.path.isdir("master_otf")
    assert os.path.exists("master_ttf/Hack-Regular.ttf")
    assert os.path.exists("master_otf/Hack-Regular.otf")

    if os.path.exists("master_ttf"):
        shutil.rmtree("master_ttf")

    if os.path.exists("master_otf"):
        shutil.rmtree("master_otf")


def test_multiple_font_build(capsys):
    ufo_paths = [
        "tests/Hack-Regular.ufo",
        "tests/Hack-Italic.ufo",
        "tests/Hack-Bold.ufo",
        "tests/Hack-BoldItalic.ufo",
    ]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(ufo_paths)

    out, err = capsys.readouterr()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
    assert os.path.exists("master_ttf") and os.path.isdir("master_ttf")
    assert os.path.exists("master_otf") and os.path.isdir("master_otf")
    assert os.path.exists("master_ttf/Hack-Regular.ttf")
    assert os.path.exists("master_otf/Hack-Regular.otf")
    assert os.path.exists("master_ttf/Hack-Italic.ttf")
    assert os.path.exists("master_otf/Hack-Italic.otf")
    assert os.path.exists("master_ttf/Hack-Bold.ttf")
    assert os.path.exists("master_otf/Hack-Bold.otf")
    assert os.path.exists("master_ttf/Hack-BoldItalic.ttf")
    assert os.path.exists("master_otf/Hack-BoldItalic.otf")

    if os.path.exists("master_ttf"):
        shutil.rmtree("master_ttf")

    if os.path.exists("master_otf"):
        shutil.rmtree("master_otf")
