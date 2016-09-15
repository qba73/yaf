#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_parser
----------------------------------

Tests for html parsers in the `yaf` module.
"""

import pytest
from bs4 import BeautifulSoup as BS
from yaf import yaf


@pytest.fixture
def soup():
    with open(fl, 'r') as f:
       sup = BS(f, 'lxml')
    return sup


   
