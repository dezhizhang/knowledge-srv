import argparse
import sys

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

    args = parser.parse_args()

    try:
        uvicorn.run(
            "src.main:app",
            host=args.host,
            port=args.port,
            reload=True
        )

    except Exception as e:
        print(e)
        sys.exit(1)
