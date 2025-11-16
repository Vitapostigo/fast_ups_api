from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import subprocess
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ups")
def home():
    return FileResponse("static/index.html")


@app.get("/ups/raw")
def get_ups():
    try:
        result = subprocess.run(
            ["upsc", "salicru@host.docker.internal:3493"],
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
    uvicorn.run("cod:app", host="0.0.0.0", port=18000)


if __name__ == "__main__":
	main()
