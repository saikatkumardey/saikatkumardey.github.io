---
date: 2023-11-14
title: SnapSort - Sorting your photos locally using OpenAI's CLIP model
postSlug: snapsort
featured: false
ogImage: ""
categories:
  - computer vision
  - clip
  - openai
description: SnapSort is a CLI tool that uses OpenAI's CLIP model to sort your photos locally.
---

I wanted a simple tool to segregate screenshots, prescriptions and other document images on my laptop. I couldn't find any tool that could do this locally, so I decided to build one myself. I used OpenAI's CLIP model to build this tool. I call it SnapSort. You can find it [here](https://github.com/saikatkumardey/snapsort).

## What is SnapSort?

SnapSort is a CLI tool that uses OpenAI's CLIP model to sort your photos locally. It can be used to sort photos into categories such as screenshots, documents, memes, etc. It can also be used to sort photos into custom categories.

## How does SnapSort work?

SnapSort uses OpenAI's CLIP model to perform zero-shot prediction from a handful of labels/categories provided to it. It then sorts the photos into the categories based on the predictions. We use HuggingFace's [CLIP](https://huggingface.co/openai/clip-vit-base-patch32) model here.

For my use-case, I provided the following categories to SnapSort, along with a batch of images from the disk:

```json
[
  "a screenshot of a software interface or a screen capture from phone",
  "a photo of an invoice or a receipt",
  "a photo of a real-world scene, an object, a person, or any image not fitting the description of a screenshot, receipt, or invoice"
]
```

CLIP is used to generate the a text-image similarity score for each category. An image is then assigned to the category with the highest score. We could set a threshold for the score to assign an image to a category only if the score is above the threshold.

## How to use SnapSort?

1. `git clone git@github.com:saikatkumardey/snapsort.git`
2. `poetry shell`
3. `poetry install`
4. `python snapsort.py dir --dry-run` (dry-run to see the results without actually moving the files)

You should run `python snapsort.py --help` to see the available options.

## What's next?

SnapSort also inherits the limitations of CLIP.

- We need to manually define the categories in a specific format for CLIP like "a photo of {object}". Sometimes, we don't know all the categories beforehand. We would ideally like it to be automatically categorised and segregated for us. We could use [CLIP+GPT2](https://github.com/jmisilo/clip-gpt-captioning) or [Llava](https://github.com/SkunkworksAI/BakLLaVA) to describe each image. Then we could cluster the images into different categories based on the descriptions.

- Negative label is a must. Since all CLIP does is provide a similarity score between a text and an image, we need to provide a negative label as well. We need a catch-all category for images that don't fit into any of the categories right now, so we don't move them into any of the categories.

- CLIP is not perfect. It can sometimes misclassify images. We would ideally like to have a way to correct the misclassifications. If we have a very specific use-case like mine, we could train a logistic regression model on top of CLIP to have a better classifications.

## Concluding thoughts

CLIP is a very powerful model. I have been wanting to use it for a while now. I barely scratched the surface of what CLIP can do. I am excited to see what else I can do with it.

## References

- [SnapSort](https://github.com/saikatkumardey/snapsort)
- [OpenAI's Repo on CLIP](https://github.com/openai/CLIP)
- [🤗](https://huggingface.co/docs/transformers/main/en/model_doc/clip#transformers.CLIPModel)
