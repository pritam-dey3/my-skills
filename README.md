# My Skills

A personal collection of agent skills curated by Pritam Dey. Only
`scratchpad-workspace` was created by Pritam; the other skills are third-party
work, retained here for convenience rather than claimed as original work.

## Install

Requires Node.js and npm. After this repository is published on GitHub, run:

```sh
npx skills add pritam-dey3/my-skills
```

The command uses the [Vercel Skills CLI](https://github.com/vercel-labs/skills).
No npm package or custom installer is required for this collection.

List available skills without installing:

```sh
npx skills add pritam-dey3/my-skills --list
```

Install just the original scratchpad skill:

```sh
npx skills add pritam-dey3/my-skills --skill scratchpad-workspace
```

Add `--global` to install at user scope instead of in the current project.

## Updates

This collection uses one Git repository with ordinary skill folders. It does not
use Git submodules or nested repositories.

Users can update installed skills with:

```sh
npx skills update
```

The CLI updates from the recorded installation source. Skills installed from
`pritam-dey3/my-skills` therefore receive the versions published in this
repository. This is an explicit update command, not a background auto-update
service, and it does not synchronize this collection's third-party copies with
their original upstream repositories.

To receive upstream changes here, the maintainer must update the ordinary
folders and publish the changes. Users who prefer direct upstream updates can
install those skills from their original repositories instead. See the
[CLI documentation](https://github.com/vercel-labs/skills) for update behavior.

## Collection

| Skill | Purpose | Origin |
| --- | --- | --- |
| [scratchpad-workspace](scratchpad-workspace/SKILL.md) | Keep one-off explorations in a dedicated workspace | Original by Pritam Dey |
| [asd-ste100](asd-ste100/SKILL.md) | Simplified Technical English guidance | Third-party |
| [codebase-to-course](codebase-to-course/SKILL.md) | Interactive courses explaining codebases | Third-party |
| [pyecharts-viz](pyecharts-viz/SKILL.md) | Visualization examples with pyecharts | Adapted from pyecharts/skills; modified by Pritam Dey |
| [revealjs](revealjs/SKILL.md) | HTML presentations with reveal.js | Ryan Brown; ryanbbrown/revealjs-skill |

## Attribution And Reuse

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for authors, sources,
and licenses. This collection does not relicense
third-party content. Preserve each author's license and notices when reusing it.

**Publication status:** local preparation only. Resolve the outstanding source
and redistribution permissions in the notices before publishing this collection.
The original scratchpad skill is licensed under
[Apache License 2.0](scratchpad-workspace/LICENSE); this does not relicense the
other skills in the collection.

## Maintaining The Collection

Keep each skill in its own folder with a `SKILL.md` containing YAML `name` and
`description` fields. Keep its scripts, references, and templates with it.
Record the upstream repository, revision, license, and local modifications when
adding or updating third-party material. Do not replace upstream notices with a
blanket repository license.

Validate local discovery from the repository root:

```sh
npx skills add . --list
```