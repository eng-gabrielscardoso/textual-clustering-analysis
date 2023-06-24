from src.app.app import App


def main() -> None:
    try:
        App()
    except Exception as e:
        print(f'Failed to load app: {e}')


if __name__ == "__main__":
    main()
