from _typeshed import Incomplete
from collections.abc import Generator

def is_eulerian(G): ...
def is_semieulerian(G): ...
def eulerian_circuit(G, source: Incomplete | None = None, keys: bool = False) -> Generator[Incomplete, Incomplete, None]: ...
def has_eulerian_path(G, source: Incomplete | None = None): ...
def eulerian_path(G, source: Incomplete | None = None, keys: bool = False) -> Generator[Incomplete, Incomplete, None]: ...
def eulerize(G): ...