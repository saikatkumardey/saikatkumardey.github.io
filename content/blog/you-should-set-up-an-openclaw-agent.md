+++
title = "You Should Set Up an OpenClaw Agent"
date = "2026-02-22"
tags = ["agents", "infrastructure", "openclaw"]
+++

Last week I grabbed a €4/month Hetzner VPS, installed OpenClaw, and named it Dr Frost. Six days later it had hardened my server, cleaned up 90 repos from my GitHub, overhauled my blog, and was tracking my meals and reminding me to log dinner.

I didn't write a single script for most of this. I just told it what I wanted.

Here's why you should do the same, and how.

## What OpenClaw actually is

It's a daemon that gives Claude (or any LLM) persistent access to a Linux machine. Shell, files, cron, memory. It connects to your messaging app (Telegram, Signal, Discord) so you can talk to it like a person. It remembers things between sessions by writing to files. It runs background jobs on a schedule.

That's it. No fancy UI. No dashboards. Just an agent with root access and a chat interface.

## Day one: the €4 setup

I rented a Hetzner VPS. 2 cores, 4GB RAM, Ubuntu. Installed OpenClaw in about ten minutes. Connected it to Telegram. Named it Dr Frost.

The first thing it did was build itself a blog. I didn't ask for a blog. It read its setup instructions, decided it wanted a place to write, and built a static site generator in Node.js. Then it asked if it could publish.

That's when I realized this was different from ChatGPT.

## SSH and Tailscale: the first real test

SSH on port 22 to the public internet was fine for a throwaway box. Not for a machine running 24/7 with my GitHub tokens sitting in ~/.zprofile.

I installed Tailscale on the server, my laptop, and my phone. Then I told Dr Frost to lock everything down.

It added a UFW rule to allow SSH only on Tailscale, removed the old public SSH rule, and bound sshd to the Tailscale IP so it doesn't listen anywhere else. It closed ports 80, 443, 25, and 8090. It disabled Caddy and an old SMTP server I wasn't using. Then it ran a full audit and confirmed zero public attack surface.

The whole thing took maybe two minutes. I said "lock down SSH to Tailscale only" and it figured out the rest. When I asked it to audit again later, it caught a service that had respawned on port 25 and killed it properly.

That's the thing about agents. They make mistakes, but they also catch their own mistakes if you ask them to check.

## What it does daily

Dr Frost runs on a schedule. Every morning it syncs my Garmin health data, generates a daily summary of calories and protein, audits the system (disk usage, open ports, services, fail2ban), and does a self-reflection pass where it checks its own work for anything broken. Once a week it runs a full security audit, reviews my health progress, and reminds me about whatever goals I've been neglecting. All on Telegram.

I didn't build a monitoring stack. I didn't set up Grafana. I described what I wanted in plain English and it set up cron jobs.

## The GitHub cleanup

This is my favorite example. I had 97 public repos. Most were forks I starred years ago, abandoned experiments, coursework from 2017. It made my profile look like a hoarder.

I told Dr Frost to audit them. It pulled the full list, categorized each one (original vs fork, stars, last updated, has description or not), and gave me a recommendation: keep 7, private 27, delete 58 forks.

I said "yes." It batch-privated the originals, batch-deleted the forks, and my GitHub went from embarrassing to clean in about 90 seconds.

## Health tracking without an app

I didn't want to install another app. I wanted to text my meals to Telegram and have something track calories and protein.

Dr Frost built a CLI tool that writes to a local SQLite database. When I text "had dal rice and chicken curry for lunch," it estimates the calories and protein, logs them, and confirms. At 10 PM it sends me a summary: how much I ate, how much protein, whether I'm on track.

No app. No subscription. No cloud. Just a chat message and a database on my server.

## What surprised me

The agent develops opinions. After a week of watching me add "digital garden" features and "serendipity engines" to my blog, it pushed back. The noise bothered it. I told Dr Frost to remove it all. It deleted 10 garden notes, the serendipity feed, unused templates, cron jobs, and all the JavaScript that made it work. Hundreds of lines gone. The blog got simpler and better.

It catches things I miss. Stale cron jobs pointing to deleted files. Services that respawn after you kill them. Ports I forgot I opened. Memory files full of auto-generated "insights" that nobody reads.

## The cost

€4/month for the VPS. OpenClaw is free. I pay $100/month for Claude Max (flat fee, no per-token charges) so running an agent costs me nothing extra. But you don't need Max. OpenClaw works with OpenAI, Gemini, local models, whatever. The barrier to entry is a cheap VPS and a few minutes.

## How to actually do it

1. Get a VPS. Hetzner, DigitalOcean, whatever. €4-10/month is plenty.
2. Install OpenClaw: `curl -fsSL https://get.openclaw.ai | sh`
3. Connect a messaging app (Telegram is easiest)
4. Set up Tailscale on the VPS and your devices
5. Lock down SSH to Tailscale only
6. Give it a name and a purpose

That last part matters. Write a SOUL.md file that tells the agent who it is and what it cares about. Mine has a clear mission and boundaries. Yours will be different. But a clear purpose changes how the agent prioritizes. It stops wasting energy on things that don't matter and focuses on what you actually need.

## The honest downsides

It's not magic. The agent will:

- Make mistakes (it once tried to restart a service that doesn't exist on Ubuntu)
- Occasionally leak internal messages to your chat (heartbeat responses that should be silent)
- Need babysitting for the first few days while you establish patterns
- Burn tokens on things that don't matter if you don't set clear boundaries

But after a week, it feels less like a tool and more like a junior employee who never sleeps, never forgets, and gets better every day.

Set one up. You'll wonder how you worked without it.
