+++
title = "Saving 97% of context: Why agents need clean markdown"
date = "2026-02-23"
tags = ["ai", "engineering", "productivity"]
description = "Raw HTML is toxic for AI context windows. Here is how html2md saves 97% of your tokens."
+++

Feeding raw HTML to an LLM is like trying to read a novel while someone flashes strobe lights and yells ads in your ear. It’s technically possible, but you're going to miss half the plot. 

Web pages are a disaster area of scripts, tracking pixels, and CSS boilerplate. For a human browser, this is noise. For an AI agent, it's a context window killer. 

I just ran a test on a standard technical article from IEEE Spectrum. The numbers are pretty stark:
- **Raw HTML:** 472 KB (roughly 118,000 tokens)
- **Cleaned Markdown:** 10 KB (about 2,600 tokens)

That is a **97.8% reduction** in tokens. 

This isn't just about saving money on your API bill. It's about performance. When you force an agent to wade through 100,000 tokens of boilerplate, you are increasing the "background noise" of the prompt. The model starts losing its place, missing nuances, and hallucinating because it's distracted by a thousand nested `<div>` tags.

I use a tool called `html2md` (built on Mozilla's Readability engine) to handle this. It rips out the junk and leaves only the signal. 

If you're building RAG pipelines or any agentic workflow that scrapes the web, stop feeding your models HTML. Give them clean markdown. Save the context window for the thinking, not the trackers.
