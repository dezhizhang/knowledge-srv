import argparse
import uvicorn

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a web server")

    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="host bind the server to (default: localhost)"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="port bind the server to (default: 8080)"
    )

    uvicorn.run("server:app", host="0.0.0.0", port=8000,reload=True)

