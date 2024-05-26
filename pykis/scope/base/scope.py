from typing import TYPE_CHECKING, Protocol, TypeVar, runtime_checkable

from pykis.client.object import KisObjectBase, KisObjectProtocol

if TYPE_CHECKING:
    from pykis.kis import PyKis


@runtime_checkable
class KisScopeProtocol(KisObjectProtocol, Protocol):
    """한국투자증권 API Scope"""


class KisScope(KisObjectBase):
    """한국투자증권 API Scope"""

    def __init__(self, kis: "PyKis"):
        self.kis = kis


TScope = TypeVar("TScope", bound=KisScope)
