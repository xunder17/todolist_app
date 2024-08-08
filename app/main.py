from fastapi import FastAPI
from .routers import users, tasks
import logging

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)


def setup_logging(log_file='app.log', level=logging.INFO):  # TODO
    """Настраивает логирование."""
    logging.basicConfig(
        filename=log_file,
        filemode='a',  # Запись в конец файла
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=level
    )


setup_logging()
