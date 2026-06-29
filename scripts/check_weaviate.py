import os

import weaviate
from weaviate.connect import ConnectionParams


def main() -> None:
    http_host = os.getenv("WEAVIATE_HTTP_HOST", "localhost")
    http_port = int(os.getenv("WEAVIATE_HTTP_PORT", "8080"))
    grpc_host = os.getenv("WEAVIATE_GRPC_HOST", http_host)
    grpc_port = int(os.getenv("WEAVIATE_GRPC_PORT", "50051"))

    client = weaviate.WeaviateClient(
        connection_params=ConnectionParams.from_params(
            http_host=http_host,
            http_port=http_port,
            http_secure=False,
            grpc_host=grpc_host,
            grpc_port=grpc_port,
            grpc_secure=False,
        )
    )

    try:
        client.connect()
        print(f"Weaviate is ready: {client.is_ready()}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
