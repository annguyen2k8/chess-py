from typing import *
from os import PathLike
from pygame.color import Color

from .Maths import Vector2

AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
FileArg = Union[AnyPath, IO[bytes], IO[str]]

Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]

RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]