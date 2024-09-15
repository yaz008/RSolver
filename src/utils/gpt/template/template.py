from dataclasses import dataclass, field
from re import findall

@dataclass(slots=True)
class Template:
    string: str
    _vars: dict[str, str] = field(init=False)

    def __post_init__(self) -> None:
        pattern: str = r'(?<!\\){%[ \n]*[_a-zA-Z][_a-zA-Z0-9]*[ \n]*[^\\]%}'
        matches: list[str] = findall(pattern=pattern, string=self.string)
        self._vars = { var[2:-2].strip(): var for var in matches }

    def render(self, subs: dict[str, str]) -> None:
        result: str = self.string
        for name, sub in subs.items():
            result = result.replace(self._vars[name], sub)
        return result