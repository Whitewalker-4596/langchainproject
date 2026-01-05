from dotenv import load_dotenv

load_dotenv()
import os


def main():
    print("Hello from langchainproject!")
    print("OPEN_API_KEY:", os.getenv("OPEN_API_KEY"))
    print(os.environ.get("OPEN_API_KEY"))


if __name__ == "__main__":
    main()
