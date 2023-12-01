"""Dimension class.

make test T=test_dimension_class.py
"""
import pytest
from . import TestBase


class TestDimensionClass(TestBase):
    """Feature dimension class."""

    @staticmethod
    def test_gene():
        """Check function size_class."""
        from pipeline_anomaly_dimension_class import FeatureClass, size_class, Error

        assert size_class(100, 100, 10) == FeatureClass.GENE
        assert size_class(10, 10, 10) == FeatureClass.PITT
        assert size_class(5, 5, 10) == FeatureClass.PINH
        assert size_class(5, 100, 10) == FeatureClass.CISL
        assert size_class(100, 5, 10) == FeatureClass.AXSL
        assert size_class(50, 10, 10) == FeatureClass.AXGR
        assert size_class(10, 50, 10) == FeatureClass.CIGR

        with pytest.raises(Error) as exc:
            size_class(0, 10, 10)
        assert 'Wrong FeatureClass params' in str(exc)

        with pytest.raises(Error) as exc:
            size_class(-1, 10, 10)
        assert 'Wrong FeatureClass params' in str(exc)
