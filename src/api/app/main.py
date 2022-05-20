import os

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(

    title=os.getenv('PROJECT_NAME'),

    docs_url='/api/openapi',

    openapi_url='/api/openapi.json',

    default_response_class=ORJSONResponse,
)


if __name__ == '__main__':

    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8010,
    )
