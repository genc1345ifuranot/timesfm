"""TimesFM: A time series forecasting model from Google Research.

This package provides a PyTorch-based implementation of TimesFM,
a foundation model for time series forecasting.

Note: Forked from google-research/timesfm for personal learning/experimentation.
See https://github.com/google-research/timesfm for the upstream project.
"""

from timesfm.timesfm_base import TimesFm, TimesFmHparams, TimesFmCheckpoint

__version__ = "0.1.0"
__all__ = ["TimesFm", "TimesFmHparams", "TimesFmCheckpoint"]
