#!/usr/bin/env bash
LC_ALL=C

local_branch="$(git rev-parse --abbrev-ref HEAD)"
project_abbr="$1"

if [[ -z "$project_abbr" ]]; then
    echo "Error: Project abbreviation (project_abbr) is required as the first argument."
    exit 1
fi

valid_branch_regex="^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)/${project_abbr}-[0-9]+(-[a-z0-9._-]+)*$"

message="This branch violates the branch naming rules. Please rename your branch."

if [[ ! $local_branch =~ $valid_branch_regex ]]
then
    echo "$message"
    exit 1
fi

exit 0
