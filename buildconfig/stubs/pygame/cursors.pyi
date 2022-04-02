"""
Set of cursor resources available for use. These cursors come in a sequence 
of values that are needed as the arguments for pygame.mouse.set_cursor(). 
To dereference the sequence in place and create the cursor in one step, 
call like this:
    pygame.mouse.set_cursor(*pygame.cursors.arrow).

Here is a list of available cursors:
    arrow, diamond, ball, broken_x, tri_left, tri_right

There is also a sample string cursor named 'thickarrow_strings'.
The compile() function can convert these string cursors into cursor byte data
that can be used to create Cursor objects.

Alternately, you can also create Cursor objects using surfaces or cursors 
constants, such as pygame.SYSTEM_CURSOR_ARROW.
"""

from typing import Any, Iterator, Sequence, Tuple, Union, overload

from pygame.surface import Surface

from ._common import FileArg, Literal

_Small_string = Tuple[
    str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str
]
_Big_string = Tuple[
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
]

arrow: Cursor
diamond: Cursor
broken_x: Cursor
tri_left: Cursor
tri_right: Cursor
ball: Cursor
thickarrow_strings: _Big_string
sizer_x_strings: _Small_string
sizer_y_strings: _Big_string
sizer_xy_strings: _Small_string
textmarker_strings: _Small_string

def compile(
    strings: Sequence[str],
    black: str = "X",
    white: str = ".",
    xor: str = "o",
) -> Tuple[Tuple[int, ...], Tuple[int, ...]]: ...
def load_xbm(
    curs: FileArg, mask: FileArg
) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, ...], Tuple[int, ...]]: ...

class Cursor:
    @overload
    def __init__(self, constant: int = ...) -> None: ...
    @overload
    def __init__(self, cursor: Cursor) -> None: ...
    @overload
    def __init__(
        self,
        size: Union[Tuple[int, int], Sequence[int]],
        hotspot: Union[Tuple[int, int], Sequence[int]],
        xormasks: Sequence[int],
        andmasks: Sequence[int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        hotspot: Union[Tuple[int, int], Sequence[int]],
        surface: Surface,
    ) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __copy__(self) -> Cursor: ...
    def __hash__(self) -> int: ...
    def __getitem__(
        self, index: int
    ) -> Union[int, Tuple[int, int], Sequence[int], Surface]: ...
    copy = __copy__
    type: Literal["system", "color", "bitmap"]
    data: Union[
        Tuple[int],
        Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, ...], Tuple[int, ...]],
        Tuple[Union[Tuple[int, int], Sequence[int]], Surface],
    ]
