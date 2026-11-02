"""Tests for the Support Ticket Summary project."""

from app import (
    build_summary,
    count_priority,
    count_status,
    load_config,
    load_tickets,
)


def test_count_status_counts_matching_status():
    tickets = [
        {"id": "T-101", "status": "open", "priority": "high"},
        {"id": "T-102", "status": "closed", "priority": "low"},
        {"id": "T-103", "status": "open", "priority": "medium"},
    ]

    assert count_status(tickets, "open") == 2


def test_count_status_is_case_insensitive():
    tickets = [
        {"id": "T-101", "status": "Open", "priority": "high"},
        {"id": "T-102", "status": "OPEN", "priority": "low"},
    ]

    assert count_status(tickets, "open") == 2


def test_count_priority_counts_matching_priority():
    tickets = [
        {"id": "T-101", "status": "open", "priority": "high"},
        {"id": "T-102", "status": "closed", "priority": "low"},
        {"id": "T-103", "status": "open", "priority": "high"},
    ]

    assert count_priority(tickets, "high") == 2


def test_build_summary_reports_totals():
    tickets = [
        {"id": "T-101", "status": "open", "priority": "high"},
        {"id": "T-102", "status": "closed", "priority": "low"},
        {"id": "T-103", "status": "open", "priority": "medium"},
    ]

    assert build_summary(tickets, "open", "high") == {
        "total": 3,
        "open": 2,
        "high_priority": 1,
    }


def test_load_config_reads_json(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        """{
  "report_title": "Support Report",
  "data_file": "tickets.csv",
  "open_status": "open",
  "high_priority": "high"
}""",
        encoding="utf-8",
    )

    result = load_config(config_file)

    assert result == {
        "report_title": "Support Report",
        "data_file": "tickets.csv",
        "open_status": "open",
        "high_priority": "high",
    }


def test_load_tickets_reads_csv(tmp_path):
    data_file = tmp_path / "tickets.csv"
    data_file.write_text(
        "id,status,priority\nT-201,open,high\nT-202,closed,low\n",
        encoding="utf-8",
    )

    result = load_tickets(data_file)

    assert result == [
        {"id": "T-201", "status": "open", "priority": "high"},
        {"id": "T-202", "status": "closed", "priority": "low"},
    ]
