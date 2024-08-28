#!/usr/bin/env python3

import os

from machetli import pddl, tools

PLANNER_REPO = os.environ["DOWNWARD_REPO"]
PLANNER = os.path.join(PLANNER_REPO, "fast-downward.py")


def evaluate(domain, problem):
    solvable_command = [
        PLANNER, domain, problem, "--search",
        "astar(lmcount(lm_rhw(use_orders=false)))",
    ]
    result_solvable = tools.run_with_limits(
        solvable_command, time_limit=10, memory_limit=3000)

    unsolvable_command = [
        PLANNER, domain, problem, "--search",
        "astar(lmcount(lm_rhw(use_orders=true)))",
    ]
    result_unsolvable = tools.run_with_limits(
        unsolvable_command, time_limit=10, memory_limit=3000)

    return ("Solution found." in result_solvable.stdout and
            "Search stopped without finding a solution." in result_unsolvable.stdout)

if __name__ == "__main__":
    pddl.run_evaluator(evaluate)
