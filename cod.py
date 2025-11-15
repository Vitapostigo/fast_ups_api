from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import subprocess
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/ups")
def get_ups():
    try:
        result = subprocess.run(
            ["upsc", "salicru@127.0.0.1:3493"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return JSONResponse(
                {"error": "No se pudo obtener información del SAI", "detail": result.stderr},
                status_code=500
            )

        lines = result.stdout.strip().split("\n")
        data = {}

        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()

        return data

    except Exception as e:
        return JSONResponse(
            {"error": "Fallo inesperado", "detail": str(e)},
            status_code=500
        )


def main():
    uvicorn.run("cod:app", host="127.0.0.1", port=18000)


if __name__ == "__main__":
	main()
