"""A renderer base class."""
from __future__ import annotations

from abc import abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass
from types import TracebackType
from typing import ContextManager, Iterator, Optional, Text, Type

from ..message import Message


@dataclass
class Renderer(ContextManager["Renderer"]):
    """Renderer base class."""

    def __enter__(self) -> Renderer:
        """Enter context."""
        raise NotImplementedError()

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> Optional[bool]:
        """Exit context."""
        raise NotImplementedError("You must implement this method")

    @abstractmethod
    @contextmanager
    def into_raw_mode(self) -> Iterator[Renderer]:
        """Enter raw mode."""
        raise NotImplementedError("You must implement this method")

    @abstractmethod
    def render(self, screen: Text) -> None:
        """Render a screen."""
        raise NotImplementedError("You must implement this method")

    @abstractmethod
    def next_message(self) -> Optional[Message]:
        """Get next message."""
        raise NotImplementedError("You must implement this method")
