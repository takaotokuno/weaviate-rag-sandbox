# Weaviate RAG Sandbox

Docker Compose と Dev Container で、ローカル開発用の Weaviate ベクトル DB と Python クライアント環境を起動できます。

## 構成

- `weaviate`: Weaviate Database `1.38.1`
  - HTTP: `localhost:8080`
  - gRPC: `localhost:50051`
  - データ永続化: Docker volume `weaviate_data`
  - ローカル開発向けに匿名アクセスを有効化
  - ベクトル化モジュールは無効化し、Python 側で生成したベクトルを投入する想定
- `app`: Python 3.12 Dev Container
  - `weaviate-client` v4 系をインストール

## 起動方法

```bash
docker compose up -d weaviate
```

Dev Container を使う場合は、VS Code / Cursor などで「Reopen in Container」を実行してください。`app` コンテナと `weaviate` コンテナが同じ Compose ネットワークで起動します。

## 接続確認

ホスト側から確認する場合:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_weaviate.py
```

Dev Container 内から確認する場合:

```bash
python scripts/check_weaviate.py
```

Dev Container 内では `WEAVIATE_HTTP_HOST=weaviate` と `WEAVIATE_GRPC_HOST=weaviate` が設定済みです。ホスト側から実行する場合は、デフォルトで `localhost` に接続します。

## 停止・削除

```bash
docker compose down
```

永続化データも削除する場合:

```bash
docker compose down -v
```
