#!/bin/bash
# commit
# date YYYY-mm-dd HH:MM:SS

################################################################################
#
# Changes author and commit dates of a commit.
#
# Warning:
# For OS X you may also install GNU coreutils (brew install coreutils), add it
# to PATH (PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH") and then use
# "2 days ago" syntax.
#
# Example:
# ./git cdc 20ac4d "2 hours ago"
#
# Source:
# http://stackoverflow.com/questions/454734/how-can-one-change-the-timestamp-of-an-old-commit-in-git
#
################################################################################

PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"

commit="$1" datecal="$2"

if [ "${commit}" = "" ] || [ "${datecal}" = "" ]
then
    script_name=`basename "${0}"`
    (>&2 echo "")
    (>&2 echo "Usage: ./${script_name} commit date")
    (>&2 echo "")
    exit 1
fi

temp_branch="temp-rebasing-branch"
current_branch="$(git rev-parse --abbrev-ref HEAD)"

date_timestamp=$(date -d "$datecal" +%s)
date_r=$(date -R -d "$datecal")

git checkout -b "$temp_branch" "$commit"
GIT_COMMITTER_DATE="$date_timestamp" GIT_AUTHOR_DATE="$date_timestamp" git commit --amend --no-edit --date "$date_r"
git checkout "$current_branch"
git rebase  --autostash --committer-date-is-author-date "$commit" --onto "$temp_branch"
git branch -d "$temp_branch"