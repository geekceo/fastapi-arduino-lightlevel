from fastapi import FastAPI
import serialread

@app.get('/arduino/light-level')
def light_level():
    level: int = int(serialread.read())

    level_type = 'dark' if level >= 800 else 'light'

    return {'level': level, 'type': level_type}