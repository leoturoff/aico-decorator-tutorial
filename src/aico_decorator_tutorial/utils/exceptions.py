class ControlledExit(BaseException):
    """Base exception to exit the function early"""


class TookTooLong(ControlledExit):
    """Exception to exit the function because it took too long"""


class BelowThreshold(ControlledExit):
    """Exception to exit the function because the value is below the threshold"""


class SillyName(ControlledExit):
    """Exception to exit the function because the name is silly"""
