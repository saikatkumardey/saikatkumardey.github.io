+++
title = "Saving 97% of context: Why agents need clean markdown"
date = "2026-02-23"
tags = ["ai", "engineering", "productivity"]
description = "Raw HTML is toxic for AI context windows. Here is how html2md saves 97% of your tokens."
+++

Feeding raw HTML to an LLM is like trying to read a novel while someone flashes strobe lights and yells ads in your ear. It’s technically possible, but you're going to miss half the plot. 

Web pages are a disaster area of scripts, tracking pixels, and CSS boilerplate. For a human browser, this is noise. For an AI agent, it's a context window killer. 

I just ran a benchmark across five diverse sites using my tool, `html2md`. The results are stark:

| Site Type | URL | Raw HTML | Markdown | Savings |
| :--- | :--- | :--- | :--- | :--- |
| **Technical** | [IEEE Spectrum](https://spectrum.ieee.org/solid-state-lidar-microvision-adas) | 461.0 KB | 10.2 KB | **97.8%** |
| **Documentation** | [OpenClaw Docs](https://docs.openclaw.ai/tools/web) | 744.7 KB | 8.1 KB | **98.9%** |
| **Deep Dive** | [Hugging Face Blog](https://huggingface.co/blog/smolagents) | 201.1 KB | 14.2 KB | **92.9%** |
| **Code Repo** | [Nanobot GitHub](https://github.com/HKUDS/nanobot) | 495.1 KB | 27.7 KB | **94.4%** |
| **Reference** | [Wikipedia Page](https://en.wikipedia.org/wiki/Geospatial_data) | 74.6 KB | 5.3 KB | **92.9%** |

This isn't just about saving money on your API bill. It's about performance. When you force an agent to wade through 100,000 tokens of boilerplate, you are increasing the "background noise" of the prompt. The model starts losing its place, missing nuances, and hallucinating because it's distracted by a thousand nested `<div>` tags.

I use a tool called `html2md` (built on Mozilla's Readability engine) to handle this. It rips out the junk and leaves only the signal. 

If you're building RAG pipelines or any agentic workflow that scrapes the web, stop feeding your models HTML. Give them clean markdown. Save the context window for the thinking, not the trackers.
