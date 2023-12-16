from functools import wraps
from io import BytesIO

from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import Response, StreamingResponse, JSONResponse
from gtts import gTTS, gTTSError
from gtts.lang import tts_langs

app = FastAPI()
tts_langs = tts_langs()

@app.get("/")
async def root():
    content = "Created as part of the Nativify project - https://nativify.vercel.app/"
    return Response(content=content, media_type="text/plain")

@app.get("/tts/{lang}")
def tts(text: str, lang: str = Path(..., description="Language code"), tld='us', slow=False):
    if lang not in tts_langs:
        raise HTTPException(
            detail=f"{lang} is not a valid language code.",
            status_code=400
        )

    mp3 = BytesIO()
    gTTS(text=text, lang=lang).write_to_fp(mp3)
    mp3.seek(0)

    return StreamingResponse(mp3, media_type="audio/mp3")

@app.exception_handler(gTTSError)
async def gtts_exception_handler(request: Request, exc: gTTSError):
    if exc.rsp is not None:
        headers = exc.rsp.headers
        headers.pop("Content-Length", None)

        return JSONResponse(
            status_code=exc.rsp.status_code,
            content={"detail": exc.rsp.content.decode()},
            headers=headers
        )

    raise

@app.get("/langs")
@app.get("/v1/langs")
async def get_langs():
    return tts_langs

# CORS

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
