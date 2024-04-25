from typing import TYPE_CHECKING

from pykis.responses.dynamic import KisDynamic
from pykis.responses.types import KisString

if TYPE_CHECKING:
    from pykis.kis import PyKis


class KisWebsocketApprovalKey(KisDynamic):
    """한국투자증권 웹소켓 접속 키"""

    approval_key: str = KisString["approval_key"]
    """접속 키"""


def websocket_approval_key(self: "PyKis"):
    """
    웹소켓 접속 키를 발급합니다.

    OAuth인증 -> 실시간 (웹소켓) 접속키 발급[실시간-000]
    (업데이트 날짜: 2024/04/04)
    """
    return self.fetch(
        "/oauth2/Approval",
        body={
            "grant_type": "client_credentials",
            "appkey": self.appkey.appkey,
            "secretkey": self.appkey.secretkey,
        },
        response_type=KisWebsocketApprovalKey,
        method="POST",
        auth=False,
        appkey_location=None,
        verbose=False,
    )
