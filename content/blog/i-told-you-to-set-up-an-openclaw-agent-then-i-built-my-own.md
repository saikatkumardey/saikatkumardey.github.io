+++
title = "I Told You to Set Up an OpenClaw Agent. Then I Built My Own."
date = "2026-03-22"
tags = ["agents", "smolclaw", "openclaw"]
+++

Let's say you set up a persistent AI agent. It runs on a cheap VPS, talks to you over Telegram, locks down your SSH, cleans up 97 GitHub repos, builds you a calorie tracker from a lunch photo. You're sold. You [write a blog post telling everyone to do the same thing](/blog/you-should-set-up-an-openclaw-agent/). That was me, a month ago, with OpenClaw.

Then I stopped using it and built my own. Let's talk about why.

## What OpenClaw got right

[OpenClaw](https://github.com/openclaw/openclaw) gives you the hard part for free: a daemon process, Telegram integration, cron scheduling, shell access. You install it, write a `SOUL.md`, and you have a working agent in ten minutes. The agent ran morning news digests, tracked my meals, pushed back on bad ideas. For two weeks it just worked.

So what went wrong? Nothing. That's the thing. The framework was doing exactly what it was designed to do. But I wanted to change how the agent stored memories. I wanted a self-review step at the end of each day. I wanted the handover between sessions to work differently. Every time I reached for something structural, I was reading someone else's code, working around someone else's abstractions. I wanted it to do something else.

## The case for building your own

What's the interesting part of running a persistent agent? It's not the Telegram bot or the cron scheduler. Those are solved problems. It's how the agent remembers, how it reviews its own work, how it decides what to keep and what to forget. That's where all the leverage is. And that's exactly the part you want full control over.

So I built [SmolClaw](https://github.com/saikatkumardey/smolclaw). Claude on Telegram, backed by a folder of markdown files. The entire persistence layer is text files. `SOUL.md` defines who the agent is. `AGENT.md` has standing orders. `MEMORY.md` keeps facts that persist across sessions. Text files you can read, grep, and version-control.

Migration from OpenClaw took one session. I pointed SmolClaw at the old agent's workspace and it read everything: memories, tools, cron configs. One agent read another agent's brain because the brain was just files. I didn't write an export script or run a database migration.

## What happens when the agent owns its own config

Week one, the agent responds like a polite chatbot. It asks permission for everything. "Should I do this? Would you like me to build that?" You correct it. "Don't ask, just do it if it's reversible." It gets better for a session, then restarts and forgets. Back to square one.

Now, week two. The agent starts writing the corrections itself. It reads through the day's conversations, notices the pattern ("user had to repeat the same instruction 4 times"), and edits its own `SOUL.md` to encode the rule. Next restart, the rule is still there because it's a file, not context window. I didn't build a self-editing feature. The agent has write access to its own files and Claude is smart enough to figure out that repeated corrections should be written down. The file system is the memory. Claude is the intelligence. SmolClaw just connects them.

Week three, the agent is building its own tools. I uploaded a photo of my lunch. It logged the calories to a SQLite database it created, built a dashboard, hosted it on a local web server, sent me the URL. I asked for a Hacker News digest every morning. It wrote the cron config and the scraping logic. Running at 7am Jakarta time every day since. Early on it was writing raw SQL for every meal log, rediscovering the schema each session. Its nightly self-review caught the pattern and it built a dedicated tool. That fix came from the agent reviewing its own mistakes, not from me telling it to do anything.

## The 80-line constraint

`MEMORY.md` is capped at 80 lines. This was an accident that turned into the best design decision in the project.

Without the cap, the agent writes everything down. Every preference, every correction, every one-off instruction. Within a week the memory file is 400 lines of noise and the agent can't find anything useful. Sound familiar? It's the same problem humans have with note-taking apps.

With the cap, the agent has to decide what matters. "Would I search for this later?" becomes the filter. Old entries get replaced by more important ones. The memory stays sharp because it's forced to be selective. You only discover this by owning the full system. No framework ships a "limit your agent's memory to 80 lines" feature. You find it yourself.

## What doesn't work

The agent still repeats mistakes I've corrected. I'll tell it to stop doing something, it'll agree, three days later it does the same thing. This is a model limitation. When the relevant instruction scrolls out of context and the agent doesn't happen to load the right memory file, the correction is gone. You can't fix this with better prompting. You fix it with constraints that don't depend on the agent remembering.

Restarts are fragile. There's a handover system that saves a summary before shutdown so the agent can pick up where it left off. When it works, it's seamless. When it doesn't fire (crash, OOM kill), context is just gone.

Debugging is hard. When a cron stops running, you read log files. There's no dashboard. And the obvious one: this is Claude with markdown files and glue code. It's not a new model or a reasoning breakthrough. If that framing doesn't interest you, this isn't for you.

## Why you should build yours

So what are agent frameworks actually solving for you? Tool calling, message routing, API wrappers. Solved problems. The hard problems (memory management, self-correction, knowing when to forget) are still yours. If you're solving those yourself anyway, you might as well own the easy ones too. The total code is small. The decisions are what matter.

Start with OpenClaw. Learn what a persistent agent can do. Then build your own so you control how it does it. SmolClaw is open source. You can install it and start there, or read through it in twenty minutes and build something better.

`curl -fsSL https://raw.githubusercontent.com/saikatkumardey/smolclaw/main/install.sh | bash`

[github.com/saikatkumardey/smolclaw](https://github.com/saikatkumardey/smolclaw)
