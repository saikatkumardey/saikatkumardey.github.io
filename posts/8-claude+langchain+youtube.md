---
title: "I summarised a 3 hour long youtube video using Langchain + Claude"
date: 2023-05-18T20:03:57+05:30
description: ""
categories: ["llm", "ai", "claude", "langchain"]
---

I used Langchain + Claude to summarise [Sam Altman's testimony to the US Senate on AI](https://www.youtube.com/watch/?v=fP5YdyjTfG0). The video is 3 hours long and the transcript has about 30k+ tokens. I used Langchain to extract the transcript and Claude to summarise it. The result is a 1 page summary of the key points from the video. I have included the summary, code, and prompt below.

Tech:

- Langchain to extract the transcript from YouTube
- Claude (`claude-instant-v1-100k`) to summarise the transcript

## Prompt

```
"""
Please write a professional summary with a beginning, middle, and end based on the video transcript.

Instructions

- Do not include any details that are not mentioned in the video.
- Use bullet points and section headers to organize your summary.
- Do not include any personal opinions or thoughts.
- Include title, introduction, witnesses, their testimonies, key takeaways and conclusion.


Video transcript:
"""
```

## Summary

```

Here is a professional summary of the key points from the Senate hearing on AI oversight:

# Senate Hearing on AI Oversight - May 16, 2023

## Witnesses

- Sam Altman, CEO of OpenAI
- Christina Montgomery, IBM's Vice President and Chief Privacy and Trust Officer
- Gary Marcus, AI scientist and entrepreneur

## Key Takeaways

- AI has the potential for both great benefits and substantial risks. Proper oversight and regulation are needed to maximize the benefits while mitigating the risks.

- Witnesses recommend a combination of self-regulation by AI companies and government regulation to ensure trustworthy and safe AI.

- High-risk uses of AI, such as those impacting elections, medical advice, and national security, should face the strictest oversight and regulation.

- Transparency, accountability, and limits on certain AI capabilities are seen as important principles for a regulatory framework.

- An independent agency focused on AI may be needed to keep up with the rapid pace of AI development. However, proper resources and expertise will be critical for such an agency to be effective.

- International coordination will also be important given the global nature of AI development and risks. The U.S. should take a leadership role in setting responsible AI standards.

## Conclusion

The hearing highlighted both the promise and potential pitfalls of generative AI. While witnesses differed in some details, there was broad agreement that a combination of self-regulation, government oversight, and international coordination will be essential to maximize the benefits of AI technologies while mitigating the risks. The Senate considers this hearing as the first step in developing appropriate policies and safeguards for AI.

```

## Code

```python
import argparse
import os

import anthropic
from langchain.document_loaders import YoutubeLoader


def load_transcript(url):
    loader = YoutubeLoader.from_youtube_url(
        url,
        add_video_info=True,
    )
    docs = loader.load()
    if len(docs) == 0:
        raise ValueError("Sorry, No transcript found.😢")
    return docs[0]


def write_summary(doc):

    anthropic_key = os.getenv("ANTHROPIC_KEY")

    client = anthropic.Client(anthropic_key)

    prompt = f"""
Please write a professional summary with a beginning, middle, and end based on the video transcript.

Instructions

- Do not include any details that are not mentioned in the video.
- Use bullet points and section headers to organize your summary.
- Do not include any personal opinions or thoughts.
- Include title, introduction, witnesses, their testimonies, key takeaways and conclusion.


Video transcript:

{doc.dict()}

"""
    prompt_formatted = (
        f"{anthropic.HUMAN_PROMPT}{prompt}\n{anthropic.AI_PROMPT}"
    )
    response = client.completion(
        prompt=prompt_formatted,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-instant-v1-100k",
        max_tokens_to_sample=100000,
        temperature=0.3,
    )
    return response["completion"]


def main():

    parser = argparse.ArgumentParser(
        description="Write a professional summary based on a YouTube video transcript."
    )
    parser.add_argument("url", type=str, help="The YouTube URL of the video.")
    args = parser.parse_args()
    try:
        doc = load_transcript(args.url)
        summary = write_summary(doc)
        print(summary)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

```

## Run the script

- First install the required packages:

`pip install anthropic langchain`

- Then set the `ANTHROPIC_KEY` environment variable to your API key obtained from [Anthropic Console](https://console.anthropic.com).

- Run this script with the following command:

```bash
python3 main.py https://www.youtube.com/watch/?v=fP5YdyjTfG0
```

**Fun fact:** _Bing Chat (GPT-4) helped me organise my dirty notebook into a nice CLI script which I share with you all today._
