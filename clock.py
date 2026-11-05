"""Выводит текущее время в терминале. Остановка: Ctrl+C."""
import sys
import time
from datetime import datetime


def main() -> None:
    once = "--once" in sys.argv
    try:
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            if once:
                print(now)
                return
            print(f"\rТекущее время: {now}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nВыход.")


if __name__ == "__main__":
    main()
