from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # MongoDB configs
    MONGO_DATABASE_HOST: str = "mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set"
    MONGO_DATABASE_NAME: str = "admin"

    RABBITMQ_HOST: str = "localhost"  # or the Docker host if running remotely
    RABBITMQ_PORT: int = 5673  # Port mapped in Docker Compose
    RABBITMQ_DEFAULT_USERNAME: str = "guest"  # Default username
    RABBITMQ_DEFAULT_PASSWORD: str = "guest"  # Default password


settings = AppSettings()
