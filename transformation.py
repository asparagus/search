#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Contains the base class for transformating one problem to another."""


class Transformation:
    """Base class for a transformation."""

    def apply(self, problem):
        """Applythe transformation on a problem."""
        raise NotImplementedError()

    def revert(self, problem):
        """Revert the transformation on the problem's output."""
        raise NotImplementedError()
