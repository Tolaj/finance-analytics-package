from typing import Iterable, List, Dict
import numpy as np
import matplotlib.pyplot as plt

# Generates a bar chart visualizing cash inflows and outflows over specific time periods
def plot_cashflows(stream: Iterable[float], chart_title: str = "Cash Flows") -> None:
    flow_values = list(stream)
    time_steps = list(range(len(flow_values)))
    plt.figure()
    plt.bar(time_steps, flow_values)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.xlabel("Period")
    plt.ylabel("Cash Flow Amount")
    plt.title(chart_title)
    plt.tight_layout()
    plt.show()


# Visualizes the loan balance over time and provides a stacked bar chart of principal versus interest components
def plot_amortization(plan: List[Dict], chart_title: str = "Amortization Schedule") -> None:
    time_steps = [entry["period"] for entry in plan]
    rem_balances = [entry["balance"] for entry in plan]
    prin_parts = [entry["principal"] for entry in plan]
    int_parts = [entry["interest"] for entry in plan]

    plt.figure()
    plt.plot(time_steps, rem_balances, label="Outstanding Balance")
    plt.xlabel("Period")
    plt.ylabel("Currency Amount")
    plt.title(chart_title)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.bar(time_steps, prin_parts, label="Principal")
    plt.bar(time_steps, int_parts, bottom=prin_parts, label="Interest")
    plt.xlabel("Period")
    plt.ylabel("Payment Breakdown")
    plt.title(f"{chart_title} (Principal vs Interest)")
    plt.legend()
    plt.tight_layout()
    plt.show()


# Plots annual depreciation expenses and the resulting decline in book value over time
def plot_depreciation(yearly_expenses: Iterable[float], chart_title: str = "Depreciation Over Time") -> None:
    expense_list = list(yearly_expenses)
    timeline = list(range(1, len(expense_list) + 1))
    accumulated_dep = np.cumsum(expense_list)
    # Estimate original cost assuming total depreciation equals cost (for visualization purposes)
    estimated_cost = sum(expense_list)

    plt.figure()
    plt.bar(timeline, expense_list)
    plt.xlabel("Year")
    plt.ylabel("Depreciation Expense")
    plt.title(chart_title)
    plt.tight_layout()
    plt.show()

    plt.figure()
    curr_book_vals = [estimated_cost - acc for acc in accumulated_dep]
    plt.plot(timeline, curr_book_vals, marker="o")
    plt.xlabel("Year")
    plt.ylabel("Book Value")
    plt.title("Book Value Trajectory")
    plt.tight_layout()
    plt.show()


# Creates a profile curve showing how Net Present Value changes with different discount rates
def plot_npv_profile(rate_options: Iterable[float], npv_results: Iterable[float], chart_title: str = "NPV Profile") -> None:
    r_list = list(rate_options)
    n_list = list(npv_results)
    plt.figure()
    plt.plot(r_list, n_list, marker="o")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.xlabel("Discount Rate")
    plt.ylabel("Calculated NPV")
    plt.title(chart_title)
    plt.tight_layout()
    plt.show()


# A general-purpose helper function to plot growth curves for Present Value or Future Value calculations
def plot_pv_fv_growth(x_data: Iterable[float], y_data: Iterable[float], x_axis: str = "Time", y_axis: str = "Amount", chart_title: str = "Growth Curve") -> None:
    xs = list(x_data)
    ys = list(y_data)
    plt.figure()
    plt.plot(xs, ys, marker="o")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(chart_title)
    plt.tight_layout()
    plt.show()