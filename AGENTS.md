# Project rules for AI agents (pi)

## Git — STRICT
- **NEVER** run `git commit`, `git push`, `git add` (staging), `git merge`, `git rebase`, `git reset --hard`, or any other git command that modifies the repo or the remote.
- **NEVER** force-push, tag, or create PRs.
- The human handles ALL git operations (committing, pushing, deploying).
- You may only use **read-only** git commands (`git status`, `git log`, `git diff`) and even then only when it helps answer a question.

## General
- Edit files only in this project directory unless asked otherwise.
- When a change needs to be deployed, tell the human what to commit/push instead of doing it.
