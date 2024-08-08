from app import create_app  # cannot import name 'create_app' from 'app'
import logging

app = create_app()  # Error


def setup_logging(log_file='app.log', level=logging.INFO):  # TODO
    """Настраивает логирование."""
    logging.basicConfig(
        filename=log_file,
        filemode='a',  # Запись в конец файла
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=level
    )


"""Пример записи логов.
    logging.debug("Это отладочное сообщение.")
    logging.info("Это информационное сообщение.")
    logging.warning("Это предупреждение.")
    logging.error("Это сообщение об ошибке.")
    logging.critical("Это критическое сообщение.")
"""
if __name__ == '__main__':
    app.run(debug=True)
    setup_logging()
