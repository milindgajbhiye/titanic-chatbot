"""
Titanic Chatbot Agent Module

This module provides a query processing system for the Titanic dataset.
It analyzes natural language questions about Titanic passenger statistics
and returns relevant data-driven responses.
"""

import pandas as pd
from typing import Optional

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")


def process_query(question: str) -> str:

    if not question or not isinstance(question, str):
        return "Please provide a valid question."

    question = question.lower()

    # --- Male Passenger Percentage ---
    if ("male" in question or "men" in question) and (
        "percentage" in question or "percent" in question or "how many" in question
    ):
        total = len(df)
        male_count = (df["sex"] == "male").sum()
        percentage = (male_count / total) * 100

        return (
            f"{percentage:.2f}% of passengers were male.\n"
            f"That is {male_count} out of {total} total passengers."
        )

    # --- Average Fare ---
    if "average" in question and "fare" in question:
        avg_fare = df["fare"].mean()
        return f"The average ticket fare was ${avg_fare:.2f}."

    # --- Embarkation Ports ---
    if "embark" in question or "port" in question:
        counts = df["embarked"].value_counts()
        ports = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}

        response = "Passengers embarked from:\n"
        for port, count in counts.items():
            port_name = ports.get(port, port)
            response += f"- {port_name}: {count} passengers\n"

        return response

    # --- Age Histogram Trigger ---
    if "histogram" in question and "age" in question:
        return "VISUALIZE_AGE_HISTOGRAM"

    return (
        "I couldn't understand that question.\n"
        "Try asking about:\n"
        "- Male passenger percentage\n"
        "- Average ticket fare\n"
        "- Embarkation ports\n"
        "- Age histogram"
    )