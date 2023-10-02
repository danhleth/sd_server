from fastapi import FastAPI
from pathlib import Path
from modules.api import API
import uvicorn

app = FastAPI()
api = API(app)

def run_server():
    """Run server."""
    cwd = Path(__file__).parent.resolve()

    # start the server!
    uvicorn.run(
        "app:app",
        # host='0.0.0.0',
        port=7861,
        # log_config=f"{cwd}/log.ini",
        # workers=4,
        reload=True
    )


if __name__ == "__main__":
    run_server()