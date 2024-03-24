import re
import sys
from typing import Callable, Generator, List, Dict

def parse_log_line(line: str) -> dict:
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)"
    match = re.match(pattern, line)
    if match:
        return {"datetime": match.group(1), "level": match.group(2), "message": match.group(3)}
    return {}

def load_logs(file_path: str) -> List[dict]:
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            log_entry = parse_log_line(line.strip())
            if log_entry:
                logs.append(log_entry)
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return [log for log in logs if log["level"].upper() == level.upper()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main(log_file_path: str, log_level: str = None):
    logs = load_logs(log_file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['datetime']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python script.py path/to/logfile.log [log_level]")
    else:
        log_file_path = sys.argv[1]
        log_level = sys.argv[2] if len(sys.argv) > 2 else None
        main(log_file_path, log_level)
