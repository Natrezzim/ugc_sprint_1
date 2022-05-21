from typing import Optional

from utils.producer import AIOProducer

aio_producer: Optional[AIOProducer] = None


async def get_producer():
    return aio_producer
