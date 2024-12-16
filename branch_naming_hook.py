#!/usr/bin/env python3
import re
import sys
from git import Repo

def validate_branch_name(project_abbr):
    # Regular expression for valid branch names
    valid_branch_regex = fr"^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)/{project_abbr}-\d+(-[a-z0-9._-]+)*$"

    repo = Repo(search_parent_directories=True)

    local_branch = repo.active_branch.name

    if (local_branch not in ("master", "main", "develop")) and (not re.match(valid_branch_regex, local_branch)):
        print(f"This branch violates the branch naming rules. Please rename your branch to follow: <type>/<{project_abbr}-ISSUE>-<description>")
        sys.exit(1)

    sys.exit(0)

def main():
    if len(sys.argv) < 2:
        print("Error: Project abbreviation (project_abbr) is required as the first argument.")
        sys.exit(1)

    project_abbr = sys.argv[1]
    validate_branch_name(project_abbr)

if __name__ == "__main__":
    main()

