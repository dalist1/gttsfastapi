# Nativify TTS API

Nativify TTS API is a FastAPI application that provides a simple interface for text-to-speech conversion using the Google Text-to-Speech (gTTS) library. The API supports multiple languages and offers a convenient way to get the list of supported languages.

## Endpoints

### 1. Root

- **Path**: `/`
- **Method**: `GET`
- **Description**: Returns a plain text response containing a brief description of the project and a link to the Nativify project page.

### 2. Text-to-Speech

- **Path**: `/tts/{lang}`
- **Method**: `GET`
- **Parameters**:
  - `text`: The text to be converted to speech.
  - `lang`: The language code for the text (e.g., `en`, `fr`, `es`). Check the [supported languages]<a href="https://cloud.google.com/translate/docs/languages" target="_blank">example</a> for more information.
- **Description**: Converts the input text to speech in the specified language and returns an MP3 audio file.

### 3. Supported Languages

- **Path**: `/langs` or `/v1/langs`
- **Method**: `GET`
- **Description**: Returns a JSON object containing the list of supported languages and their corresponding language codes.

## Error Handling

The API handles errors raised by the gTTS library and returns a JSON response with the appropriate status code and error details.

## Example Usage

1. Get the list of supported languages:

```
GET https://gttsfastapi.vercel.app/langs
```

2. Convert text to speech in English:

```
GET https://gttsfastapi.vercel.app/tts/en?text=Hello%20world
```

3. Convert text to speech in French:

```
GET https://gttsfastapi.vercel.app/tts/fr?text=Bonjour%20le%20monde
```

## Dependencies

- **fastapi**: Web framework used to create the API.
- **gTTS**: Google Text-to-Speech library responsible for the text-to-speech conversion.
- **gtts.lang**: Module to retrieve the list of supported languages.

## References

1. [FastAPI Documentation](https://fastapi.tiangolo.com/)
2. [gTTS GitHub Repository](https://github.com/pndurette/gTTS)
3. [gTTS Documentation](https://gtts.readthedocs.io/)
