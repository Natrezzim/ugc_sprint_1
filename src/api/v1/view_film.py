from uuid import UUID

from confluent_kafka import KafkaException
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPBasicCredentials
from pydantic import BaseModel

from db.kafka_producer import get_producer
from service.auth import Auth
from utils.producer import AIOProducer

security = HTTPBearer()
auth_handler = Auth()

router = APIRouter()


class Viewed(BaseModel):
    movie_id: UUID
    viewed_time: int


@router.post('/',
            summary='Добавление данных по фильму',
            description='Добавление статистики, просмотра фильма',
            response_description='Id, название, рейтинг, описание, жары, '
                                 'актеры, сценаристы, режиссеры фильма.',
            tags=['viewed']
             )
async def film_views(
        viewed: Viewed,
        producer: AIOProducer = Depends(get_producer),
        credentials: HTTPBasicCredentials = Depends(security)
):
    token = credentials.credentials
    user_id = auth_handler.decode_token(token)
    try:
        await producer.produce(
            "views",
            key='{}+{}'.format(viewed.movie_id, user_id).encode(),
            value='{}'.format(viewed.viewed_time).encode()
        )
        return {"saved": 'ok'}

    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())