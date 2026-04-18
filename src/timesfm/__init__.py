"""TimesFM: A time series forecasting model from Google Research.

This package provides a PyTorch-based implementation of TimesFM,
a foundation model for time series forecasting.
"""

from timesfm.timesfm_base import TimesFm, TimesFmHparams, TimesFmCheckpoint

__version__ = "0.1.0"
__all__ = ["TimesFm", "TimesFmHparams", "TimesFmCheckpoint"]
