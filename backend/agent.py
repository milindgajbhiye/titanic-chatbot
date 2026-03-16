"""
Titanic Chatbot Agent Module

This module provides a query processing system for the Titanic dataset.
It analyzes natural language questions about Titanic passenger statistics
and returns relevant data-driven responses.
"""

import os
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "titanic.csv"))


def process_query(question: str) -> str:

    if not question or not isinstance(question, str):
        return "Please provide a valid question."

    question = question.lower()

    # --- Total Passengers ---
    if "total passenger" in question or (
        "how many passenger" in question
        and "surviv" not in question
        and "class" not in question
        and "female" not in question
        and "women" not in question
        and "child" not in question
        and "male" not in question
    ):
        total = len(df)
        return f"There were {total} passengers in the Titanic dataset."

    # --- Survival Statistics ---
    if "surviv" in question:
        survived = df["survived"].sum()
        total = len(df)
        rate = (survived / total) * 100
        not_survived = total - survived
        return (
            f"Out of {total} passengers:\n"
            f"- Survived: {survived} ({rate:.1f}%)\n"
            f"- Did not survive: {not_survived} ({100 - rate:.1f}%)"
        )

    # --- Male Passenger Percentage ---
    if ("male" in question or "men" in question) and (
        "percentage" in question or "percent" in question or "how many" in question or "number" in question
    ) and "female" not in question and "women" not in question and "woman" not in question:
        total = len(df)
        male_count = (df["sex"] == "male").sum()
        percentage = (male_count / total) * 100

        return (
            f"{percentage:.2f}% of passengers were male.\n"
            f"That is {male_count} out of {total} total passengers."
        )

    # --- Female Passenger Percentage ---
    if "female" in question or "women" in question or "woman" in question:
        total = len(df)
        female_count = (df["sex"] == "female").sum()
        percentage = (female_count / total) * 100

        return (
            f"{percentage:.2f}% of passengers were female.\n"
            f"That is {female_count} out of {total} total passengers."
        )

    # --- Average Fare ---
    if "average" in question and "fare" in question:
        avg_fare = df["fare"].mean()
        return f"The average ticket fare was ${avg_fare:.2f}."

    # --- Fare range / min / max ---
    if "fare" in question and ("highest" in question or "maximum" in question or "max" in question):
        max_fare = df["fare"].max()
        return f"The highest ticket fare paid was ${max_fare:.2f}."

    if "fare" in question and ("lowest" in question or "minimum" in question or "min" in question or "cheapest" in question):
        min_fare = df["fare"].min()
        return f"The lowest ticket fare paid was ${min_fare:.2f}."

    # --- Passenger Class Distribution ---
    if "class" in question:
        counts = df["pclass"].value_counts().sort_index()
        class_names = {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}
        total = len(df)

        response = "Passenger class distribution:\n"
        for pclass, count in counts.items():
            name = class_names.get(pclass, f"Class {pclass}")
            pct = (count / total) * 100
            response += f"- {name}: {count} passengers ({pct:.1f}%)\n"

        return response

    # --- Children ---
    if "child" in question or "children" in question or "kid" in question:
        children = (df["age"] < 18).sum()
        total = len(df)
        pct = (children / total) * 100
        return (
            f"There were approximately {children} passengers under 18 years old ({pct:.1f}%).\n"
            f"(Note: some age values in the dataset are missing.)"
        )

    # --- Average Age ---
    if "average" in question and "age" in question:
        avg_age = df["age"].mean()
        return f"The average age of passengers was {avg_age:.1f} years."

    # --- Oldest / Youngest ---
    if ("oldest" in question or "maximum age" in question or "max age" in question):
        oldest = df["age"].max()
        return f"The oldest passenger was {oldest:.0f} years old."

    if ("youngest" in question or "minimum age" in question or "min age" in question):
        youngest = df["age"].min()
        return f"The youngest passenger was {youngest:.1f} years old."

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
        "- Total passengers\n"
        "- Survival rate or number of survivors\n"
        "- Male or female passenger percentage\n"
        "- Average ticket fare\n"
        "- Passenger class distribution\n"
        "- Children on board\n"
        "- Average age of passengers\n"
        "- Embarkation ports\n"
        "- Age histogram"
    )