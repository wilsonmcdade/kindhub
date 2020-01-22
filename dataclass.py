from dataclasses import dataclass
from typing import Union

@dataclass
class Widget:
    name: str
    route: str
    strname: str
    config: str
    next: Union['Widget',None]
