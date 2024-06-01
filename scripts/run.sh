set -e
cd "$(dirname "$0")/.."

TAG_NAME=fastapi-sandbox
docker build -t ${TAG_NAME} .
docker run --publish 3100:3100 ${TAG_NAME}
