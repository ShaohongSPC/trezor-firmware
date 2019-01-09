# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .MoneroTransactionDestinationEntry import MoneroTransactionDestinationEntry
from .MoneroTransactionRsigData import MoneroTransactionRsigData


class MoneroTransactionSetOutputRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 511

    def __init__(
        self,
        dst_entr: MoneroTransactionDestinationEntry = None,
        dst_entr_hmac: bytes = None,
        rsig_data: MoneroTransactionRsigData = None,
    ) -> None:
        self.dst_entr = dst_entr
        self.dst_entr_hmac = dst_entr_hmac
        self.rsig_data = rsig_data

    @classmethod
    def get_fields(cls):
        return {
            1: ('dst_entr', MoneroTransactionDestinationEntry, 0),
            2: ('dst_entr_hmac', p.BytesType, 0),
            3: ('rsig_data', MoneroTransactionRsigData, 0),
        }