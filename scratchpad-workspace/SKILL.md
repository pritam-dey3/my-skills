---
name: scratchpad-workspace
license: Apache-2.0
description: Use this skill for any standalone, one-off exploratory task — research, data exploration, prototyping or calculations — that should NOT be added to or mixed into an existing codebase or product repository. Use this whenever the user's request implies throwaway, exploratory, or investigative work rather than a change to a tracked project. Do NOT use this skill when the user explicitly asks to modify, extend, or fix an existing codebase.
---
# Exploration workspace
Use a dedicated ordinary folder for a self-contained exploration. This is organisational isolation, not a locked-down security sandbox: work can use normal local tools, but all files created or edited for the task stay in that workspace.

## When to use it

Use this skill when the user is exploring, researching, modelling, prototyping, or producing one-off documents and does not want the work mixed into a product repository. Do not use it when the user explicitly asks to modify an existing codebase.

## Workspace choice

- Use `./agent-tasks` inside the current active workspace as the exploration root. Create it when needed; never create `agent-tasks` in the user's home directory, a global directory, or beside the active workspace.
- Create each exploration workspace under `<active-workspace>/agent-tasks/YYYY-MM-DD/<short-task-name>`. Use the current date and a short, descriptive task-folder name that clearly identifies the work.
- Make the new folder the active workspace or working directory before creating task files, using the current agent harness's supported workflow.
- Never create exploration artifacts in a parent folder, the user's home directory, or an unrelated repository.
- Reading source material from another location is allowed when needed. Copy only the needed inputs into this workspace before modifying them, unless the user authorizes edits to the original.

## Folder layout

Create only the folders that the task needs:

```text
agent-tasks/YYYY-MM-DD/<short-task-name>/
  README.md # task description and exploration record
  inputs/   # source files, extracts, or immutable inputs
  work/     # scripts, calculations, intermediate exports, and scratch files
  notes/    # research notes and assumptions
  outputs/  # finished user-facing deliverables only
```

- Put temporary code and working data in `work/`; do not place it beside final files.
- Put documents, spreadsheets, charts, decks, or other deliverables intended for the user in `outputs/`.
- Keep inputs distinct from derived data so it is clear what was provided versus generated.
- Create a `README.md` in every task folder. Start it with a concise task description, then keep it updated with new learnings and notable developments from the exploration.
- Do not create repository scaffolding, a Git repository, or empty folders unless the task needs them.

## Operating rules

- Treat the session folder as the write boundary. Do not modify an external codebase, its configuration, or its Git state unless the user explicitly asks.
- Preserve any pre-existing user files. Do not delete a session workspace merely because the exploration is complete.
- If the exploration produces a reusable implementation, present it as an output or a proposed patch; do not merge it into a main project without direct authorization.
- When handing work back, link or name only the finished files under `outputs/`, and mention the workspace path when it helps the user resume the session.
- The inputs folder may contain some files those are specific to the given task at hand, or inputs can be directly referenced in the scripts from other locations as well including other task folders. The inputs folder is not a requirement, but it is a good practice to keep the inputs separate from the work and outputs.

## License

Copyright 2026 Pritam Dey.

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).
This license applies to the original content in this skill folder, not to other
skills in the collection. Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied. See the license for the
specific language governing permissions and limitations.