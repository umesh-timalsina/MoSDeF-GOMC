#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Compound.visualize()`. """
import pytest
from base_test import BaseTest


class TestVisualize(BaseTest):

    @pytest.fixture
    def ethane(self):
        from mbuild.examples.ethane.ethane import Ethane
        return Ethane()

    def test_visualize1(self, ethane):
        ethane.visualize()

    def test_visualize2(self, ethane):
        ethane.visualize(show_ports=True)
