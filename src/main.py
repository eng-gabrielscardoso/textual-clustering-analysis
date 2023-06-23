import logging
from app import App


def main():
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='logs/app.log',
        filemode='w',
    )

    try:
        app = App()
    except Exception as e:
        logging.error(f'Something went wrong: {e}', exc_info=True)


if __name__ == "__main__":
    main()
