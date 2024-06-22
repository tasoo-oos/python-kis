from typing import TYPE_CHECKING

from pykis.api.stock.info import MARKET_INFO_TYPES, KisStockInfo
from pykis.api.stock.info import info as _info
from pykis.client.account import KisAccountNumber
from pykis.scope.stock.stock import KisStock

if TYPE_CHECKING:
    from pykis.kis import PyKis


__all__ = [
    "KisInfoStock",
    "info_stock",
]


class KisInfoStock(KisStock):
    """한국투자증권 주식 정보 Scope"""

    _info: KisStockInfo
    """주식 정보"""

    def __init__(self, kis: "PyKis", info: KisStockInfo, account: KisAccountNumber):
        super().__init__(
            kis=kis,
            symbol=info.symbol,
            market=info.market,
            account=account,
        )
        self._info = info

    @property
    def info(self) -> KisStockInfo:
        """종목정보 조회"""
        return self._info

    @property
    def stock(self) -> "KisInfoStock":
        """종목 Scope"""
        return self


def info_stock(
    self: "PyKis",
    symbol: str,
    market: MARKET_INFO_TYPES = None,
    account: KisAccountNumber | None = None,
) -> KisStock:
    """
    종목을 조회하고 종목 Scope를 반환합니다.

    Args:
        symbol (str): 종목코드
        market (str): 상품유형명
        account (KisAccountNumber): 계좌번호
    """

    return KisInfoStock(
        kis=self,
        info=_info(
            self,
            symbol=symbol,
            market=market,
        ),
        account=account or self.primary,
    )
