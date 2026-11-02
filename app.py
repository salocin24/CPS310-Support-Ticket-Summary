"""CPS 310 Support Ticket Summary starter project."""

import csv
import json


def load_config(filename):
    """Load application configuration from JSON."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_tickets(filename):
    """Load support tickets from a CSV file."""
    tickets = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tickets.append(
                {
                    "id": row["id"],
                    "status": row["status"],
                    "priority": row["priority"],
                }
            )

    return tickets


def count_status(tickets, status):
    """Count tickets that match the requested status."""
    return sum(
        1
        for ticket in tickets
        if ticket["status"].lower() == status.lower()
    )


def count_priority(tickets, priority):
    """Count tickets that match the requested priority."""
    return sum(
        1
        for ticket in tickets
        if ticket["priority"].lower() == priority.lower()
    )


def build_summary(tickets, open_status, high_priority):
    """Build summary information for the ticket list."""
    return {
        "total": len(tickets),
        "open": count_status(tickets, open_status),
        "high_priority": count_priority(tickets, high_priority),
    }


def main():
    """Run the support ticket summary."""
    config = load_config("config.json")
    tickets = load_tickets(config["data_file"])
    summary = build_summary(
        tickets,
        config["open_status"],
        config["high_priority"],
    )

    print(config["report_title"])
    print("-" * len(config["report_title"]))
    print(f"Total tickets: {summary['total']}")
    print(f"Open tickets: {summary['open']}")
    print(f"High-priority tickets: {summary['high_priority']}")


if __name__ == "__main__":
    main()
