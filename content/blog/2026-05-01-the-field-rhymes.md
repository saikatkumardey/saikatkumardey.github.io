+++
draft = false
title = "The Field Rhymes: A First-Principles Walk Through Modern Machine Learning in 93 Ideas"
date = "2026-05-01"
tags = ["machine learning", "deep learning", "ai", "education"]
+++


# The Field Rhymes


A first-principles walk through modern machine learning, in 93 ideas.


## Table of Contents

- [Prologue](#prologue)
- [Act I — The Apparatus](#the-apparatus)
  - [Chapter 1: How a Network Learns](#how-a-network-learns)
  - [Chapter 2: How a Network Reads](#how-a-network-reads)
  - [Chapter 3: How a Network Speaks](#how-a-network-speaks)
- [Act II — The Routing Insight](#the-routing-insight)
  - [Chapter 4: The Puzzle of Long Sentences](#the-puzzle-of-long-sentences)
  - [Chapter 5: Attention](#attention)
  - [Chapter 6: Many Heads](#many-heads)
  - [Chapter 7: Positional Encoding](#positional-encoding)
  - [Chapter 8: Residuals and LayerNorm](#residuals-and-layernorm)
  - [Chapter 9: The Transformer Block](#the-transformer-block)
  - [Chapter 10: Encoder, Decoder, Both, Neither](#encoder-decoder-both-neither)
- [Act III — The Scaling Discovery](#the-scaling-discovery)
  - [Chapter 11: The Empirical Surprise](#the-empirical-surprise)
  - [Chapter 12: Scaling Laws](#scaling-laws)
  - [Chapter 13: The Chinchilla Correction](#the-chinchilla-correction)
  - [Chapter 14: The Phase Transition](#the-phase-transition)
  - [Chapter 15: Grokking](#grokking)
- [Act IV — The Alignment Problem](#the-alignment-problem)
  - [Chapter 16: Supervised Fine-Tuning](#supervised-fine-tuning)
  - [Chapter 17: Reward Models](#reward-models)
  - [Chapter 18: RLHF](#rlhf)
  - [Chapter 19: The Magical Collapse: DPO](#the-magical-collapse-dpo)
  - [Chapter 20: GRPO and the End of the Value Function](#grpo-and-the-end-of-the-value-function)
  - [Chapter 21: Constitutional AI](#constitutional-ai)
  - [Chapter 22: LoRA and the Affordable Fine-Tune](#lora-and-the-affordable-fine-tune)
- [Act V — The Inference Problem](#the-inference-problem)
  - [Chapter 23: Why Inference Is Hard](#why-inference-is-hard)
  - [Chapter 24: The KV Cache](#the-kv-cache)
  - [Chapter 25: Grouped-Query Attention](#grouped-query-attention)
  - [Chapter 26: FlashAttention](#flashattention)
  - [Chapter 27: Quantization](#quantization)
  - [Chapter 28: Speculative Decoding](#speculative-decoding)
  - [Chapter 29: Continuous Batching](#continuous-batching)
  - [Chapter 30: Mixture of Experts](#mixture-of-experts)
- [Act VI — The Reasoning Problem](#the-reasoning-problem)
  - [Chapter 31: In-Context Learning](#in-context-learning)
  - [Chapter 32: Chain-of-Thought](#chain-of-thought)
  - [Chapter 33: Self-Consistency](#self-consistency)
  - [Chapter 34: Tool Use](#tool-use)
  - [Chapter 35: RAG](#rag)
  - [Chapter 36: Reasoning RL](#reasoning-rl)
- [Act VII — The Other Modalities](#the-other-modalities)
  - [Chapter 37: Vision Transformers](#vision-transformers)
  - [Chapter 38: CLIP and Multimodal Embeddings](#clip-and-multimodal-embeddings)
  - [Chapter 39: Vision-Language Models](#vision-language-models)
  - [Chapter 40: Segmentation: Open-Vocabulary and Promptable](#segmentation-open-vocabulary-and-promptable)
  - [Chapter 41: Diffusion Models](#diffusion-models)
  - [Chapter 42: Video Generation](#video-generation)
  - [Chapter 43: AlphaFold](#alphafold)



# Prologue


A wager about how the field rhymes — and how to read what follows.

On why most ML writing is forgettable

Most ML writing fails the memory test for one reason: it tells you what a concept is before it tells you why it had to exist.

"Attention is softmax(QKᵀ/√d) · V" is a definition. It is not a memory. A memory is: "the field needed every word in a sentence to look at every other word in a single step, because recurrent networks were too slow and forgot too much, and the only mechanism that lets you do this with learned routing is a soft, content-addressable lookup — which somebody built, and called attention."

The first kind of statement is what you forget six months after the course. The second kind is what stays.

This book is built on a wager. The wager is that if every concept is presented as the answer to a question the field couldn't otherwise answer, you will not have to memorize anything. The structure will hold the concept in place for you. Long after you have forgotten the formula, you will remember the puzzle that demanded it.

The thesis

The thesis is that the field rhymes.

What I mean: every major idea in modern machine learning is a response to a constraint introduced by a previous major idea. Recurrence couldn't see across long sequences, so attention emerged.

Attention without depth couldn't compose, so the Transformer block emerged. The Transformer scaled, so scaling laws emerged. Pre-training produced models that knew everything and followed nothing, so supervised fine-tuning emerged. SFT produced models that were technically correct but unhelpful, so reinforcement learning from human feedback emerged. RLHF was expensive and complex, so direct preference optimization emerged.

Reasoning at inference was expensive, so reinforcement learning on verifiable rewards emerged. Each new idea is the answer to a problem the previous idea created.

This rhyming structure is the only structure I trust. Subject-area maps that organize concepts by topic — "here is everything about attention, here is everything about training, here is everything about inference" — present the field as a flat encyclopedia. The encyclopedia view is useful for reference.

It is not how the field exists. The field exists as a chain of we tried X; X failed in this specific way; we tried Y to fix that failure. Every act in this book is one link in that chain.

How to read this book

The book is organized into seven acts and a small number of bookends. Each act introduces the problem the field had to solve at one moment in time. Each chapter inside an act introduces one or two concepts as answers to that problem.

Each concept, when it appears, follows the same five-beat pattern. I do this on purpose, and it is worth flagging now so you can spot it.

The puzzle. What couldn't the field do without this idea?

The bad attempt. What was tried first, and why it failed. Failure makes the answer earned.

The trick. The new move, in plain words, no math. The reader should feel the aha.

The math, as sanity check. The formula, with each symbol explained by what it does, not by what it is.

The thing nobody mentions. A non-obvious consequence, pitfall, or open question. The surprise.

The fifth beat is the one that matters most for memory. The first four beats give you the official story. The fifth gives you the hook — the strange, asymmetric, off-topic detail that turns a forgettable definition into something that sticks.

Whenever I find myself writing about a concept and I cannot generate a fifth beat for it, that is a sign I do not yet understand it well enough to teach it. I rewrite, or I cut.

What this book is not

It is not a textbook. A textbook is structured to be comprehensive and authoritative. This book is structured to be memorable and opinionated. It will leave things out. It will refuse to be neutral when neutrality is wrong.

It is not a reference. If you need the exact parameters of FlashAttention-3, or the precise formulation of Group Relative

Policy Optimization, or the dimension of the latent space in Stable Diffusion XL, the wiki this book is based on is more useful, and the original papers are more useful still. The book points at the wiki for reference; the wiki points at the papers; the papers point at the truth.

It is not finished. The field rhymes, but it does not stop. Every chapter ends on what is currently understood. Some chapters end on what is currently disputed. A few chapters end on what is currently open.

By the time you read this, some of the open questions will have been answered, and others will have opened. Research is not a fixed body of knowledge but a moving boundary, and any book that pretends otherwise is lying.

What this book is

It is a walk through modern machine learning, ordered by the problems the field had to solve, told in the voice of someone who has been confused by all of it and has now made peace with most of it.

It assumes you can program. It assumes you have at least half-glanced at calculus and linear algebra. It does not assume you know what attention is, or what a

Transformer block looks like, or why RLHF was needed. If you already know those things, you may still find the framing useful — it is the connections between concepts that this book optimizes for, and connections are what separate a list of facts from an internal model.

If you read it carefully, you should be able to walk into any conversation with a frontier ML team and explain, in your own words, every major idea on a ninety-three-concept map of the field. Not recite.

Explain. With reasons. People who do this for a living will know the difference.

A confession before we start

I will tell you what I do not know, and what the field does not know, as we go.

There are a small number of things in this book that nobody understands. Why does the Transformer scale so cleanly with compute? Why does in-context learning work? Why does grokking — sudden generalization long after training loss has hit zero — happen at all? Why do wide flat minima generalize and narrow ones not?

Why do emergent abilities seem to appear at specific scales? These are unsolved problems. They will not be solved on the way out of a textbook chapter.

A book that pretends these are solved is forgettable. A book that names them as open is unforgettable. I will name them.

There are also a small number of places where the field has settled on something that I think will turn out to be wrong, or at least wrong-shaped. I will say so when I think so. I will mark my opinions clearly so you can disagree with them. The voice of this book is opinionated by design; you are encouraged to read it the way you would read a smart, slightly cranky friend explaining their field over dinner. Disagree freely. Argue back. The book will not be hurt.

Now let us begin.

End of Prologue.


## The Apparatus


How a network learns to read, optimize, and speak.

Where we begin

A neural network is a function with knobs.

The knobs are called parameters. The function takes some input — a sentence, an image, a row of numbers — and produces some output. There are billions of knobs in a frontier model. Setting them all by hand is obviously impossible. So we need a procedure that takes a network whose knobs are set badly and turns it into one whose knobs are set well, automatically, by example.

That procedure is the entire content of this act. By the end you will be able to describe, from memory, the three things every modern model has in common: how it learns (Chapter 1), how it reads (Chapter 2), and how it speaks (Chapter 3). These



are the apparatus. Act II will be the architecture that ties them together. Act

III will be what happens when you scale them up. Everything else in this book is footnotes to those four things.

## Chapter 1


### How a Network Learns


Imagine you have a function f(x; θ) — input x, parameters θ. You also have a loss function L(θ) that measures how badly the function performs on training data.

Lower loss is better; zero loss means perfect prediction. The loss is a number that depends on the parameters. As you turn the knobs, the loss moves. Training is the problem of turning the knobs to make the loss go down.

In one dimension this is trivial. If the loss goes up when you increase θ, you decrease θ. If it goes down, you increase θ.

You compute the derivative of L with respect to θ, take a small step in the opposite direction, and you've descended a little. Repeat until the loss stops going down.

In a million dimensions it is also trivial — at least mechanically. You compute the gradient of L with respect to every parameter (one number per parameter — the partial derivative), and take a step in the direction opposite the gradient. The math is identical. The bookkeeping is the part that took years to invent — backpropagation, the algorithmic trick that lets you compute all those partial derivatives in roughly the cost of one forward pass instead of millions of them.

But the idea is the same: each knob turns by an amount proportional to how much it would help to turn it.

That is gradient descent. It is the only learning algorithm modern deep networks use. Everything else is a refinement, a hack, or a trick.

The first refinement is stochastic.

Computing the gradient of the full loss requires looking at every training example.

This is too slow when you have a billion examples. Instead, we compute the gradient on a small minibatch — say, 256 examples — and use that as a noisy estimate of the true gradient. We take a step. We grab the next 256. We take another step. Over time, the noise averages out. We arrive at the same place full-batch gradient descent would have, much faster, with one quirk: SGD doesn't quite descend the loss surface, it bounces around it.

The bouncing turns out to be a feature, not a bug. The bouncing helps the optimizer escape narrow valleys (which tend to generalize poorly) and find wide ones (which tend to generalize well). This is one of the deepest empirical facts in machine learning. We do not have a complete theory of it. Whole research careers have been spent trying to formalize why SGD's noise is precisely the right kind of noise to find good minima, and no answer is yet definitive. The phenomenon is real; the explanation is open.

The second refinement is momentum.

The gradient at any one minibatch is noisy.

If you average gradients over a few recent minibatches — an exponential moving average — the noise smooths out and you keep track of the direction of consistent descent. Momentum makes the optimizer behave like a heavy ball rolling downhill: it builds up speed in flat directions, dampens oscillation in steep ones, and rolls through small bumps that pure SGD would get stuck on.

The third refinement is adaptive learning rates. Different parameters need different step sizes. A parameter whose gradient is consistently small needs a bigger step; one whose gradient swings wildly needs a smaller one. Adam is the standard recipe.

It tracks an exponential moving average of the gradient (the momentum) and an exponential moving average of the squared gradient (the variance), and divides the first by the square root of the second. The result: each parameter gets its own adaptive learning rate, scaled to its own statistics. Adam also includes a bias correction — without it, the moving averages are biased toward zero in the first few hundred steps because they start from zero. The bias correction undoes this. Almost every paper you read used

Adam or one of its descendants.

We need one more piece. As you stack layers — and modern networks are dozens of layers deep — the gradient that flows from the loss back to the early layers passes through every intermediate layer's local Jacobian. If those Jacobians have small singular values, the gradient vanishes: by the time it reaches the early layers, it's effectively zero, and those layers don't learn. The same problem in reverse — exploding gradients — also happens, less often.

The history of training deep networks is largely a history of fighting this single problem. Batch normalization was an early fix, popular in vision: normalize each layer's activations across the batch dimension so they don't drift to weird scales, and gradients stay better-behaved.

Layer normalization is the Transformer-friendly version, normalizing across the feature dimension instead. Residual connections (we'll meet them in Act II) are a more powerful fix: add a "highway"

through which gradients can flow without being multiplied by anything. Modern deep networks use residuals and normalization in combination. Neither is optional.

The thing nobody mentions: every architectural choice in deep learning, from

ResNets to Transformers to Mamba, is filtered by whether it cooperates with gradient descent. We don't choose architectures because they are mathematically beautiful. We choose them because their loss landscapes are easy for

SGD to descend. This is a strong inductive bias — a prior on which functions the optimizer can find — and it shapes what we can build more than any theoretical argument. The architecture you can train is the architecture that wins. The history of the field is the history of architectures that play nicely with SGD; the others, however elegant, are footnotes.



## Chapter 2


### How a Network Reads


Networks operate on numbers.

Language is text. The first job of any language model is to bridge that gap: turn text into numbers, in a way that preserves meaning and works at any length.

The naive approach is to assign each unique word in a corpus an integer. The vocabulary is the set of words. "the" is 1, "cat" is 2, "Saikat" is — well, it depends on whether "Saikat" appeared in the training data. If it didn't, you have an out-of-vocabulary token, and the model has to fall back on a generic placeholder like <UNK>.

You lose all information about that word.

This fails for English. It fails harder for languages with rich morphology —

Finnish, Turkish, Tamil — where every word can take dozens of inflected forms, and a vocabulary big enough to cover them all becomes prohibitive. It fails completely for code, math, and scientific text where novel tokens appear constantly. You cannot train a coherent language model on a vocabulary that throws away most of what it sees.

The fix, called subword tokenization, is a clever compromise. Instead of breaking text at word boundaries, you break it at frequent substring boundaries. The most common technique is Byte Pair Encoding — BPE. Start with a vocabulary of single bytes (or characters). Find the most frequent pair of adjacent tokens in your training corpus — say, "th" — and merge it into a single new token. Find the next most frequent pair, perhaps "the" or " e", and merge that. Repeat until your vocabulary reaches a target size, typically thirty thousand to a hundred and fifty thousand tokens.

The result is a vocabulary where common words are single tokens, rare words break into a few subword pieces, and never-before-seen strings break into characters or short fragments. Nothing is ever truly out-of-vocabulary; the model can always represent any text, just at a granularity that depends on how rare the input is. "Bandung" might be one token in an Indonesian-trained model and four in an English one. The choice is made by frequency, automatically.

Once we have token IDs, we need to turn them into vectors. This is what an embedding layer does. It is just a lookup table: for each token ID in the vocabulary, store a learnable vector of some dimension d (typically 1024, 4096, or larger in frontier models). Token 47, which let's say represents "Paris," has a vector. Token 312, "France," has another. Initially these vectors are random. During training, gradient descent slowly nudges each token's vector toward a position in space that makes the network's predictions accurate. Over time, vectors of related tokens cluster — "Paris" ends up near "France," "London" near "England," "happy"

near "joyful."

Stop and notice something extraordinary. The embedding space is not designed. Nobody tells the network that "Paris" and "France" should be near each other. The training objective — predict the next token correctly — implicitly forces the network to discover a geometric structure in which related tokens are nearby, because nearby tokens produce similar predictions. The famous result that "king − man + woman ≈ queen" is a side-effect: the geometry of meaning emerges from the geometry of co-occurrence, and the network gets there by gradient descent on next-token loss. We did not design this.

We pointed an optimizer at a corpus and the geometry fell out.

The thing nobody mentions:

tokenization is one of the most consequential choices in a model, and almost nobody thinks about it. Wrong vocabulary in your domain — Indonesian street names, organic chemistry, programming languages — becomes a permanent capability ceiling. You can pre-train all you want; if your tokenizer can't represent the input cleanly, the model can't learn to predict it cleanly. People have pre-trained billion-parameter models on Indonesian text for years without noticing that their tokenizer was splitting common Indonesian street prefixes into four pieces while splitting

English ones into one. Performance on every Indonesian benchmark suffered, and nobody could find the bug because it wasn't a bug — it was the vocabulary they had downloaded from a previous paper.

The fix is to design the vocabulary deliberately, on representative data, before pre-training. Most teams skip this step. They pay for it forever.



## Chapter 3


### How a Network Speaks


We've turned text into vectors. We've optimized the network's parameters. Now we need to close the loop: how does the network turn its internal representations back into text?

The answer is, in spirit, the inverse of how it reads. The network produces, for each position in the sequence, a vector of numbers — one per token in the vocabulary — called the logits. These are unconstrained real numbers. To turn them into a probability distribution over the vocabulary, we apply softmax:

exponentiate each logit, then divide by the sum of all exponentiated logits. The result is a probability distribution over the vocabulary that sums to one, where each token's probability is proportional to e raised to its logit.

Softmax has two properties that matter.

First, it is differentiable, which means gradients can flow back through it during training. Second, it is monotonic in the logits — the highest logit always gets the highest probability — but the distribution is soft. Close logits map to similar probabilities, far logits to very different ones. The "softness" lets the model express degrees of confidence rather than committing to a single answer, which is what makes the gradient signal useful.

The training objective falls out naturally.

Given an input sequence, the network produces a probability distribution over the next token. The training data tells us what the next token actually was. We compute the negative log-likelihood of the correct token under the predicted distribution: −log P(correct token).

Minimizing this loss, summed over a corpus of trillions of tokens, is what we mean by "training a language model."

This is the entire pre-training objective.

There is nothing else. Predict the next token. Repeat over a trillion tokens of text.

Adjust the parameters by gradient descent. After enough compute, the network will have absorbed an unreasonable amount of the structure of human language, world knowledge, reasoning, and dialog. The fact that this works — that next-token prediction at scale produces a model that can write essays, debug code, and reason about physics — is the central empirical surprise of modern AI. We did not predict it. We do not fully understand it. We will return to it in Act III.

For now, just notice: the prediction is a probability distribution. To actually produce text, we have to sample from it.

The simplest strategy is greedy: always pick the highest-probability token. This is deterministic and often dull. The model gets stuck in repetitive loops because it always takes the safest path; once it commits to a phrase, it tends to keep committing.

Sampling strategies fix this. Temperature scales the logits before softmax — divide by a temperature t. Low temperatures (t < 1) sharpen the distribution: high-probability tokens get even higher probabilities, low-probability ones vanish.

High temperatures (t > 1) flatten it: more variety, more risk of incoherence. Top-k sampling restricts the choice to the k most probable tokens; top-p, also called nucleus sampling, restricts it to the smallest set of tokens whose cumulative probability exceeds p. These are heuristic dials that let you trade off coherence and creativity.

The thing nobody mentions: the choice of sampling strategy is part of the deployed system in ways that most people don't appreciate. The same network with greedy decoding feels stale; with high temperature, it feels unhinged; with top-p around 0.9 and temperature near 1, it feels alive. None of these regimes was trained into the model — the model was trained only to produce a probability distribution.

The character of the output, the personality of the deployed AI, is partly a sampling-time decision. This is one of many places where the deployed system is meaningfully different from the trained network. Act V will cover the rest.

We have the apparatus. We can read; we can optimize; we can speak. We have a sequence model — implied above, made explicit now — that processes one token at a time, threading a hidden state forward, predicting the next. This was the dominant architecture for language until 2017. It worked, for short sequences. For long ones, it fell apart in a specific way, for specific reasons.

In Act II we'll see why it had to die.

End of Act I.


## The Routing Insight


From the failure of recurrence to the block that ate the field.

Where we left off

In Act I we built the apparatus. We learned to chop language into tokens, project them into embedding space, and predict the next token with a softmax over the vocabulary. We met the recurrent neural network: a sequence model that reads one word at a time, threading a hidden state through time the way you thread a string through beads.

The recurrence was elegant. It was also a trap.

This act is about the trap, the people who fell into it, and the way out. By the end you will be able to describe, from memory, every component of a

Transformer block — and, more important, you will be able to say why each



component had to exist. That second thing is the only kind of understanding that survives.

## Chapter 4


### The Puzzle of Long Sentences


Let me describe the failure of recurrence honestly, because most introductions to the Transformer describe it carelessly.

A recurrent network reads "The cat that the dog chased was tired." It begins with "The," updates a hidden state, reads "cat,"

updates again, then "that," "the," "dog,"

"chased," "was," and finally "tired." To predict "tired" — or rather, to know that cat is the thing that is tired, not dog — the network has to keep the information about "cat" alive in its hidden state across six updates. Each update is a matrix multiplication followed by a nonlinearity.

In principle, the network can learn to preserve "cat" through six steps.

In practice, it doesn't.

The gradient that tells the network to preserve "cat" has to travel backward through six matrix multiplications during training. Either the gradient explodes (when those matrices have eigenvalues above one) or vanishes (when they're below one). Almost nothing has eigenvalues exactly equal to one, so almost everything fails. The network learns short-range dependencies easily and long-range dependencies almost never.

LSTMs and GRUs were the first patches.

They added little gates — additive paths that information could flow along without being mangled by a matrix multiply at every step. The gates helped. They turned a six-step problem into a forty-step problem. Machine-translation systems in 2016 could handle sentences. They could not handle paragraphs.

There was a deeper issue, and it was not about memory. It was about parallelism.

To process the seventeenth word in a recurrent network, you need the hidden state from the sixteenth word. You cannot compute step seventeen before step sixteen has finished. The whole architecture is a chain. You cannot use a thousand GPUs to read a thousand-word document in parallel; you can use one

GPU, sequentially, a thousand times.

Around 2016 the field was holding two contradictory beliefs. The first: deep learning works because we can throw bigger models, more data, and more compute at problems. The second: the dominant architecture for language is one that fundamentally cannot use more compute. You can buy more GPUs, but the recurrence forces you to use them one at a time.

Several research groups noticed the contradiction. They also noticed something else. The translation systems that worked best in 2016 were the ones that bolted attention onto the side of an

RNN. The encoder would produce a hidden state for every word in the source language; the decoder, while generating the translation, would compute attention weights over those encoder states — pointing at the parts of the source it was currently translating. Attention was a side-channel that let the decoder skip the recurrence and look directly at any position it wanted.

The dangerous question was already in the air. If attention is what's actually doing the work, why do we need the recurrence at all?

In June 2017, a paper from Google answered: we don't. It was titled "Attention

Is All You Need." The architecture it proposed — the Transformer — has not been meaningfully replaced in the eight years since. Nothing else has come close.

The rest of this act is about why.



## Chapter 5


### Attention


Attention is a soft, learnable lookup.

Three of those four words are doing real work; let me unpack them.

Imagine a database. Each row has a key and a value. You have a query — a question you want the database to answer. To answer it, the database compares your query to every key, scores how well each one matches, and returns the values weighted by those scores. If your query matches one key perfectly, you get back that one row's value. If it half-matches several keys, you get back a blend.

That's attention. The clever part is that the queries, keys, and values are all learned.

Take a sentence. Each word, after embedding, is a vector. The model has three small weight matrices — call them

W_Q, W_K, W_V. It runs each word's embedding through each matrix to produce a query vector, a key vector, and a value vector for that word. So every word now plays three roles: it has a question it's asking (the query), an advertisement of what it has to offer (the key), and the actual content it would contribute (the value).

Then, for each word, you compare its query against every word's key — including its own. The dot product of the query and a key is high when they "match,"

whatever match has come to mean during training. You softmax these scores so they sum to one, and you use them to take a weighted average of the value vectors.

Each word now has a new representation that is a blend of the value vectors of the words it most wanted to listen to.

The formula is the sanity check, not the idea:

Attention(Q, K, V) = softmax(QKT / √d) · V

Read it left to right. QKT is the matrix of all query-key dot products: every query against every key. The √d division is a numerical trick. As you make the vectors longer, dot products get bigger; the softmax saturates and gradients die.

Dividing by √d (where d is the dimension of the keys) keeps the scores in a reasonable range. Softmax turns scores into probabilities. Multiplying by V does the lookup.

What does this mean during training?

Every word in every sentence emits a query that says what it's looking for, a key that says what it has on offer, and a value that says what it actually contributes.

Through gradient descent, the network discovers that "her" should query for nearby female nouns, that "Paris" should query for "France"-flavored context, that the period at the end of a clause should attend to the verb. Nobody told it to. The gradient told it to.

And here is the thing nobody mentions, the surprise that locks attention into your memory:

Attention is permutation-equivariant. It does not know which word came first. If you shuffle the input words, you get the same output, just in shuffled order.

This is not a bug. It is the deepest property of the architecture. A recurrent network bakes order into its bones — the meaning of "step seven" is "the thing that comes after step six." A Transformer has no such commitment. Sequence is something we add on top, optionally, with positional encodings (Chapter 7). The architecture has no opinion about whether you are reading text or staring at a bag of pixels or processing a set of records in a database. Most of modern

ML's flexibility traces to this one fact, and almost no introduction to attention mentions it.



## Chapter 6


### Many Heads


There is a question that should be bothering you. If a query, a key, and a value are each just vectors, then for each word the model computes one query and asks one question. Sentences are richer than that. The word "bank" might want to ask, simultaneously, am I a financial institution or a riverside?, what verb governs me?, am I the subject or the object?, is this a metaphor?

You cannot ask four questions with one query.

The fix is so simple it feels like cheating.

You don't have one set of weight matrices

W_Q, W_K, W_V. You have eight. Or sixteen. Or ninety-six. Each set produces its own queries, keys, and values, runs its own attention computation in its own small subspace, and produces its own output. You concatenate the outputs of all heads and project them back to the original dimension with one final matrix.

That's multi-head attention. The model gets to ask many questions in parallel, and each head is free to learn a different kind of question.

What do the heads actually learn? When researchers looked, they found something striking. Different heads specialize. One head learns to be a syntactic pointer — it makes verbs attend to their subjects.

Another learns to be a copy operation — it makes "London" attend to the previous mention of "London." Another learns to be a coreference resolver. Another, sometimes, learns nothing at all and can be pruned without hurting performance.

There is no supervision for any of this.

Nobody tells head 7 to be a syntactic pointer. The training objective is just "predict the next token correctly," and the network discovers, by gradient descent over billions of examples, that having one head act as a syntactic pointer is useful for predicting next tokens. The specialization is an emergent division of labor in a system that was, mathematically, fully symmetric to begin with.

The cost is not free. Each head needs its own set of weight matrices, so multi-head attention has more parameters than single-head. But the per-head dimension is usually small (the model's hidden dimension divided by the number of heads), so the total parameter count of attention stays in the same range. You get parallelism in kinds of question without paying much for it.

The thing nobody mentions: in the original 2017 paper, they used eight heads of dimension 64, totaling 512. Modern frontier models use 96+ heads. But in 2023 a different idea took over for inference efficiency — Grouped-Query Attention, where many query heads share a single key/value pair (Act V). The reason: at inference time, you have to store all those keys and values in the KV cache, and the cache is the dominant memory cost. So we keep many query heads (cheap, only used during forward pass) but share their keys and values (expensive, stored across the entire generation). This is the kind of asymmetric trick that wins when you have to actually deploy the thing.



## Chapter 7


### Positional Encoding


We left a debt at the end of Chapter 5. Attention does not know which word came first. If we feed it a sentence, it will treat the sentence as a bag of words.

We have to repay this debt before we can build a working model.

The repayment looks suspicious at first.

We compute a vector for each position — position 0, position 1, position 2 — and we add it to the corresponding word's embedding. Just add. Vector addition.

Stop and notice how strange this is. We have a vector that means "cat" and a vector that means "position three," and we add them together to make a vector that means "cat at position three." There is no reason to expect this should work. We are conflating two completely different kinds of information by putting them in the same numerical bucket.

It works anyway. The model figures it out.

Here is the partial explanation. The embedding space has many dimensions — typically 512, 1024, or 4096. The word information and the position information end up using different subspaces of the embedding. The model learns, during training, that some directions in the embedding space mean "lexical content"

and other directions mean "position."

When attention computes dot products, it can attend based on either signal. A head that wants to look at "the verb regardless of where it is" will use the lexical subspace; a head that wants to look at "the previous word" will use the positional subspace. Addition in a high-dimensional space is, statistically, almost the same thing as concatenation, as long as the space is big enough.

The original Transformer used a fixed sinusoidal encoding — a clever choice.

Position p got a vector whose components were sines and cosines of p at different frequencies. The reason: the dot product between the encoding of position p and the encoding of position p+k depends only on k, not on p. The model, in principle, can learn to attend to "the word three positions before me" by using a fixed offset in attention space, regardless of where in the sequence it currently is. This is called relative position information, and it generalizes to longer sequences than the model was trained on.

Modern models mostly use Rotary

Position Embeddings (RoPE), which encode position by literally rotating the query and key vectors by an angle proportional to the position. The dot product between rotated vectors then depends only on the difference of angles, which is the difference of positions. This gives you relative positions for free, with better extrapolation to long sequences. RoPE is what every serious model uses now —

Llama, Qwen, DeepSeek, Mistral.

There are also models that learn position embeddings from scratch — every position gets a learned vector, like another token in the vocabulary. This works well if you never need to extrapolate beyond the training length. It fails terribly the moment you do.

The thing nobody mentions: for years, it was an open question whether positions even need to be encoded explicitly. Causal attention (the kind used in GPT-style decoders) attends only to previous positions, so the attention pattern itself contains positional information — position three can attend to positions zero, one, and two, which is different from what position five can do. Some researchers have found that decoder-only models with no positional encoding at all still work, because the causal mask leaks position.

This is the kind of empirical curiosity that makes ML feel less like engineering and more like ecology — the field is still discovering what its own creations can do.



## Chapter 8


### Residuals and LayerNorm


We have attention. We will need to stack many attention layers, because one layer of attention can route information once but cannot reason about complex compositions. Stacking is what gives us depth, and depth is what gives us power.

Stacking, as we learned in Act I, is exactly what kills neural networks.

When you stack twenty layers of any operation — attention or anything else — the gradient that needs to flow back through twenty layers gets multiplied by twenty Jacobians. Even if each Jacobian is reasonable, their product is not. Gradients vanish. Training stalls. The deep network performs worse than a shallow one.

There are two mechanisms in a

Transformer that prevent this from happening. Both are simple. Neither is obvious until you've seen what training is like without them.

The first is the residual connection. After each sublayer (attention, then later the feed-forward network), instead of replacing the input with the sublayer's output, we add them: y = x + f(x). The sublayer learns to compute a correction to its input, not to replace its input. The forward path always has a "highway" — a route along which information can flow without being touched by any sublayer.

The consequence for gradients is profound. The Jacobian of x + f(x) with respect to x is I + ∂f/∂x, where I is the identity. Multiplying twenty such

Jacobians together gives you something like (I + small)^20, which still has the identity as its dominant component. The gradient still has a route home. You can stack a hundred layers, and the gradient still gets back to the input.

There is a deeper way to understand residuals. They mean the network's representation is iteratively refined. Each block reads the current representation, decides what should be added to it, and adds it. The representation never restarts.

The first block produces a slightly better representation; the second produces a slightly better one than that; the hundredth produces the final one. The model's reasoning is a long, continuous polishing of a single vector per token, not a series of fresh starts.

The second mechanism is Layer

Normalization. After (or before) each sublayer, we normalize the activations of each token to have zero mean and unit variance, then apply a learned scale and shift. The reason is again about training stability. Without normalization, activations drift in scale during training — some grow, some shrink — and the optimizer has to constantly readjust learning rates per layer. With normalization, every layer's activations have a known scale. Gradients are well-behaved.

Why LayerNorm and not BatchNorm?

BatchNorm normalizes across the batch dimension; LayerNorm normalizes across the feature dimension. For sequences of variable length, BatchNorm is awkward — different positions have different sequence-length context. LayerNorm doesn't care about the batch or the sequence length. Each token is normalized independently, and the math just works.

There is an architectural decision here that the field took a few years to settle.

Should LayerNorm come before the sublayer (pre-norm) or after the residual addition (post-norm)? The original 2017 paper used post-norm. It worked, but it required careful learning-rate warmup; otherwise training was unstable. Around 2019, people started using pre-norm, and the warmup requirement disappeared.

Modern Transformers all use pre-norm: x → LN → attention → + → x', then x' → LN → FFN → + → x''. The residual highway is unbroken; the LayerNorm is inside the branch that does the work.

The thing nobody mentions: the combination of residuals and normalization is what makes depth cheap.

Without residuals, even with LayerNorm, gradients eventually vanish. Without

LayerNorm, even with residuals, training is brittle. Together, they are why we can stack 96 Transformer blocks and have the thing converge. Almost every "deep"

architecture proposed since 2015 —

ResNet, Transformer, Mamba, modern

CNNs — uses both. They are not optional.

They are the price of admission to being deep.



## Chapter 9


### The Transformer Block


We now have all the pieces to build one Transformer block.

A block takes a sequence of vectors in and produces a sequence of vectors out, of the same shape. Inside, there are exactly two sublayers, each wrapped in a residual connection and a LayerNorm.

The first sublayer is multi-head attention. We've already built it. It lets each token gather information from every other token. After this sublayer, every token's representation has been enriched with relevant context from the rest of the sequence. The residual ensures it hasn't lost what it already had.

The second sublayer is a feed-forward network — sometimes called an MLP, or an

FFN, or a "position-wise feed-forward." It is two linear layers with a nonlinearity in between, applied independently to each token. No mixing across tokens; the feed-forward processes each position alone.

Why the FFN? The blunt answer:

attention can mix and match information across positions, but each token's processing needs to be a non-linear function of its own enriched representation. Attention is linear in the values (it's just a weighted sum). Without the FFN, the entire Transformer would be a deep linear network with some softmax mixing — which collapses, mathematically, to a much weaker model. The FFN gives the Transformer its non-linearity, its capacity to compute, its expressiveness.

There is a less blunt answer, and it is more interesting. Some recent work treats the FFN as a key-value memory. The first linear layer projects each token into a high-dimensional space (typically 4× the model dimension); each direction in that space corresponds to some pattern the network has learned to detect. The activations after the nonlinearity tell you which patterns are "active" for this token.

The second linear layer maps active patterns back to specific output directions. The FFN is, plausibly, where the model stores most of its factual knowledge — patterns like "the capital of

France is Paris" become specific direction triggers in the FFN.

The block, in pseudocode (pre-norm convention):

y = x + Attention(LN(x)) z = y + FFN(LN(y))

That's it. Two sublayers, two residuals, two LayerNorms. The block has roughly 12d² parameters where d is the model dimension — most of them in the FFN, because the FFN's hidden dimension is 4d.

A "Transformer" is just this block, stacked. GPT-3 stacks 96 of them. Llama-3 70B stacks 80. The block is the same; the count varies. Each block reads the current representation, refines it, passes it on.

After 96 blocks, the representation has been polished enough that a final linear layer can read off the next-token probabilities.

Stop and notice something extraordinary. We have built a model that, on the surface, has no recurrence, no convolution, no special structure for sequences. It is a stack of identical blocks, each of which performs a soft routing over the sequence and a per-token non-linear transformation. There is no part of this architecture that "knows" it is processing language. The same architecture, with different inputs, processes images, audio, video, protein sequences, and chess positions. We will come back to this in Act

VII.

The thing nobody mentions: the

Transformer block is, plausibly, the most important architectural unit invented in deep learning's modern era. It is taught in courses as one architecture among many; it has been one architecture among many for some time. But when scaling laws (Act

III) entered the picture, it became clear that the Transformer scales more cleanly with compute than anything else we've tried. A whole research community has spent eight years trying to find a successor. Mamba is the most credible challenger; it is still not the default. The block has refused to be replaced.



## Chapter 10


### Encoder, Decoder, Both, Neither


The original 2017 paper proposed the

Transformer for machine translation.

Translation needs two stages: read the

French sentence (encode), then write the

English one (decode). So the original architecture was an encoder-decoder: a stack of N blocks that processes the input, then a separate stack of N blocks that generates the output.

The decoder differs from the encoder in two ways. First, it has a causal mask. When decoding, you generate one token at a time, and each token can only attend to previous tokens — never to future ones, because the future tokens don't exist yet.

The mask is implemented as a giant upper-triangular matrix of negative infinities added to the attention scores before the softmax. After softmax, the upper-triangle becomes zero, and a query at position three can attend only to positions zero, one, two, three.

Second, the decoder has cross-attention.

In addition to attending to previous decoder tokens (self-attention with causal mask), each decoder token also attends to the encoder's output. Cross-attention is just attention where the queries come from one stream (the decoder) and the keys and values come from another (the encoder). It's the channel through which the decoder "reads" the source sentence while it writes the translation.

This is a beautiful design. It also turned out to be more architecture than necessary.

Within two years, two simpler variants emerged. They have eaten the field.

The first variant is encoder-only. BERT, in 2018, said: what if we just take the encoder, train it on a different objective, and use the resulting representations for any task? The objective they chose was masked language modeling — randomly mask out 15% of the input tokens and ask the model to predict them. This forces the model to use bidirectional context.

Position three's representation depends on the entire sentence, including positions four, five, and six. There is no causal mask; every token sees every other token.

BERT also added a small architectural trick: a special [CLS] token prepended to every input. The [CLS] token's only job is to aggregate information from the whole sequence into a single vector that downstream classifiers can read. The model learns, through training, to use that token as a sentence-level summary. Add a logistic regression on top of the [CLS] vector and you have a sentiment classifier.

Replace it with a different head and you have a question-answering system. BERT's architecture itself was unchanged across tasks; only the head changed.

For three years, BERT and its descendants dominated language tasks that understood text — classification, retrieval, named-entity recognition. It was the standard.

The second variant is decoder-only. GPT, also from 2018, said: what if we just take the decoder, drop the cross-attention (so it has nothing external to attend to), and train it to predict the next token? You get a model whose sole capability is autoregressive generation: given a prompt, produce the most likely continuation, one token at a time.

This sounds like a worse idea than BERT.

Bidirectional context is more informative than causal context. Why throw it away?

The reason GPT won is that "predict the next token" is a strictly more general objective than "fill in the blank." If you can predict the next token in any context, you can do classification (just frame the task as a question whose answer is a token), translation (predict the translated tokens given the source), summarization (predict the summary tokens), reasoning (predict the chain-of-thought tokens), code generation, and so on. There is no task that cannot be cast as next-token prediction on a suitable prompt. BERT was good at understanding; GPT was good at everything that can be expressed as text generation, which is almost everything.

By 2022 the field had effectively collapsed onto decoder-only

Transformers. Every frontier language model since — GPT-4, Claude, Gemini,

Llama, DeepSeek, Qwen — is decoder-only. Encoder-decoder survives in a few specific applications (translation, some forms of summarization, T5-family models), and encoder-only survives mostly in embedding models for retrieval. But the centerpiece, the architecture that "language model" now refers to, is the decoder-only Transformer.

The thing nobody mentions: the field's convergence on decoder-only is partly an architectural decision and partly an economic decision. Decoder-only models can do everything encoder-decoder models can, and they can serve any task with a single deployed model and a different prompt. You don't have to fine-tune separate models per task. You don't have to maintain different inference pipelines. One model, one API, infinite tasks. Once that became technically possible, the encoder-decoder split was a maintenance burden no one wanted to pay. The Transformer didn't just win on quality. It won on operational simplicity.

Closing: The Block That Ate The Field

Let me end this act with a confession that

I think most ML educators avoid.

We have spent seven chapters building up the Transformer. We have explained, with as much honesty as I can muster, what each component does and why it had to exist. We have not explained, because nobody can, why this specific architecture scales as well as it does.

When the 2017 paper was published, it was understood as a clever architecture for translation. It was not understood as the foundation of a new technology. The authors did not predict, in their abstract, that this block — stacked deeply enough, trained on enough data, and aligned with enough human feedback — would, by 2026, be writing this sentence.

We will see in Act III what happened next. Researchers tried scaling the

Transformer up — bigger model, more data, more compute. The loss kept going down. They tried bigger. The loss kept going down. They derived equations describing exactly how the loss would fall as a function of how much they spent.

Those equations held over six orders of magnitude. The Transformer turned out to be, for reasons we still do not fully understand, an architecture that converts compute and data into capability with a fidelity nothing else has matched.

What you have learned in this act is the substrate. What you will learn in the next act is what happens when you pour an unreasonable amount of compute into it.

The block is the same. The world that built around the block is what changed.

End of Act II.


## The Scaling Discovery


When the field learned to forecast capability from compute.

Where we left off

In Act II we built the Transformer. We took a stack of identical blocks, each performing soft routing followed by a per-token nonlinear transformation, and we gave it the ability to read sequences of arbitrary length and produce a probability distribution over the next token at every position. We claimed, at the end of that act, that the Transformer turned out to scale unreasonably well — better than any architecture before it, better than any architecture proposed since. We did not explain what that meant.

This act is what it meant.

By the end you will be able to describe, from memory, why the field's center of gravity shifted from algorithmic



cleverness to compute scale; what Kaplan and Hoffmann actually showed; why GPT-3 was the moment everyone took notice; what emergent abilities are and why people argue about whether they are real; and why grokking is the strangest open problem in deep learning. These are the load-bearing ideas of the modern era.

Every conversation about AI capability for the next ten years will reference at least one of them.

## Chapter 11


### The Empirical Surprise


Here is the situation in 2018. The

Transformer has been published.

People are using it for translation, where it is better than the LSTM-based systems it replaces. It is also being applied to other language tasks — classification, question answering — where it works fine. There is no particular sense, at this point, that anything special is happening. The

Transformer is one architecture among several. Convolutional networks dominate vision. The general lesson of deep learning, accumulated over five years, is more data and bigger models help, up to a point, and then they stop helping.

OpenAI does something simple. They take the Transformer decoder, throw away the encoder, throw away cross-attention, and train it on a large corpus of internet text with one objective: predict the next token. They call it GPT — Generative Pre-trained Transformer — and they release a paper showing it does well on a few language benchmarks. The model has 117 million parameters. Nobody outside the field notices.

A year later they release GPT-2. Same architecture. Bigger: 1.5 billion parameters.

More data. More compute. The loss is lower. The benchmarks are better.

Generated text is suspiciously coherent.

They publish the model in stages over fear of misuse, which seems either prescient or paranoid depending on who you ask. Most people in the field assume this is the end of the curve. Returns are diminishing.

In 2020 they release GPT-3. Same architecture. Bigger: 175 billion parameters, more than a hundred times

GPT-2. Trained on hundreds of billions of tokens. The paper is titled "Language

Models are Few-Shot Learners," and the central claim is that this model can do tasks it was never trained on, by being given a few examples in the prompt.

Translation, summarization, arithmetic, code generation, analogical reasoning — none of these were training objectives.

The model does them because they are subsumed by the next-token prediction objective applied at sufficient scale.

The loss kept going down. Nobody had told it to stop.

Take a moment to feel how strange this is. The conventional wisdom in machine learning, accumulated over decades, was that models overfit: train them too long or make them too big and their training error keeps falling but their test error stops falling and starts to rise. There was supposed to be a sweet spot. GPT-3 had blown past every supposed sweet spot. It was not just bigger than what came before. It was bigger than what was supposed to be useful. And it was qualitatively better in ways no one had predicted.

This is the empirical surprise. The

Transformer, trained on next-token prediction, did not behave like other architectures in other domains. It kept improving as you fed it more compute.

The improvement was not random — it followed a precise mathematical pattern.

The pattern had a name. It was called a scaling law.



## Chapter 12


### Scaling Laws


In 2020, a team at OpenAI led by Jared

Kaplan published a paper called "Scaling Laws for Neural Language

Models." It is one of those papers that is worth reading not because it is technically deep but because it changed what the field thought it was doing.

The setup is simple. Train a Transformer language model on a fixed dataset. Vary three things independently: the number of parameters in the model (call it N), the number of tokens you train on (call it D), and the total compute budget (call it C).

Plot the test loss as a function of each.

What you find — what they found — is that loss is a power law in each of these.

A power law looks like this:

L = a · N⁻ᵇ + irreducible

Loss equals some constant divided by N raised to some power. On a regular plot it looks like exponential decay. On a log-log plot — log loss against log compute — it looks like a straight line. The slope of that line is the exponent. The exponent is small — typically around 0.05 to 0.1 — but it does not decay. It does not bend. As you scale, the loss falls along the same line, with the same slope, for as far as you can extend the experiment.

This is empirical. There is no theoretical derivation. People have tried. Some toy models suggest reasons why power laws should appear in high-dimensional learning, but no derivation predicts the specific exponents Kaplan measured. The scaling law is a fact about Transformers and language data. It works, and we do not know exactly why.

The implication, however, was clear, and it was earthquake-shaped.

If loss is a power law in compute, with no obvious end, then the question of how good a model is becomes a question of how much compute you have. You can predict, before training, how much compute it would take to reach any given loss level. You can budget against a target.

You can estimate, with some confidence, how much better a model trained on ten times more compute would be. Suddenly, capability is forecastable.

Three labs took this seriously. OpenAI was already doing it. Anthropic and

DeepMind started doing it. The next few years of frontier AI development followed the same recipe, with minor variations:

take the Transformer, scale it up by a known factor, train it on a known amount of data, project the loss before you start, and measure whether you hit the projection. Almost always, you hit it. When you didn't, it was because of a bug, a data issue, or a hardware failure — not because the law had broken.

The law has not broken. As of this writing, the latest frontier models — five orders of magnitude more compute than

GPT-2 — still sit on the line. The line has bent slightly in places, mostly because the dataset ran out of high-quality unique tokens, but the underlying relationship has not failed.

The thing nobody mentions: scaling laws were not really an academic discovery.

They were the discovery that turned ML from a research field into an industrial field. Before scaling laws, training a frontier model was a research project — uncertain, full of failed runs, depending on novel architectural insights. After scaling laws, it became closer to a manufacturing problem: estimate the cost, secure the compute, run the recipe, ship the model.

Anthropic was founded on a thesis that included scaling laws. OpenAI's transition from research lab to product company was paid for by scaling laws. Every multibillion-dollar AI investment since 2020 is, in some sense, a bet on the continuation of a power law nobody fully understands.



## Chapter 13


### The Chinchilla Correction


There is a subtlety the Kaplan paper got wrong, and the field believed the wrong thing for two years before someone corrected it.

The question is: given a fixed compute budget C, how should you spend it? You can train a small model on a lot of data, or a big model on less data, or anything in between. C is roughly proportional to N times D — number of parameters times number of training tokens. If you have a million dollars of compute, you can buy more parameters or more tokens, but not both.

Kaplan's paper concluded that you should buy mostly parameters. Their analysis suggested that for a given compute budget, you should train the biggest model your compute allows, and run it for relatively few tokens. The community took this at face value. GPT-3,

MT-NLG, Gopher, PaLM — all trained with this assumption. The result was a generation of models that were enormous (hundreds of billions of parameters) but undertrained (trained on a few hundred billion tokens, when their parameter count suggested they could absorb trillions).

In 2022, a team at DeepMind led by

Jordan Hoffmann published a paper titled "Training Compute-Optimal Large

Language Models." They redid the experiment more carefully. Instead of varying N and D somewhat independently, they ran a large grid of model-size and dataset-size pairs at fixed compute budgets, and asked which pair produced the lowest loss for that budget. The answer was different from what Kaplan had concluded.

The compute-optimal recipe, according to Hoffmann, was: scale parameters and tokens roughly equally. If you double your compute budget, you should double both your parameter count and your training tokens, not put it all into parameters. They demonstrated this by training a 70-billion-parameter model called Chinchilla on 1.4 trillion tokens — significantly more tokens per parameter than GPT-3 had used — and showing that Chinchilla outperformed

Gopher, a 280-billion-parameter model, on essentially every benchmark, while using less compute.

This was the Chinchilla correction. It said, in effect: every frontier model trained between 2020 and 2022 was undertrained. They had the wrong shape.

The field updated. Llama, the open-weights family that Meta released in 2023, was Chinchilla-pilled — relatively modest parameter counts trained on enormous token budgets. Llama-3, in 2024, pushed even further past Chinchilla-optimal: 70 billion parameters trained on 15 trillion tokens, far more tokens than Chinchilla would have suggested were optimal at that scale. The reason for going past

Chinchilla-optimal is economic: at inference time, smaller models are cheaper to serve, and you would rather pay slightly more compute during training to get a smaller model that costs less every day for years afterward. Chinchilla-optimal minimizes training loss at fixed training compute. It does not minimize deployed cost. The two objectives diverge.

The thing nobody mentions: the

Chinchilla paper is one of the rare instances in modern ML where a careful empirical correction overturned widely-held belief and immediately changed practice. Most papers do not do this. Most papers add to the noise. Hoffmann's paper subtracted from it. If you want to learn how to read ML papers well, read the

Chinchilla paper, then read three randomly selected papers from any 2024 conference. The difference in epistemic quality will teach you what to demand.



## Chapter 14


### The Phase Transition


Scaling laws say loss falls smoothly with compute. They say nothing about capabilities. Capability is not the same as loss. A model with low loss is good at predicting next tokens; whether it can solve a multi-step word problem is a separate question, even if loss is the only thing the optimizer cares about.

Around 2022, papers started appearing with a strange claim. Some capabilities, the claim went, do not improve smoothly with scale. They are absent at small scale, and then, past a certain compute threshold, they appear. The model becomes capable of three-digit multiplication, or analogical reasoning, or following multi-step instructions, at a specific size — not earlier, not gradually.

This was called emergent abilities. The most cited paper, by Wei and collaborators, presented dozens of tasks where the capability curve looked flat for a long time and then jumped. The paper became influential immediately. People interpreted it to mean that further scaling would unlock further sudden capabilities, in unpredictable ways. There were essays speculating about what would emerge at the next order of magnitude. The argument was sometimes deployed as a reason for concern about future systems:

if capabilities appear discontinuously, you cannot anticipate them.

In 2023, a paper from Stanford — "Are

Emergent Abilities of Large Language

Models a Mirage?" by Schaeffer, Miranda, and Koyejo — argued that the discontinuities were partly a measurement artifact. If you measure a task using exact-match accuracy, and the task requires a long sequence of correct steps, then you will see a sharp jump from "always wrong" to "sometimes right" at the scale where the per-step accuracy crosses some threshold. The underlying capability — per-step accuracy — is improving smoothly all along. The emergence is in the metric, not the model.

This deflated some of the original claims.

It did not deflate all of them. There are tasks where, even on smooth metrics like log-likelihood of correct continuation, you see sharper-than-power-law improvements past certain scales. Some genuine non-linearity remains. The current consensus, as far as there is one, is: yes, there are jumps, and the original paper overstated their sharpness, and both of these claims are compatible. Both are true, in a way that depends on how you measure.

This is a perfectly normal scientific situation, but it is also a useful lesson about the field. ML benchmarks are not natural quantities like temperature or weight. They are constructed, often hastily, often by the same teams that train the models. A capability that looks emergent in one metric can look smooth in another. A capability that looks emergent in zero-shot can look smooth with chain-of-thought. The shape of the curve depends on the shape of the lens.

The thing nobody mentions: the question of what causes phase transitions in deep learning, when they happen, is wide open. We do not have a theory that predicts them. We have empirical observations of curves bending sharply.

We have informal arguments that involve thresholds in the model's internal representations crossing some critical value. We do not have anything like the theory of phase transitions in physics, where you can write down an order parameter and a critical exponent and make predictions. ML phase transitions are observed. They are not understood.



## Chapter 15


### Grokking


There is an experiment that, when you first see it, breaks your model of how neural networks work.

In 2022, a team at OpenAI published a short paper called "Grokking:

Generalization Beyond Overfitting on

Small Algorithmic Datasets." The setup is small: a tiny Transformer trained to perform modular arithmetic — for instance, given two numbers a and b, compute (a + b) mod 97. The training set is a few thousand examples. The test set is held out from the same distribution.

What you would expect, knowing standard deep-learning behavior, is the following. The model rapidly drives training loss to zero. Test loss either also falls (if the model generalizes) or stays high (if it merely memorizes). After training loss reaches zero, nothing further happens, because there is no more training signal.

What actually happens is this. Training loss falls to zero quickly, in maybe a thousand steps. Test loss stays around chance — the model is purely memorizing.

You let training continue. Tens of thousands of steps. The training loss is still zero. The test loss is still chance.

Nothing is happening, as far as you can tell. You let it continue.

Then, at some step around a hundred thousand, test loss falls off a cliff. The model starts generalizing. Within a few thousand more steps, it has gone from chance performance to near-perfect generalization. The training data has not changed. The training loss has been zero the whole time. There is no obvious external reason for the transition. The model just suddenly starts working on test data, long after it stopped learning anything new on training data.

This is called grokking. The word — borrowed from Heinlein, meaning "to understand thoroughly" — was chosen by the authors with deliberate strangeness, because the phenomenon is strange.

We do not have a complete theory of grokking. We have partial theories. The leading candidate is roughly this: there are many configurations of weights that achieve zero training loss. Some of them generalize; most do not. SGD, even after training loss reaches zero, continues to drift through the space of zero-training-loss configurations because of weight decay, noise from minibatches, and other regularization pressures. The drift is biased toward simpler, more compressed representations. Most of the time, the network spends a long time in memorizing-but-not-generalizing configurations, then crosses some boundary into a generalizing configuration, and stays there because the generalizing region is more stable under

SGD's continued perturbation.

This story is plausible. It is not yet a theorem. Researchers have shown specific cases where they can characterize the geometry of weight space well enough to predict when grokking will occur. The general theory is incomplete. The phenomenon is robust — people have replicated it across many tasks and architectures — but the explanation is not yet satisfying.

I include grokking in this act because it is the cleanest example we have of the gap between what we observe and what we understand in modern deep learning. We trained a small network. We watched it. It did something strange. We have been studying that strangeness for years. We are not done.

The thing nobody mentions: grokking is probably related to scaling. The mechanism by which a large pre-trained model develops capabilities that small ones do not — the mechanism behind apparent emergence — may be a continuous version of the same phenomenon. Tiny models grok specific algorithmic tasks late in training. Larger models, plausibly, are doing something analogous on much richer task distributions, throughout training. If we ever understand grokking properly, we will probably understand emergence as a corollary. We do not yet understand grokking properly.

Closing: The Architecture as Substrate

Step back and notice what has happened.

In Act II we built the Transformer. We presented it as one architecture among several, distinguished mostly by its parallelism and its ability to handle long-range dependencies. By the end of Act III, the Transformer is no longer one architecture among several. It is the substrate on which all of modern AI is built. The reason is not that the

Transformer is mathematically beautiful, or that it captures some essential structure of language. The reason is that the Transformer, almost uniquely, converts compute into capability along a clean power law, and we have not yet found the bottom of that curve.

This makes the Transformer something stranger than an architecture. It is closer to a resource. You pay compute; you receive capability. The exchange rate is governed by scaling laws. The shape of what you receive is governed by what you train on. The whole apparatus has the feeling of an industrial process, in a way that nothing else in machine learning ever has.

The next acts are about what to do with the apparatus. Act IV asks: how do you take a base model — trained only to predict next tokens — and turn it into something that follows instructions, behaves helpfully, and refuses to do harmful things? Act V asks: how do you serve such a model cheaply enough to be useful? Act VI asks: how do you make it think harder when the prompt demands it? Each of these acts is a different way of cashing in the capability that scaling has produced.

But this act is the inflection point. Before this act, machine learning was a research field. After this act, machine learning was a forecasting problem. The day you internalize that scaling is real, and that it has not yet ended, is the day you stop being surprised by what large models can do. The next surprise will be the day scaling stops working. We have not yet had that day.

End of Act III.


## The Alignment Problem
Turning a base model into something you can talk to.

Where we left off

In Act III we discovered that scaling works.

Pour enough compute into the

Transformer, train it on enough text, and you get a model that knows physics, history, code, every major language, and the structure of human reasoning. The loss keeps falling. The capability keeps rising. We have, at the end of pre-training, an artifact of staggering general competence.

It is also useless.

Take a base model — one that has only been pre-trained, never fine-tuned — and ask it a question. "What is the capital of

France?" The model does not answer. It continues. It might produce: "What is the capital of France? What is the capital of

Germany? What is the capital of Italy?"

because that is the kind of text it has seen on the internet. It might produce a paragraph about the geography of

European capitals. It might produce nothing useful at all. It does not know that you wanted an answer. It does not know that questions are supposed to be answered. It only knows how to predict the next token in a way consistent with internet text, and most internet text that begins with a question is not followed by an answer.

This is the alignment problem in its rawest form. The pre-trained model has knowledge but no instructions. It has capability but no purpose. It will continue any prefix you give it, in whatever direction the training data suggests, regardless of whether that direction is helpful, honest, or harmless.

This act is about how we close the gap.

By the end of it you will be able to describe, from memory, the entire post-training pipeline that turns a base model into something you can talk to: supervised fine-tuning, reward modeling, RLHF, the inner workings of PPO, the magical collapse that produced DPO, the simplification that produced GRPO, the philosophical move that produced

Constitutional AI, and the engineering trick called LoRA that makes all of this affordable.

The history of post-training is short. The first SFT-then-RLHF pipeline that became the modern recipe was published in 2022.



Everything in this act has happened in the last four years. It is the most actively contested part of the field. People who worked on it five years ago disagree with people working on it now. We are still deciding what the right shape is.

## Chapter 16


### Supervised Fine-Tuning


The simplest fix for a model that does not follow instructions is to show it instructions being followed. Take the pre-trained model. Collect a dataset of prompt-response pairs — questions and good answers, requests and good fulfillments — typically written by humans, sometimes by other models, sometimes a mixture. Continue training the model on this dataset, with the same next-token loss as during pre-training.

That is supervised fine-tuning. SFT.

The mechanism is so plain it almost feels like cheating. We are not introducing any new objective. We are not changing the architecture. We are continuing the same training, on a different dataset. The model already knows how to predict the next token; we are just giving it different next tokens to predict.

What changes is the distribution the model believes it is in. A pre-trained model has been steeped in raw internet text, where questions are usually not answered, where contradictions abound, where formatting is inconsistent. SFT shifts the model's expectations. After SFT, when the model sees a question, the most likely continuation, according to its updated weights, is an answer. When it sees an instruction, the most likely continuation is a fulfillment. The model has not learned anything fundamentally new. It has learned to expect a different distribution of text.

SFT works astonishingly well, given how simple it is. A few thousand high-quality demonstrations can transform a base model from a dazed continuator into a credible assistant. ChatGPT's first version was, in essence, GPT-3.5 plus a relatively small SFT dataset plus some reinforcement learning on top. Most of the helpfulness came from SFT. Most of the rest came from what we will discuss next.

The limitation of SFT is also the source of its simplicity. SFT can only teach the model to imitate behaviors it has been shown. If your demonstrations contain mistakes, the model learns the mistakes. If your demonstrations have a particular style, the model adopts that style — even if a different style would have been better.

There is no signal that says "this response was good for this prompt; that response was bad." There is only "this response was the one we showed you, so produce more responses like it." SFT cannot rank. It can only clone.

This is fine when human demonstrations are reliable. It breaks when humans cannot reliably write the right demonstration. The classic case is harmlessness. We can write examples of safe responses to safe queries. We cannot easily write examples of what to do when the query is unsafe — there is no single right response, and humans disagree about what the response should be. SFT cannot capture "produce a response that is safer than this one but more helpful than that one." For that, you need the model to learn from comparisons rather than from demonstrations.

The thing nobody mentions: SFT has a quiet failure mode that nobody discusses in introductory accounts. If your SFT dataset is too small or too narrow, the model can forget things from pre-training.

Instruction-tuning a model on math problems can make it worse at writing poetry. The model is over-fitting to the new distribution and losing the breadth of the old one. The solution is to keep the

SFT dataset broad, to mix in some pre-training data, or to use techniques like

LoRA (Chapter 22) that change the model's behavior without overwriting its weights.

Most public discussion of SFT skips this and presents it as free. It is not free. The bigger your SFT dataset, the more carefully you have to manage what gets preserved.



## Chapter 17


### Reward Models


To go beyond imitation, we need a way to tell the model that some responses are better than others. This is the central insight that turns post-training from a copying exercise into a learning exercise.

Here is the move. Show humans pairs of responses to the same prompt. Ask: which one is better? Collect a dataset of these comparisons. Now train a separate model — usually the same architecture as the language model, sometimes initialized from the language model itself — to predict, given a prompt and a response, what humans would have rated this response.

That separate model is the reward model. It is a function r(prompt, response) that returns a scalar — higher is better. It has been trained on human preferences, and it generalizes from the comparisons it has seen to comparisons it has not seen.

Given any prompt-response pair, it produces a number that is, statistically, what a human rater would have produced.

The reward model is the workhorse of modern alignment. Once you have it, you can score any response your language model produces. You can run the language model, generate a candidate response, ask the reward model how good it was, and use that score to update the language model. The language model becomes a system that produces responses aiming for high reward, where reward is a learned proxy for human preference.

Notice the structure. We have replaced the question "what is a good response?" — which has no closed-form answer — with the question "what response would humans prefer?" — which is also hard, but at least we have data. The reward model is the bridge. It makes preference learnable.

It is also where most of the bugs hide.

A reward model is just a neural network trained on a finite dataset of comparisons.

It generalizes imperfectly. There are responses that look great to the reward model but are, in fact, bad — a phenomenon known as reward hacking.

Examples: a reward model trained partly on length might learn that longer responses are better, regardless of quality.

A reward model trained on responses that contained citations might learn that citations are good, even fake citations. A language model optimized against this reward model will learn to produce long, citation-heavy responses, including fake citations, because the reward model — its only feedback signal — likes them.

The history of RLHF is, in significant part, the history of fighting reward hacking. The standard mitigation is KL regularization: penalize the language model for drifting too far from its pre-fine-tuning distribution. This keeps the model close to behaviors humans actually demonstrated, which limits how much it can exploit the reward model's blind spots. The KL term is a leash. The reward model is the carrot. Without the leash, the carrot leads the model into strange places.

The deeper issue is that the reward model will always be wrong somewhere.

Human preferences are messy, contradictory, and context-dependent. A reward model trained on a billion comparisons still has gaps. The language model, optimized hard enough, will find those gaps. This is not a bug in any specific implementation; it is a structural property of using a learned proxy to optimize against. The technical name is

Goodhart's Law: when a measure becomes a target, it ceases to be a good measure.

Reward models are measures. The optimizer makes them targets. They cease to be good measures. This is the central tension in RLHF, and no one has solved it cleanly.

The thing nobody mentions: the dataset of human preference comparisons is the most expensive thing in the alignment pipeline, and the most delicate.

Annotators have to be trained, calibrated, audited. A noisy or biased preference dataset produces a noisy or biased reward model, which produces a noisy or biased language model. Most of the differences between major frontier models — the ways they feel different to talk to — come from differences in their preference datasets, not from differences in their architectures. The conventional wisdom that frontier labs have similar architectures and different "personalities"

is correct, and the personalities live in the comparison data.



## Chapter 18


### RLHF


We have a base model that has been

SFT-ed. We have a reward model.

We have a KL leash to keep the language model close to its starting distribution.

Now we need an algorithm that takes the language model, generates responses, scores them with the reward model, and updates the language model to produce higher-reward responses.

This is reinforcement learning from human feedback. RLHF.

The standard algorithm — for several years, the only widely-used algorithm — is

Proximal Policy Optimization, PPO. PPO was originally designed for training agents in video games and robot simulations, and the fact that it works for language models is, frankly, slightly accidental. The setup looks like this. The language model is the policy. A response is a trajectory. Each token is an action. The reward model provides a reward at the end of the trajectory, when the response is complete.

We want to update the policy in the direction that increases expected reward, while staying close to the original policy distribution.

The classical policy gradient says: for each trajectory, compute its reward, compute the gradient of the log-probability of the trajectory under the policy, and step in the direction of (reward) × (gradient of log-probability).

This works in principle. In practice it is unstable. Trajectories with high reward dominate; the policy lurches; training breaks.

PPO's contribution is a clipped objective.

Instead of stepping freely in the direction of high reward, PPO clips the update so the policy cannot move too far in any one step. The exact form of the clipping is technical and not worth memorizing. The intuition is: policy gradient descent works, but only if the steps are small enough that the local approximation is valid. PPO enforces that the steps stay small.

This works. It is also a pain. PPO requires you to keep multiple models in memory simultaneously: the policy being trained, a frozen reference policy (for the KL term), the reward model, and a value function — a separate model that predicts expected future reward at each token, used to reduce variance in the policy gradient.

That is four models. Each one needs gradients computed. Memory pressure during PPO is enormous, and the engineering is fiddly. Stable RLHF training is a craft. It is part of why frontier labs have specialized teams.

The whole pipeline can be drawn in a few lines:

SFT model → policy policy + prompt → response reward model + response → score score + KL penalty → loss loss → policy update via PPO

Around this loop, an enormous amount of engineering. Distributed training across many GPUs. Careful learning-rate schedules. Reward-model retraining as the policy shifts. Periodic SFT mixed back in to prevent drift. Each of these is a paper, sometimes several. The high-level picture is clear; the implementation is anything but.

The result, when it works, is what you experience when you talk to ChatGPT or

Claude or Gemini. The model produces responses that are helpful, that follow instructions, that decline to do harmful things, that admit uncertainty when it does not know the answer. Most of these properties are coming from the reward model and the RL loop. SFT got us to "responsive." RLHF got us to "responsive and tuned to human preferences."

The thing nobody mentions: PPO was not designed for language. It was designed for environments with dense rewards, short trajectories, and continuous action spaces. Language is the opposite — sparse rewards (reward only at the end), long trajectories (hundreds of tokens), and discrete action spaces (one of fifty thousand tokens at each step). That PPO works at all is somewhere between a triumph of engineering and a happy accident. The community's insistence on using PPO for language for several years was, in retrospect, a path-dependent mistake — we used it because it was the available off-the-shelf tool, not because it was the right tool. The replacements that follow in this act are simpler precisely because they were designed for the actual problem instead of borrowed from a different one.



## Chapter 19


### The Magical Collapse: DPO


In 2023, a paper called "Direct

Preference Optimization" landed and quietly broke the field's assumption that

RLHF needed to be hard.

The setup is unchanged. We have prompts. We have pairs of responses. We have human preferences over those pairs.

We want to update the language model to produce responses humans prefer. The standard approach is to train a reward model on the preferences, then run PPO against the reward model. DPO's claim is that you do not need the reward model at all.

Here is the core insight, in plain words.

Under the RLHF objective with a KL penalty, the optimal policy — the one that maximizes expected reward minus KL divergence from the reference policy — has a closed-form expression. It is the reference policy reweighted by the exponential of the reward, scaled by the

KL coefficient. This expression has been known in the RL literature for years. What the DPO paper noticed is that you can rearrange this expression to define the reward in terms of the policy: given any policy, you can compute the implicit reward function it would have been optimal under. The reward model is implicit in the policy; the policy is the reward model, in the right coordinate system.

If reward is implicit in policy, then preference comparisons translate directly into a loss function on the policy. You no longer need to train a separate reward model and then optimize against it. You can optimize the policy directly on preference comparisons. The two-stage

RLHF pipeline collapses into one stage.

PPO disappears. The reward model disappears. What remains is a single supervised loss on triples of (prompt, preferred response, dispreferred response), trained with standard gradient descent.

The DPO loss, in spirit:

− log σ(β · log [π(y_w | x) / π_ref(y_w | x)] − β · log [π(y_l | x) / π_ref(y_l | x)])

You do not need to memorize this. You need to memorize what it does. It increases the policy's relative log-probability of the preferred response (y_w, "winner") and decreases its relative log-probability of the dispreferred response (y_l, "loser"), with a temperature β controlling how aggressively. Both probabilities are normalized against the reference policy, which plays the role of the KL leash. The whole thing is a sigmoid binary cross-entropy loss. Everything fits in one objective. One model in memory.

One training run.

The reaction to DPO, when it appeared, was disbelief. The result seemed too good.

People expected hidden costs — instabilities, mode collapse, reward hacking by another name. There were some. Most were tractable. By 2024, DPO and its variants (ORPO, KTO, IPO, SimPO) had become the dominant alignment approach for the open-weights ecosystem. Llama-3, Qwen, Mistral, and most academic-trained models use DPO or a close cousin. RLHF-with-PPO survives at the largest frontier labs because it has been heavily tuned and has slight quality advantages at the margin.

For everyone else, DPO is the default.

The historical lesson is that the right algorithm is sometimes hidden inside the wrong one. RLHF-with-PPO had been the standard for years. The reward-model-then-policy-optimization structure seemed essential. It was not. The algebra had a closed form that made the reward model redundant. Nobody had derived it because nobody had thought to look.

When somebody did, the field changed in a single paper.

The thing nobody mentions: DPO is mathematically equivalent to RLHF only under specific assumptions — that the reward model is fit to convergence, that the KL coefficient is the same, that the policy's reference distribution doesn't drift, and a few others. In practice these assumptions are violated, and DPO and

PPO produce subtly different policies.

There is an active research thread arguing that DPO over-fits to the preference dataset more aggressively than PPO does, because DPO does not explore — it just adjusts probabilities of responses it has already seen. PPO, generating new responses during training, gets fresh signal from the reward model on rollouts.

Whether this matters in practice depends on the dataset and the use case. The honest framing is: DPO is dramatically simpler and almost as good for most purposes, and the cases where it is meaningfully worse are still being mapped.



## Chapter 20


### GRPO and the End of the Value Function
DeepSeek's R1 paper, published in early 2025, contained an algorithmic move that quickly spread across the field: Group

Relative Policy Optimization, GRPO. To understand what GRPO does, we need to remember what PPO does and what is annoying about it.

PPO's machinery includes a value function, sometimes called a critic — a separate neural network the same size as the policy that predicts the expected future reward at each token. The value function exists because policy gradients are noisy: trajectories vary in reward, and you want to know whether a given trajectory was good for its starting state, not just absolutely. The value function provides a baseline. The policy gradient gets multiplied by (reward − value), the advantage, instead of just the reward. This reduces variance and makes training more stable. It also doubles the memory cost, because you have a second network the same size as the first.

GRPO's idea is so simple it sounds wrong. Forget the value function. For each prompt, sample G responses (typically 4 to 16) from the current policy. For each response, compute its reward. The advantage of each response is just its reward minus the average reward of the group. That is the baseline. No critic, no value function, just a group mean.

The whole apparatus that justified the value function — variance reduction — is replaced by averaging within a group. The math works out: a group baseline is a valid baseline as long as it is independent of the response being evaluated. The implementation is trivial. The memory savings are substantial. For the same compute budget you can train a bigger model, or train longer, or both.

GRPO's other contribution is that it works particularly well for verifiable reward domains. If you are training a model on math problems, the reward is binary — correct or incorrect — and you can compute it programmatically. No reward model, no human labels, just a verifier. Sample several attempts, check which ones are right, push the policy toward the right ones and away from the wrong ones. DeepSeek used this recipe to train models that could solve hard math problems by trial and error, without any human-annotated reasoning traces. The model was learning to reason, in part, by self-play against a verifier.

This connects to a broader thread that will dominate Act V and Act VI.

Reinforcement learning with verifiable rewards — RLVR — is the hot frontier of post-training in 2025-2026. It works in domains where reward is cheap and machine-checkable: code (does it compile? does it pass the tests?), math (does the answer match?), formal proof (does the proof verify?). It works less obviously in fuzzy domains: writing, judgment, taste. The big open question is how far RLVR generalizes. Models trained with RLVR on math sometimes get better at writing too, suggesting the underlying capability is reasoning rather than mathematics specifically. But the transfer is messy and incomplete, and the field is still mapping it.

The thing nobody mentions: GRPO is, in some sense, a confession. The value function in PPO had been considered essential machinery. It was elegant, it had a long pedigree in RL, it provably reduced variance. And it turned out, for language models, to be unnecessary. A simpler thing worked just as well. This is a recurring pattern in the alignment literature: the field inherits machinery from classical RL, finds it cumbersome, and eventually realizes that the language-model setting allows simpler approaches. DPO eliminated the reward model. GRPO eliminated the value function. Each time, what was thought to be essential turned out to be a particular choice that did not have to be made. The next simplification has not yet been published, but it is probably already in someone's research notebook.



## Chapter 21


### Constitutional AI


There is a different angle on alignment that deserves its own chapter, because it answers a question the previous chapters do not: where does the preference data come from?

In the standard pipeline, preferences come from humans. Annotators rank responses, and the rankings train the reward model, and the reward model trains the policy. This is expensive — humans are slow and inconsistent — and it has a more troubling property: the model's behavior is whatever average human annotators happen to prefer. If annotators are biased, lazy, or working under time pressure, those properties get baked into the model. The model's "values" are the statistical averages of a particular labor pool's snap judgments. This is not what we want, but it is what we get if humans are the only source of preference signal.

In 2022, Anthropic published a paper on

Constitutional AI. The proposal: instead of (or in addition to) humans, use a written constitution — a set of principles — and an

AI critic that evaluates responses against those principles. A response is asked, in effect: "does this comply with our principles? If not, rewrite it to comply."

The critic is itself a language model, prompted with the constitution. Its judgments are used to generate new training data, which trains the policy.

The recipe has two phases. In the self-critique phase, the model generates a response, then prompts itself to critique that response against the constitution, then prompts itself to revise based on the critique. The result is a (prompt, original, revised) triple that becomes SFT data. The model learns to produce responses that look more like the revised version than the original. This is supervised — the model is being shown improved responses to imitate.

In the RLAIF phase — reinforcement learning from AI feedback — the model generates pairs of responses, and a separate AI critic ranks them based on the constitution. These rankings replace human rankings in the standard RLHF pipeline. The critic, prompted appropriately, plays the role human annotators played. The reward model is trained on the critic's rankings, not on humans'.

The philosophical move is significant.

Instead of approximating an average human annotator, the model is approximating a model reading a written charter. The charter is explicit. You can read it, debate it, change it. Humans designed it; humans can audit it. The model's behavior, in principle, can be traced back to specific lines in the constitution. This is different from the usual situation in deep learning, where the model's "values" are an opaque function of an unwritten labor pool's preferences.

It also scales better. Human annotators are expensive and slow. AI critics are cheap and fast. You can generate millions of comparisons per day, where you might generate thousands with humans. For models that need to be evaluated on a wide range of behaviors — many languages, many topics, many edge cases — the cost difference is what makes coverage achievable at all.

The honest caveats: Constitutional AI does not make the alignment problem easier. It moves it. The new problem is writing a constitution that captures what you actually want. Constitutions are vague — "be helpful, be harmless, be honest" — and the AI critic interprets them. Different critics, with different prompting, produce different judgments. There is still annotator bias; it is just that the annotators are now language models, with their own biases inherited from pre-training. Constitutional AI does not eliminate the problem of preference. It makes the preference signal more transparent, more auditable, and more scalable. It does not make it more correct.

The thing nobody mentions:

Constitutional AI is partly a transparency mechanism, not just an efficiency one.

When a model trained with RLHF behaves badly, it is hard to say why — you would have to trace through the human labels that trained the reward model, and most of those labels are not individually inspectable. When a model trained with

Constitutional AI behaves badly, you can ask: did the constitution permit this? If yes, the constitution is wrong. If no, the critic misread it. The error becomes localizable. This is one of the reasons frontier labs increasingly use

Constitutional-style methods even when human labels are also available — not because AI feedback is better than human feedback, but because it is more legible.



## Chapter 22


### LoRA and the Affordable Fine-Tune
We have one more piece to add to the picture, and it is mostly an engineering trick, but it has reshaped the economics of post-training enough that it deserves its own chapter.

The pre-trained model is enormous. A frontier model has hundreds of billions of parameters; even a "small" open model has tens of billions. Fine-tuning all of those parameters — running gradient descent on the entire weight set — requires a lot of memory. Optimizer state alone is several times the size of the parameters; with

Adam you need running estimates of mean and variance for each parameter, which is more parameters. Fine-tuning a 70-billion-parameter model with full-parameter Adam needs hundreds of gigabytes of GPU memory. This is feasible at frontier labs. It is not feasible for most teams.

In 2021 a paper called "LoRA: Low-Rank

Adaptation of Large Language Models"

proposed a different approach. Freeze the original weights. Add, alongside each weight matrix W, a small low-rank update — two thin matrices A and B such that the effective weight becomes W + BA, where A is d-by-r, B is r-by-d, and r is much smaller than d. Only A and B get gradients.

Only A and B are updated. Only A and B need optimizer state.

The reason this works is empirical, not theoretical. Fine-tuning a pre-trained model usually does not require the full d-by-d update space. The actual updates that gradient descent computes during fine-tuning tend to be approximately low-rank — they live in a small subspace of the full weight space. LoRA constrains updates to that low-rank subspace explicitly. Most of the time, you do not lose much by doing so. With r = 16 or r = 32, you can fine-tune a model with a few hundred times less memory than full fine-tuning, and the result is usually within a percentage point of the fully-fine-tuned model on most benchmarks.

The implications are economic. A single

A100 GPU, which used to be sufficient only for fine-tuning small models, can fine-tune a 70-billion-parameter model with

LoRA. A single H100 can fine-tune a 200-billion-parameter model. The cost of post-training collapses. Researchers, hobbyists, and small companies can now do what previously required a frontier lab. The

Llama ecosystem — the explosion of community-fine-tuned models in 2023-2024 — is a LoRA phenomenon.

There is a beautiful side benefit. The

LoRA matrices A and B are small — typically a few hundred megabytes for a multibillion-parameter model. You can store many LoRAs for the same base model and swap them at serving time. You can deploy a single base model and a library of LoRAs for different domains, different tones, different languages. The base model lives in GPU memory permanently. The LoRA gets loaded for each request. The economics of multi-tenant fine-tuning, where you serve specialized models for many customers, become tractable.

LoRA is also frequently combined with the alignment techniques in the rest of this act. SFT-with-LoRA. DPO-with-LoRA.

The savings compound. A practitioner can take an open-weights model, run DPO with LoRA on a domain-specific preference dataset using a single GPU, and produce a meaningfully better model in days. This was not possible four years ago.

It is now routine.

The thing nobody mentions: there is a quiet inequality embedded in LoRA.

Frontier labs do not use LoRA for their headline models. Full fine-tuning still gives slightly better results, and at frontier scale the slight difference is worth the engineering cost. LoRA has become the democratization layer of post-training — the way everyone outside the top labs can do alignment work. Inside the top labs, the frontier is still full-parameter fine-tuning with bespoke infrastructure. The gap between frontier and democratized models is not the architecture or even the data; it is the small quality boost from full-parameter optimization, multiplied across dozens of training runs over years. The compound interest of being slightly better at every step.

Closing: From Capability to Behavior

We have completed the post-training pipeline. We can now describe, end to end, what happens to a model after pre-training to make it useful.

Pre-training produces a base model: a

Transformer trained on next-token prediction over trillions of tokens of text.

It has knowledge but no manners.

Supervised fine-tuning shows it how to follow instructions, by training it to imitate prompt-response pairs from a curated dataset. Reward modeling teaches a separate model to predict human preferences over responses. RLHF, classically with PPO, optimizes the language model to produce responses the reward model rates highly, with a KL leash to prevent drift. DPO collapses the two-stage RLHF pipeline into a single supervised loss on preference pairs. GRPO further simplifies by removing the value function and using group baselines.

Constitutional AI replaces humans in the preference loop with a written charter and an AI critic. LoRA makes all of these operations affordable on commodity hardware.

Each of these is an answer to a question the previous step left open. SFT answered "how do we make the model follow instructions?" Reward modeling answered "how do we get signal beyond demonstrations?" RLHF answered "how do we use that signal?" DPO answered "do we really need the two-stage pipeline?" GRPO answered "do we really need the value function?" Constitutional AI answered "do we really need humans for every preference?" LoRA answered "do we really need to update every parameter?" The pattern of the field is the same as in Acts II and III: every advance is an answer to a constraint introduced by a previous advance.

What is the end state? In 2026, a frontier model has gone through pre-training, SFT, some combination of RLHF and DPO and

Constitutional AI, with verifiable-reward

RL on reasoning tasks layered on top. The exact recipe varies by lab, and the recipes are guarded. But the moves are now standard. The wild experimentation of 2022-2024 has narrowed to a small set of techniques, applied in a small set of orderings, with most innovation happening at the data layer rather than the algorithm layer. This is what mature subfields look like.

We have a model that follows instructions, behaves helpfully, refuses to do harmful things, and admits uncertainty when it does not know. We do not yet have a model that does these things efficiently, or one that thinks hard before answering, or one that can use tools to extend its abilities. Those problems belong to Act V and Act VI. But we have, finally, a model you can talk to.

The capability was the gift of pre-training. The behavior is the gift of post-training. Both were necessary. Neither is sufficient.

End of Act IV.


## The Inference Problem


Making the model cheap enough to be useful.

Where we left off

In Act IV we finished the post-training pipeline. We have a model that follows instructions, behaves helpfully, refuses harmful requests, and admits uncertainty.

The capability is real. The behavior is real.

We have, at the end of training, an artifact of remarkable usefulness.

It is also, in its naive form, ruinously expensive to run.

A frontier-class model has hundreds of billions of parameters. Each token of generation requires reading every parameter from GPU memory at least once. The arithmetic is not the bottleneck — modern accelerators do trillions of multiply-adds per second. The bottleneck is bandwidth: how fast you can move weights from HBM to the compute units. A single token of generation can require reading hundreds of gigabytes of weights, and even on the fastest hardware that takes milliseconds. Multiply by hundreds of tokens per response, by millions of users, by hundreds of requests each per day, and the cost of serving language models becomes the dominant economic question in the field.

This act is about how we make inference cheap enough to be useful. By the end you will be able to describe, from memory, why generation is memory-bandwidth bound rather than compute-bound; what the KV cache is and why it makes inference both possible and expensive; the engineering tricks that fight memory pressure (Grouped-Query Attention,

FlashAttention, paged attention, quantization); the algorithmic tricks that hide latency (speculative decoding, continuous batching); and the architectural trick that breaks the parameter-cost equation entirely (Mixture of Experts).

If Act IV was about turning capability into behavior, Act V is about turning behavior into a service. The two are different problems. Most of what your users experience — speed, cost, availability — comes from this act, not from the previous ones. Frontier labs win or lose on inference economics as much as on model quality. Sometimes more.

## Chapter 23


### Why Inference Is Hard



Let me start by describing the cost structure of language model inference, because almost every introductory account gets the emphasis wrong.

A Transformer processes a sequence in two distinguishable phases. Prefill is when you feed the model the entire prompt at once. The model runs a single forward pass over all the prompt tokens, computing attention and feed-forward outputs in parallel. Prefill is fast and compute-bound; you can keep the GPU's tensor cores fully utilized, and the wall-clock time scales roughly linearly with prompt length but is dominated by matrix-multiply throughput.

Decode is when you generate tokens one at a time. To produce token N+1, you need to compute its attention against all previous N tokens. Then you advance to

N+2, attention against all previous N+1 tokens. And so on. Each step processes a single new token through the entire model.

There is no parallelism across tokens — the next token depends on the previous one, you cannot generate them simultaneously. Each decoding step requires reading every model parameter from HBM to compute one token's worth of activations.

This is the asymmetry that defines inference economics. During prefill, you process many tokens per pass, so the cost of reading parameters is amortized across tokens. During decode, you process exactly one token per pass, so every parameter has to be read for every token.

Modern GPUs have terabytes-per-second of memory bandwidth and tens of teraflops of compute. The compute is wildly underutilized during decode. A 70-billion-parameter model in 16-bit precision is 140 gigabytes; on an H100 with about 3 TB/s of bandwidth, just reading the parameters takes 140/3000 = 47 milliseconds per token. That is a hard floor. You cannot generate faster than 21 tokens per second on a single H100 for a 70B model, no matter how clever your software is, because the bandwidth is the bottleneck. The actual matrix-multiply for that token would take a few milliseconds at most. The GPU is mostly idle, waiting for weights to arrive.

This is the central fact of inference, and almost every optimization in the rest of this act is a way to address it. Some optimizations reduce how many parameters you need to read (quantization, MoE). Some increase how many tokens you can produce per parameter-read (continuous batching, speculative decoding). Some reduce the additional memory pressure beyond parameters themselves (KV cache management, FlashAttention). What unites them is the same diagnosis: inference is bandwidth-bound, and the entire point of the optimization stack is to either move less data or do more work per byte moved.

The thing nobody mentions: the prefill-vs-decode distinction has economic consequences that don't show up in benchmarks. A user who sends a long prompt and gets a short response is mostly paying for prefill, which is cheap per token. A user who sends a short prompt and gets a long response is mostly paying for decode, which is expensive per token. Anthropic's API prices reflect this — input tokens are 3-5x cheaper than output tokens. This isn't pricing fiction; it tracks the actual hardware cost. Most product designs that fight token budgets are accidentally pushing users toward expensive token shapes. A frontend that pre-loads a long system prompt and returns terse responses is dramatically cheaper than one that streams long responses to a short query, even if total token counts are equal.



## Chapter 24


### The KV Cache


Recall how attention works, from Act

II. For each query position, you compute its attention against the keys at every position, including all earlier ones.

During prefill, this is fine — you do all positions at once. During decode, this becomes painful in a specific way.

To generate token N+1, the model computes the query, key, and value vectors for that one token. The query needs to attend against the keys for tokens 1 through N. But you already computed those keys when you generated tokens 1, 2, 3, and so on. Recomputing them every step would cost O(N²) work for an N-token generation — quadratically expensive.

So we cache them. After every decoding step, we save the key and value vectors that step produced into a buffer. When the next decoding step runs, it computes only the new token's K and V, then attends against the entire stored buffer plus the new entry. The cache grows by one slot per step. Each query attends against everything in the cache.

That buffer is the KV cache. Its existence is what makes Transformer inference tractable. Without it, generating a thousand-token response would cost

O(N²) recomputation. With it, the cost is

O(N) total work — the same N work for the query side, against a cache that is amortized over all previous steps.

But the cache costs memory. A lot of memory. For each layer in the model, for each attention head, for each token in the sequence, you store one key vector and one value vector, each of dimension d/h (where d is the model dimension and h is the number of heads). For a 70-billion-parameter model with 80 layers, 64 heads of dimension 128 each, in 16-bit precision:

80 × 64 × 128 × 2 bytes = ~1.3 megabytes per token, per direction. For an 8K-token context, that's ~20 GB per request. The model itself is 140 GB. The cache for one request is a seventh of the model. Multiply by hundreds of concurrent requests and the cache, not the weights, becomes the dominant memory consumer.

This is why frontier model serving is largely a cache-management problem. The weights are loaded once into GPU memory and stay there. The caches are per-request and grow during generation.

Running out of cache memory means dropping requests or paging to slower storage. Every byte you can save in the cache translates directly into more concurrent users per GPU.

The thing nobody mentions: the KV cache problem is what made long context go from a benchmark headline to a serving headache. Doubling context length doubles cache memory per request. Going from 8K to 1M context is a 125x increase in cache size. Models that advertise million-token context windows are technically capable of using them, but the per-request memory cost makes most production deployments cap context far below the advertised limit. The capability is real; the economics are not.



## Chapter 25


### Grouped-Query Attention


We introduced multi-head attention in Act II, Chapter 6. The standard setup uses many query heads (often 32, 64, or 96), and each head has its own key and value heads. In Multi-Head Attention (MHA), the count of Q, K, and V heads is the same.

When the field discovered that the KV cache dominated serving cost, somebody asked an obvious question: do we need that many K and V heads?

The answer turned out to be no.

Multi-Query Attention (MQA), proposed by Noam Shazeer in 2019, takes the extreme stance: one K head and one V head, shared across all query heads. The query side keeps its many heads, each with its own learned weights, but the key and value sides collapse to a single shared head. This cuts the cache size by a factor equal to the number of original heads — 32x or 64x or whatever. For most models the cache becomes small enough that long contexts and many concurrent requests become feasible.

MQA worked, but with a quality cost.

Models trained with MQA were slightly worse than the equivalent MHA models on most benchmarks — usually a percentage point or two on quality scores. The savings were huge, the loss was small, and for a few years many production deployments used MQA anyway because the economics demanded it.

In 2023 a paper from Google proposed

Grouped-Query Attention (GQA), which is the compromise that has now eaten the field. Instead of one K/V head shared by all queries, you have a small number of

K/V heads — typically 8 — each shared by a group of query heads. With 64 query heads and 8 K/V heads, each K/V head serves 8 queries. The cache shrinks by a factor of 8 instead of 64. The quality loss almost entirely disappears.

This is one of those changes that a reader can look at and ask: why didn't anyone try this from the start? The answer is that nobody knew the cache would matter so much. Multi-Head Attention was the natural design. The discovery that the K/V projections were redundant — that 64 separate K heads were doing nearly the same thing as 8 grouped ones — only happened once people were forced to optimize for serving cost. Constraints reveal which choices were arbitrary.

Today every frontier open model uses

GQA. Llama-3, Qwen-2, Mistral, DeepSeek, all use 8 K/V heads with various numbers of query heads. The cache is small enough that long contexts work and concurrent serving scales. The transition from MHA to

GQA is one of the cleanest examples of a paper that quietly changed the entire serving stack of the field.

The thing nobody mentions: GQA is a training-time decision. You cannot turn a trained MHA model into a GQA model without retraining. This means the choice of how many K/V heads to use was made years before the model is deployed — a serving decision baked in at architecture time. Frontier labs choose K/V head counts based on projected serving economics, not theoretical considerations.

If the inference team wins the architecture argument, the model has 4

K/V heads. If the research team wins, it has 16. The numbers in published papers represent the outcome of internal organizational fights you never see.



## Chapter 26


### FlashAttention


The KV cache addresses one form of memory pressure during decode. But during prefill — and during training — there is a different memory problem, and it shows up in a place you might not expect.

Standard attention computes the matrix

QK^T, which is N×N for a sequence of length N. For long sequences, this matrix is enormous. A 32K-token context has a 32K-by-32K attention matrix per head, per layer. That's a billion entries per head, multiplied by however many heads and layers, multiplied by however many GPUs running in parallel. The intermediate attention matrix doesn't fit in fast on-chip

SRAM. It has to be spilled to slower HBM.

Reading and writing this matrix to HBM during the forward and backward passes is the dominant cost of long-context training and prefill.

In 2022 Tri Dao published a paper called "FlashAttention" that proposed an alternative implementation. The math is unchanged — the output is bit-identical to standard attention. What changes is the memory access pattern.

The trick is tiling. Instead of computing the full QK^T matrix and then applying softmax and then multiplying by V,

FlashAttention processes the computation in small blocks. Each block fits in SRAM.

The algorithm does enough work within

SRAM to update a running output vector and a running softmax normalizer, then moves to the next block. The full attention matrix is never materialized in HBM.

This is the kind of optimization that sounds like it should not be possible.

Softmax requires the maximum value across the entire row to compute correctly — how can you tile across rows when you don't know the max?

FlashAttention solves this with a numerical trick: it tracks a running maximum and a running normalizer per row, and corrects them as new blocks come in. The corrections are exact. The output matches standard attention to floating-point precision.

The result is a 2-4x speedup on long sequences and a substantial reduction in memory pressure. FlashAttention-2 in 2023 improved the speedup further.

FlashAttention-3 in 2024 added FP8 support and reached close to the theoretical peak of H100 hardware. The technique is now the default attention implementation in every major training framework. Models trained without it would be uncompetitively slow.

FlashAttention is the kind of contribution that does not change capabilities — the model produces the same outputs as before — but changes economics. A trick that makes attention 3x faster makes long-context training 3x cheaper, which is the difference between a million-token context being a research curiosity and a deployable feature.

Hardware-aware algorithm design is a discipline. FlashAttention is its canonical example.

The thing nobody mentions:

FlashAttention is a systems paper that succeeded in a research community. Most

ML researchers don't read systems papers; most systems papers don't get cited by ML researchers. FlashAttention crossed the boundary because it was numerically equivalent to the existing operation — you could swap it in without changing your model — but offered a giant practical speedup. The lesson the field learned, slowly, is that the best optimizations are sometimes invisible from the algorithm-paper-writing side.

The cost of being too pure about that division is leaving 3x performance on the table for two years until somebody else writes the kernel for you.



## Chapter 27


### Quantization


The simplest way to reduce memory bandwidth is to reduce the number of bytes per parameter. Models are typically trained in 16-bit floating point — bfloat16 or float16. Each parameter is 2 bytes. A 70-billion-parameter model in bf16 is 140 GB.

What if we used 8-bit instead? Or 4-bit?

Each parameter would take half or a quarter as much memory and bandwidth.

The cache would shrink. Every step of every operation would be faster. The model might be smaller than your GPU's

HBM by enough that you could fit it on commodity hardware.

This is quantization. The catch is that you cannot just round the weights to 8 bits and expect the model to keep working. Naive rounding destroys the quality. The interesting question is how to compress the weights to fewer bits without destroying what they encoded.

The basic trick is to map each weight matrix's value range to a smaller integer range. If a layer's weights span -3.2 to +4.1, you can map that range to 256 integer levels (8-bit) and store one scaling factor per layer (or per row, or per group of rows). Reading a quantized weight requires multiplying by the scale factor before use; this is cheap. The model now takes half the memory and half the bandwidth. The arithmetic happens in a higher precision (16-bit or 32-bit) — quantization is about storage and bandwidth, not about compute. The computation reads quantized weights, dequantizes on the fly, and operates at full precision. The memory savings are real; the arithmetic cost is unchanged.

This works astonishingly well. 8-bit quantization (`int8`) can be applied to almost any model with negligible quality loss. 4-bit quantization (`int4` or one of its variants like NF4) is more aggressive and requires more care — you usually need to quantize in groups (dozens of weights sharing one scaling factor) and use schemes that handle outlier weights specially. Done right, 4-bit quantization preserves most of the model's quality while quartering its memory footprint.

There are two main flavors. Post-training quantization takes a trained model and applies the compression after the fact. This is the simple case; it works for most models on most tasks; it is the default for serving. Quantization-aware training trains the model from the start with the awareness that it will be quantized, and recovers some of the quality lost in post-training quantization.

The line is moving. As quantization techniques improve, post-training quantization gets closer to the quality of full precision, and the case for quantization-aware training weakens.

The implications for serving are dramatic. A model that ran on a 8-GPU node in 16-bit precision might run on a 2-

GPU node in 4-bit. A model that took 50 milliseconds per token in bf16 might take 15 in int4. The user experience improves.

The cost per token falls. And the model — bit-identical from a behavioral standpoint, near enough — gets to more users.

Quantization is the most important optimization in serving economics, by orders of magnitude.

The thing nobody mentions:

quantization has a cliff. Models behave normally down to 4 bits, then start to degrade unevenly below 3 bits, with quality collapsing at 2 bits or below. The cliff exists because the information capacity of a model is roughly bounded by the number of bits per parameter, and below 3-4 bits you start running into the entropy floor of what the model can represent. There are clever techniques (1.58-bit ternary networks, for instance) that try to push past the cliff, but they require quantization-aware training and architectural changes. The simple "take a trained model, quantize, ship" recipe stops working below 4 bits. This is one of the few hard limits in serving.



## Chapter 28


### Speculative Decoding


We have shrunk the parameters with quantization. We have shrunk the cache with GQA. We have made attention faster with FlashAttention. The model is now as cheap to run, per token, as we can make it. The decode-time bandwidth bottleneck still exists — every token still requires reading every parameter — but each parameter is now smaller and there are fewer auxiliary structures to read.

What if we could produce more than one token per pass through the model?

Speculative decoding says: have a small, fast model produce a draft of several tokens. Then, in a single forward pass of the big model, verify the entire draft. If the big model agrees with the draft on tokens 1, 2, 3, and 4, but disagrees on token 5, you accept tokens 1-4, replace token 5 with the big model's answer, and continue from there. You produced four tokens of output for the cost of one forward pass through the big model.

The draft model is typically a smaller model — often a much smaller model fine-tuned to mimic the target model's distribution. It generates draft tokens cheaply. The big model then runs all of them through in parallel, computing what its own next-token distribution would be at each position, and checks whether the draft tokens are consistent with the big model's distribution. The verification is parallel, which is cheap. The big model is forced through one forward pass, regardless of how many tokens it accepts.

The math behind this works because of an elegant property called speculative sampling. You can show, with some probability theory, that if you accept tokens stochastically based on the ratio of the big model's probability to the draft model's probability for that token, the resulting samples are exactly distributed as samples from the big model alone. No quality loss. The draft model is purely an acceleration mechanism.

The speedup depends on the agreement rate between draft and target. For a well-chosen draft model on a typical workload, you can accept 3-5 tokens per big-model forward pass on average. That's a 3-5x speedup at no quality cost. For users, this shows up as faster streaming. For operators, it shows up as lower cost per token.

There is a variant called self-speculation where the same model serves as both draft and target by exploiting tricks like

Medusa heads (extra decoding heads that predict multiple future tokens at once) or layer skipping (running early layers as the draft). These are increasingly important because they don't require maintaining a separate draft model.

Speculative decoding is now standard at frontier labs and in most well-optimized open-model serving stacks. It is one of the rare optimizations that is purely upside — you get faster generation with mathematically identical output. The catch is implementation complexity: you need a paired draft model, you need to handle the verification logic, you need to integrate it with continuous batching.

Most production stacks took a year or two after the technique was published to get it working in production.

The thing nobody mentions: speculative decoding changes incentives for model design. If your serving stack uses speculation, you have a strong reason to ensure the draft model has a similar tokenizer and similar distribution to the target. This affects choices throughout the stack — model families that include matched draft models (like Llama with smaller variants in the same family) are easier to deploy with speculation than models without. The serving requirements are starting to influence the model release cadence.



## Chapter 29


### Continuous Batching


So far we have been thinking about a single request. In production, a server handles many concurrent requests. The naive way to batch them is static batching:

collect a fixed number of requests, run them all together, wait for the slowest one to finish, return all results, repeat.

Static batching is terrible for language model serving. Different requests have different output lengths. A request that needs to generate 50 tokens finishes quickly; a request that needs 5,000 tokens dominates the batch. The 50-token request waits for the 5,000-token request, wasting capacity. GPU utilization is poor because most slots in the batch are idle once their request finishes.

In 2022 a paper called Orca proposed continuous batching (sometimes called iteration-level scheduling or in-flight batching). The idea: do not commit to a fixed batch. At every decoding step, look at which requests are still active, schedule them onto the GPU together, and let new requests join the batch the moment a slot opens up. A batch is now a fluid set of requests that grows and shrinks step by step.

This was a substantial engineering change. The serving stack had to track per-request state across heterogeneous batches. Memory allocation became dynamic — when a request joins, you allocate space in the KV cache for it; when it finishes, you free that space. The complications cascaded: paged attention came along, which lets the KV cache be allocated in fixed-size pages rather than contiguous blocks, much like virtual memory in operating systems. With paged attention, KV cache allocation becomes flexible enough to support arbitrary batch composition.

The throughput improvement is large.

Compared to static batching, continuous batching with paged attention can handle 5-10x more concurrent requests on the same hardware. The reason is utilization:

every step, the GPU is processing as many tokens as can fit, regardless of which requests they belong to. There is almost no idle time waiting for the slowest request.

Continuous batching is now the default in every serious serving stack. vLLM,

TensorRT-LLM, SGLang, and most internal serving systems at frontier labs implement it. If you are doing self-hosted inference and not using continuous batching, you are paying 5-10x more for hardware than you need to.

The thing nobody mentions: continuous batching plus paged attention plus KV cache compression is, collectively, what enables multi-tenant LLM serving at all.

Without these techniques, every request would need its own pre-allocated GPU memory block, and serving more than a few users per GPU would be impossible.

The economic model of LLM APIs — pay per token, no minimum, instant response — depends on this stack. The user-facing pricing is downstream of the systems engineering. When you call an API and get a response in seconds for fractions of a cent, you are riding on top of continuous batching plus paged attention plus speculation plus quantization, all working together. Strip any one of them out and the economics collapse.



## Chapter 30


### Mixture of Experts


Everything in this act so far accepts the basic structure of the Transformer:

every parameter is read for every token.

The optimizations make each parameter smaller, the cache faster, the attention cheaper. What if we changed the structure?

Mixture of Experts (MoE) does exactly that. The idea is older than the

Transformer; the move that made it dominant in modern frontier models is recent.

Replace the FFN sublayer in each

Transformer block with a mixture of FFNs — say, 8, or 64, or 256 of them, called experts. For each token, a small router network decides which 1 or 2 experts that token will use. The token's hidden state goes only to the selected experts. The other experts sit idle for that token.

Read that carefully. The model has 64

FFN copies, but each token uses only 2 of them. For each token, you read 2 experts' worth of FFN parameters, not 64. The total parameter count is 32x larger than a dense model with the same active parameters per token, but the compute per token is the same. Parameters and compute are no longer one-to-one.

This is the MoE bargain: you can have a model with vastly more total parameters than a dense model, while keeping per-token compute roughly the same. The intuition is that different experts specialize in different patterns — one becomes good at math, another at code, another at French — and the router learns which expert each token should go to.

The economic implication is significant.

A 200-billion-parameter dense model costs roughly twice as much per token to serve as a 100-billion-parameter dense model. A 200-billion-parameter MoE model with 25-billion active parameters costs roughly the same per token as a 25-billion dense model. You pay for total parameters in storage; you pay for active parameters in inference cost. Storage is comparatively cheap (HBM is expensive but not as expensive as compute over time); active compute is what dominates serving cost. MoE lets you scale the storage-cheap dimension while keeping the compute-expensive dimension small.

Frontier MoE models include Mixtral (8 experts of 7B each, 2 active per token),

DeepSeek-V3 (256 experts, 8 active), and various rumored frontier-lab models. The training is harder than dense models — you need load balancing losses to ensure tokens distribute evenly across experts, otherwise some experts get all the work and others atrophy. The inference is harder too — different tokens in the same batch may need different experts loaded into compute units, which complicates batching. But the economic case is strong enough that essentially every frontier lab now ships MoE variants.

The thing nobody mentions: MoE is a sparse architecture, and sparse architectures fight modern hardware.

GPUs are designed for dense matrix multiplications. When tokens in a batch route to different experts, you end up with many small matrix multiplications instead of one big one — a workload pattern GPUs are bad at. The actual speedup MoE delivers in production is often less than the theoretical "fewer FLOPs per token"

calculation suggests, because the FLOPs you do execute are at lower utilization.

Serving frameworks have spent the last two years aggressively optimizing MoE inference (expert parallelism, expert offloading, careful scheduling) and the gap is closing. But the lesson is that algorithmic theory and hardware reality are not the same thing, and MoE is one of the cleaner cases where the gap matters in practice.

Closing: The Economics Are the Story

We have completed the inference stack.

We can now describe, end to end, what happens when a token of output gets generated.

The model lives in GPU HBM, quantized to 4 or 8 bits. Each layer's K and V projections share heads via GQA, so the

KV cache is small. Attention is implemented with FlashAttention, so the long-context cost is bounded. The KV cache is paged, so the cache memory is allocated dynamically per request. The serving system runs continuous batching, so concurrent requests share GPU passes.

A draft model produces speculative tokens, so the big model produces multiple tokens per pass. Some layers route tokens to different experts via MoE, so the active parameter count is a fraction of the total parameter count. Every one of these tricks is doing the same thing: trying to produce a token of output for less bandwidth, less memory, less time.

This is what frontier model serving looks like. It is not the model. It is the model plus a stack of optimizations, each of which would have been a major paper five years ago, all of which now coexist in production code. The cost per token has fallen by orders of magnitude in the last three years, almost entirely because of this stack. The model itself is largely the same architecture as 2020. The stack is what changed.

If you internalize one thing from this act, internalize this: in 2026, the cost of a frontier-class inference call is dominated by serving infrastructure, not by training cost amortization. This means the economics of AI products live in this layer.

Whether your application is sustainable, whether your unit economics work, whether you can compete with frontier labs on cost — these are determined by how good your inference stack is, not how good your model is. The model is increasingly a commodity. The serving is the moat.

We have, finally, a usable model that can be served at scale. The next act is about making it think harder.

End of Act V.


## The Reasoning Problem
When the leverage moved from pre-training to test-time compute.

Where we left off

In Act V we made the model cheap enough to be useful. Quantized to four bits, served with paged KV caches, accelerated by speculative decoding, batched continuously, sometimes routed through experts — the model produces tokens at low cost. We have, as of the end of Act V, a deployed system that follows instructions, behaves helpfully, and serves at scale.

We do not have a model that thinks.

Take a simple word problem. A train leaves station A at 9 AM going 60 miles per hour. Another train leaves station B, 200 miles away, at 9:30 AM going 80 miles per hour, heading toward station A. When do they meet? A frontier model from 2022 — a model that had completed all the training and post-training we have described — would often answer wrong. It would emit a number. The number might be plausible, but it would not have been computed. The model would generate the most likely-looking answer-shaped string, the way it generates any string, by predicting one token at a time based on what came before. There was no separate place where reasoning happened. There was only token prediction.

This act is about how we made models reason.

By the end you will be able to describe, from memory, why in-context learning works at all; what chain-of-thought is and why such a small change produced such large gains; how self-consistency turns a single chain into a vote; the difference between retrieval-augmented and tool-augmented generation; and the move that defines 2025 frontier development — reinforcement learning on verifiable rewards. These are the techniques that turned a fluent base model into something that, on hard problems, behaves like a thinking system.

The chapters in this act are short and sharp. The ideas are simpler than those in

Act IV, but they have outsized consequences for what models can do. In particular, this is the act where the leverage shifted: through 2023, capability gains came mostly from bigger models.

From 2024 onward, an increasing fraction of capability gain came from making smaller models reason longer. That shift is



the most important thing happening in the field right now, and this act is where it lives.

## Chapter 31


### In-Context Learning


Let me describe a phenomenon that, when it was first observed, nobody could fully explain.

You take GPT-3. You give it a prompt that contains a few examples of a task.

English: cat. French: chat. English: dog.

French: chien. English: bird. French: — and the model produces oiseau. You did not fine-tune the model. You did not change its weights. You showed it three examples in the prompt, and the fourth example came out correctly. The model has learned a task from its prompt.

This is in-context learning. The 2020

GPT-3 paper, "Language Models are Few-

Shot Learners," made this the central claim, and the claim was correct in a way that surprised even the authors. A model trained with one objective — predict the next token on a corpus of internet text — turned out to have absorbed something more general. Given examples in the prompt, it could perform tasks it had never been trained on.

This is strange. Learning in machine learning means updating weights. The model's weights are frozen during inference. So in what sense is it learning?

There is no fully satisfying answer, but there is a partial one. During pre-training on internet text, the model has seen many patterns that look like "examples of X, then a new instance of X, completed in the manner of the prior examples." Recipes have a structure; FAQ pages have a structure; tables have a structure. The model has learned to be very good at noticing when the current sequence has fallen into a pattern, and at continuing the pattern. From the model's perspective, "learning a task from a few examples" is just "noticing the pattern and continuing it" — no different from continuing a recipe or completing a list. The mechanism is the same as ordinary next-token prediction; what surprised us is how general that mechanism turned out to be.

There is a deeper line of work, sometimes called implicit gradient descent or meta-learning interpretation, that argues attention layers, when given a sequence of input-output pairs, can in some technical sense implement a small gradient-descent step inside the forward pass. The model is doing learning, but the learning is happening within attention rather than within weight updates. There are theoretical demonstrations that this can work in toy settings. Whether it explains in-context learning in real

Transformers remains contested. The phenomenon is real; the mechanism is partial.

What is not contested is the practical consequence. In-context learning meant that, suddenly, you did not need to fine-tune a model for every new task. You could write a prompt. The prompt became the interface. Prompt engineering — a phrase that was a joke in 2020 — became a discipline by 2022. Whole companies were built on the realization that, with the right prompt, a frontier base model could do most things you used to need a custom-trained model for.

The thing nobody mentions: in-context learning has a capacity. You can fit only so many examples in the prompt before context length runs out, and the quality of in-context learning peaks somewhere between five and twenty examples for most tasks. Beyond that, more examples often hurt. Why? Probably because the model's attention is finite. With too many examples, it cannot weight them all properly, and the signal degrades. This is one of those facts that practitioners learn by hand and that the literature has barely formalized. If you want to do in-context learning well, the right number of examples is usually a small handful, chosen carefully. More is not better.



## Chapter 32


### Chain-of-Thought


Now consider a different kind of prompt. Same model, different framing.

Q: A train leaves station A at 9 AM going 60 mph. Another leaves station B, 200 miles away, at 9:30 AM going 80 mph toward A.

When do they meet? A: — and the model emits a number. Often a wrong number.

Now you change exactly one thing.

Before the answer, you ask the model to think.

Q: A train leaves station A at 9 AM going 60 mph.

Another leaves station B, 200 miles away, at 9:30

AM going 80 mph toward A. When do they meet?

Let's think step by step.

The model now produces something like:

At 9:30, the first train has been traveling for 30 minutes at 60 mph, so it has covered 30 miles. The remaining distance between the trains is 200 − 30 = 170 miles. After 9:30, they approach each other at 60 + 80 = 140 mph. So they will meet after 170 / 140 ≈ 1.21 hours, which is about 1 hour 13 minutes.

They meet at approximately 10:43 AM.

The answer is correct. The model can now solve the problem. The same weights that emitted a wrong number a moment ago, when given a different prompt, produce a correct multi-step solution.

This is chain-of-thought. The 2022 paper by Wei and others showed that simply prompting the model to produce intermediate reasoning steps before the final answer dramatically improves accuracy on multi-step problems. The improvement was not a few percentage points. It was sometimes thirty or forty percentage points on benchmarks like

GSM8K (math word problems). For problems that require composition — combining several inferences to reach a conclusion — chain-of-thought is often the difference between the model being usable and the model being useless.

The intuition is straightforward, and you should hold onto it. A Transformer has a fixed amount of computation per token.

The forward pass through a hundred layers is whatever the layers can do, no more. When the model emits a final answer in a single token, all the computation that produced that token had to happen inside that one forward pass.

For a multi-step problem, that's not enough computation. You cannot derive a four-step inference inside a single forward pass; the model's depth is finite.

But if you let the model emit intermediate tokens — partial work, scratch reasoning, restated subproblems — then each of those tokens had its own forward pass, with its own hundred layers of computation. The model is using its own previous outputs as a kind of working memory. The chain of thought is the model's scratchpad. Total computation per problem is now (depth of model) × (number of intermediate tokens) instead of just (depth of model). For hard problems, the difference is enormous.

This is not a metaphor. There are formal results showing that Transformers with chain-of-thought are computationally more powerful than Transformers without, in a precise complexity-theoretic sense. They can solve problems that would require much greater depth in a single forward pass. The intermediate tokens are not just a presentation device. They are additional compute.

Once you internalize this, a lot of subsequent developments stop being mysterious. Self-consistency (Chapter 33) makes sense because if reasoning is happening in the chain, you should sample multiple chains and aggregate. Reasoning

RL (Chapter 36) makes sense because the chain itself is now the unit of optimization, not just the final answer.

Tool use (Chapter 34) makes sense because the chain can include calls to external systems, extending the working memory beyond what the model produces internally.

Chain-of-thought is the move that turned the Transformer from a one-shot predictor into a multi-step reasoner.

Everything after it is variations on the theme.

The thing nobody mentions: chain-of-thought is not free. Each intermediate token costs decoding time. A response that uses chain-of-thought might be 10x as long as a response that does not, which means 10x the cost and 10x the latency.

For problems that benefit from CoT, this is fine — the alternative was being wrong.

For problems that don't, it's pure waste.

There is real engineering work in deciding when to use CoT, ideally automatically.

Some frontier models now have an internal "thinking" mode that they enter only when the prompt seems to benefit from it. The decision of when to think harder is itself becoming a learned behavior.



## Chapter 33


### Self-Consistency


Areasoning chain is a sample. Different samples produce different chains, and different chains can lead to different final answers. Some chains contain mistakes.

Some take dead ends and recover. Some happen to land on the right answer through a partly-wrong path.

If we sample only one chain, we are at the mercy of which chain we got. Sample five chains, and the picture changes.

Maybe four of them arrive at the same answer, by different reasoning paths, and one arrives at a different answer. The four agreeing chains are more likely to be right, because consistent reasoning across multiple samples is harder to fake than a single lucky path. Take the majority answer. Throw away the chains.

This is self-consistency. The 2022 paper by Wang and others is short and clear:

sample multiple chains of thought, take the most common final answer. On benchmarks like GSM8K, self-consistency on top of chain-of-thought adds another 10-20 percentage points of accuracy. The trick costs more compute — you generate several full chains instead of one — but the quality gain is almost free in any setting where you can afford the latency.

The deeper observation is that self-consistency is taking advantage of decoding stochasticity. With temperature greater than zero, the model produces different chains on different runs. Each chain is an independent sample of the model's reasoning distribution. The right answer is, for many problems, the mode of that distribution — even if any single sample only hits it some of the time.

Voting recovers the mode.

This generalizes. The whole framework of test-time compute scaling — the 2024 frontier theme — extends self-consistency. Sample many chains. Score them. Take the best. Or sample chains in a tree, with branches and pruning. Or use a verifier model to check chains and discard the bad ones. Or have the model critique its own work and revise. Each of these is a way of spending more inference compute to get a better answer, and they all share self-consistency's basic insight: a single sample is noisy; multiple samples reduce noise; the right answer is what survives.

The implication for serving economics is significant. Until 2024, the cost of a query was roughly fixed — generate a response, return it. With test-time scaling, you can make any query better by spending more compute on it. The cost-quality tradeoff is now a dial, set per query. Important queries get more samples. Trivial ones get one. Frontier products are starting to expose this dial — "think harder" buttons, "deep research" modes. They are all variants of self-consistency in spirit.

The thing nobody mentions: self-consistency requires a verifiable answer format. Voting on the most common answer only works if the answers are comparable — numerical answers, multiple-choice, structured outputs. For free-form text where every chain produces a different paragraph, there is no obvious vote to take. Self-consistency works because most reasoning benchmarks have clean answer formats.

Real-world problems often do not.

Generalizing self-consistency to free-form domains is an open research problem and one of the areas where you can make a real contribution if you are looking for one.



## Chapter 34


### Tool Use


Chain-of-thought lets the model use its own outputs as scratch memory.

But the model is bad at certain things. It is bad at arithmetic with many digits. It is bad at remembering what happened on the internet last week. It is bad at executing code. It is bad at looking up specific facts in a structured database.

For all of these, there is something the model could just call that is good at the task. A calculator. A search engine. A code interpreter. A SQL database. A weather

API. The pattern that turns this from a fantasy into a working system is tool use.

The mechanism is, by now, standard.

The model is given a list of available tools, each with a name, a description, and a schema for arguments. During generation, the model can emit a special token sequence that means "call this tool with these arguments." The runtime intercepts the call, executes the tool, and inserts the result back into the context. The model continues generation from there.

In practice this looks like: the user asks "what's the weather in Jakarta tomorrow?"

The model generates a tool call:

`get_weather(city="Jakarta", date="2026-05-02")`. The runtime calls the weather

API. The result — say, 32°C and partly cloudy — gets inserted into the model's context. The model then generates a natural-language response that incorporates the result. From the user's perspective, the model "knew" the weather. From the system's perspective, the model knew when to ask.

The deep insight is that tool use is just a special case of chain-of-thought. The intermediate tokens, instead of being internal scratch reasoning, are external

API calls. The model's working memory now extends to whatever the tools can produce. Anything the tool ecosystem can compute, the model can effectively use.

This is why the 2024-2026 frontier looks like model-plus-tools rather than model-alone. The tools dramatically expand what the model can do without needing the model itself to know everything.

There is a hierarchy here. Function calling is the simplest version: the model can invoke a single function. Agents are the more elaborate version: the model can invoke many functions across many turns, accumulate state, decide what to do next based on what it learned, and pursue multi-step goals. The line between these is fuzzy and getting fuzzier; a "function-calling model" with a long enough conversation is indistinguishable from an "agent."

Tool use changes the alignment problem too. A model that just generates text can be evaluated for accuracy. A model that calls tools can take actions in the world — send emails, modify files, execute trades.

The space of mistakes is now much larger.

A wrong tool call is not just a wrong token; it can have real consequences. This is why frontier model deployments increasingly include sandboxed tool execution, permission systems, and human-in-the-loop confirmations. The risks of capable tool use are different from the risks of capable text generation, and the field is still working out the right safeguards.

The thing nobody mentions: most of the value of tool use comes from a small number of tools, used well. People building agentic systems tend to build large tool libraries — dozens or hundreds of functions — under the assumption that more tools means more capability. The data so far suggests the opposite. A model with five excellent tools (search, code execution, calculator, file I/O, web fetch) is usually more capable than one with fifty mediocre ones, because choosing the right tool out of five is a tractable problem and choosing out of fifty is not. The model gets confused. The right design is a small, well-described tool palette that covers a large fraction of use cases. Adding tools without adding capability is a real failure mode.



## Chapter 35


### RAG


There is a special case of tool use that deserves its own chapter, because it is the most economically important deployed AI technique of 2024-2025.

The problem: you want a model to answer questions using information that wasn't in its training data. Internal company documents. Recent news. A specific user's past conversations. You could fine-tune the model to know this information, but that's expensive and slow.

You could put everything in the prompt, but most things don't fit. What you want is a way to fetch the relevant information at query time and put only the relevant pieces in the prompt.

This is Retrieval-Augmented Generation:

RAG. The idea is to keep a corpus of documents stored as embedding vectors in a vector database. At query time, embed the user's query, find the most similar documents in the database, prepend them to the prompt, and let the model generate a response that uses them.

The mechanism is straightforward. An embedding model — separate from the main language model — converts each document chunk into a vector that represents its semantic content. These vectors are stored in a database optimized for nearest-neighbor search (FAISS,

Pinecone, Qdrant, pgvector). At query time, you embed the query, find the top-K nearest documents, retrieve their text, and feed it to the model along with the question.

What makes RAG work is semantic search. The vector database is not doing keyword matching. It is finding documents whose meaning is close to the query, even if they share no exact words. A query about "fixing a leaky faucet" will retrieve documents about "repairing dripping taps"

because their embeddings are close. This robustness is what makes RAG useful — the user does not have to phrase their query the same way the relevant documents are phrased.

RAG has eaten a huge fraction of enterprise AI deployment. Internal knowledge bases, customer support, legal document retrieval, code search — all of these now use RAG as the standard architecture. The reasons are economic.

Fine-tuning a model on a company's internal data is expensive and produces a model that is hard to update. RAG is cheap and can be updated by re-indexing the documents. You don't need ML expertise to add a new document; you just chunk it and embed it.

The honest caveats are real. RAG quality depends on retrieval quality, and retrieval is not solved. If the relevant document is the third-best match instead of the best, the model often won't use it. If chunking splits a critical paragraph in half, the model gets only half the context. If the embedding model doesn't speak your domain, retrieval fails. There are ways to improve all of these — re-ranking, hybrid search, better chunking — but RAG is more like a stack of heuristics than a clean technique. The papers that promise "advanced RAG" are usually papers proposing one more heuristic to try.

The thing nobody mentions: RAG is, in some sense, a workaround for limited context windows. If models had truly unlimited context, you could just put your entire document corpus in the prompt and let the model find what it needs. We don't have that — million-token context windows exist but are expensive and degrade in quality at the long end — so we paste in only the most-relevant pieces. As context windows get longer and cheaper, the pressure on RAG decreases. There is an active debate in the field about whether RAG is a permanent architecture or a transitional hack on the way to long-context-everywhere. The honest answer is: probably permanent for documents that change frequently and where retrieval is cheap, probably replaced by long context for documents that are stable and where retrieval is expensive. Most production systems will use both.



## Chapter 36


### Reasoning RL


We come, finally, to the move that defines 2025 frontier development.

This is where the field is, as of early 2026.

This is what your interviewers will want to talk about.

The setup is the marriage of three things from earlier in this book. From Act IV:

reinforcement learning, with policies and rewards and gradient updates on long sequences. From Chapter 32: chain-of-thought, with models producing intermediate reasoning before final answers. From Chapter 20: GRPO, with group baselines and verifiable rewards as the training signal.

Combine them. Train the model with reinforcement learning, where the policy is the model's chain-of-thought reasoning, and the reward is whether the final answer is correct. Use GRPO as the algorithm. For each problem, sample multiple complete reasoning trajectories.

Check which ones produce correct answers (the verifier — easy for math and code, harder elsewhere). Push the model toward trajectories that produced correct answers and away from those that didn't.

This is reasoning reinforcement learning, sometimes called RLVR (RL with Verifiable

Rewards). The crucial property is that the reasoning itself becomes the unit of optimization. The model is not learning what answer to produce; it is learning how to think in a way that leads to correct answers. Long chains, branching exploration, self-correction in the middle of a chain — all of these emerge as patterns the model learns when they help, and disappear when they don't.

The early evidence was OpenAI's o1 in late 2024, which scored substantially above prior models on hard reasoning benchmarks (math olympiads, competitive programming). DeepSeek's R1 in early 2025 replicated and extended the recipe in the open, showing that reasoning RL on a moderately-sized base model could produce results competitive with much larger non-reasoning models. The R1 paper laid out the GRPO recipe in enough detail that any reasonably equipped lab could reproduce the technique. Within months, every frontier lab had a reasoning model.

The deeper claim — and this is contested — is that reasoning RL transfers. A model trained with RLVR on math gets better at code. A model trained on code gets better at math. A model trained on both starts to look better at general reasoning, including problems that are not strictly verifiable.

This is the bet underwriting the entire 2025-2026 wave of frontier development:

that reasoning is a single thing, and that training it on cheap-to-verify domains generalizes to expensive-to-verify domains. If true, this is enormous. If not,

RLVR remains powerful but contained — math and code only, with quality stagnating elsewhere.

The state of evidence as of early 2026 is mixed. There is clear transfer within technical domains. There is some transfer to broader reasoning tasks (logic puzzles, multi-step planning). There is unclear transfer to fuzzier domains (writing quality, judgment, taste). The labs that bet hardest on reasoning RL — DeepSeek,

OpenAI, Anthropic to a lesser degree — are betting that the transfer is broader than the current evidence shows. They might be right. We don't yet know.

The economic implication, if the bet pays off, is severe. If reasoning capability scales with RL post-training compute rather than primarily with pre-training compute, the cost curve of intelligence shifts. Pre-training is dominated by a small number of giant companies because it requires hundred-million-dollar training runs. RLVR, in contrast, can be done on much smaller compute budgets if you have a base model to start from. This is partly why DeepSeek, with substantially less compute than the U.S. labs, has been competitive at the frontier. The whole structure of who can train frontier models depends on which kind of compute matters most.

The thing nobody mentions: reasoning

RL exposes a lot of weight space to learning that pre-training didn't reach.

The model has the capacity to reason; pre-training merely gave it the prior. RL is what specializes the prior into reasoning specifically. There is a real argument that we are still early in this regime — that current reasoning models are using only a fraction of what RLVR could give us if we threw more compute at it. The next year of frontier development will tell us. If you had to bet on what gets dramatically better in 2026, I would bet on reasoning models trained with much more RL compute than they have today.

Closing: The Compute Has Moved

Step back and notice what has changed.

Through Acts I-III, capability came from pre-training. The story was: bigger models, more data, more compute, lower loss. This was the era of scaling laws. The frontier moved by spending more.

Through Act IV, capability came from post-training. The story was: better instruction-following, better preference alignment, better behavior. This was the era of RLHF, then DPO, then

Constitutional AI. The frontier moved by tuning the model after pre-training.

Through Act V, cost came from inference. The story was: cheaper serving, faster decode, more concurrent users.

This was the era of FlashAttention, GQA, speculative decoding, MoE serving. The frontier moved by squeezing the last drops of efficiency from each token.

Act VI is something different. Capability is now coming from test-time compute.

The story is: longer chains, better reasoning, more thoughtful samples. The frontier moves by thinking more during inference. The model itself isn't bigger; it's spending more tokens per problem.

This is a regime change. Pre-training scaling has not stopped — frontier labs are still training larger models — but the rate of capability improvement per dollar of pre-training compute has slowed, while the rate of capability improvement per dollar of inference compute, via reasoning

RL and chain-of-thought, has not. The leverage has moved.

What this means for the next few years, in concrete terms: the next major capability jumps will probably come from longer thinking, not bigger models.

Models that solve research mathematics will probably do so by reasoning for hours, not by being a hundred trillion parameters. Models that write good code will probably do so by exploring branches and verifying, not by memorizing GitHub.

The architecture, by and large, will be the same Transformer we built in Act II. The training will be the same scaling laws and post-training stack we have already covered. What will change is how much compute the model spends thinking on each query.

If that is right, then the most important practitioner skill of the next era is not training bigger models. It is designing the right reasoning loops, the right verifiers, the right test-time compute allocations.

This is a skill that did not really exist three years ago. It exists now. The labs that get good at it will define what intelligent systems look like in 2027.

Act VII will deal with everything else — multimodality, vision, embodied AI, the parts of the field that are not purely about language. These are growing rapidly, and they share most of the apparatus this book has covered. But the core engine, the thing that makes the modern AI era go, is what we have built across the first six acts.

From the apparatus of Act I to the reasoning loops of Act VI, the chain is complete. We have a model that learns, a model that reads, a model that speaks, a model that scales, a model that aligns, a model that serves, and now, a model that thinks.

What we do with it next is no longer a problem of machine learning research. It is a problem of judgment, taste, and choice. Those are different problems, and they belong to a different book.

End of Act VI.


## The Other Modalities


When the same apparatus turned out to work for everything else.

Where we left off

In Act VI we made the model think. Chain-of-thought, self-consistency, tool use, retrieval, reasoning RL — by the end of that act we had a system that could spend test-time compute to solve problems that base-model token prediction could not.

The story of the language model, as a language model, was essentially complete.

But the world is not made of language. It is made of images, audio, video, sensor readings, protein sequences, chemical structures, three-dimensional scenes. The systems we have spent six acts building are linguistic by construction. To be useful for the rest of the world, they need to absorb those other modalities, or they need to be replaced by something that can.

This act is about how the architecture we built — the same Transformer, the same attention, the same scaling laws — turned out to extend, almost without modification, to most of the rest of perception. By the end you will be able to describe, from memory, why an image can be tokenized; what CLIP did and why it changed everything that came after; how vision-language models work in practice; what diffusion is and why it eats generative modeling for images and video; the segmentation tradition and how it was absorbed into the foundation-model frame; and the AlphaFold story, which is a different kind of architecture solving a different kind of problem and is included here because it is the cleanest example we have of the approach paying off in science.

The chapters in this act are shorter than those in the language acts. Most of the heavy intellectual work is already done.

Vision and multimodality re-use machinery from earlier acts. What is new is mostly in how the apparatus is bent to fit different inputs. There is one important exception — diffusion — which is its own kind of generative procedure, and it gets a more thorough treatment.

A note on framing. Some readers come to ML through computer vision and find this organization backwards. For them, the language work is the recent novelty grafted onto an older vision tradition.

There is truth in this. Convolutional neural networks dominated the field for a decade before the Transformer arrived. The vision-first reader can read this act first.

But the pedagogical argument for going language-first is that the abstractions are cleaner in the language setting — tokens are discrete and atomic, attention is straightforward, scaling is well-behaved.

Vision adds spatial structure and pixels are messy. Once you understand the language case, vision is "it is just like that, but you tokenize an image instead of a sentence."

The other direction — coming from vision to language — has more cognitive friction.

## Chapter 37


### Vision Transformers



e have spent this book treating "tokens" as discrete linguistic units.

A token is an integer index into a vocabulary, a few characters of text. The model embeds it, processes it through

Transformer blocks, predicts the next one.

Everything in Acts II through VI assumes this setup.

What if the tokens were not text?

A 2020 paper by Dosovitskiy and others, titled "An Image Is Worth 16×16 Words,"

answered the question. Take an image.

Cut it into a grid of fixed-size patches — typically 16 pixels by 16 pixels each. A 224×224 image becomes a 14×14 grid of patches, totaling 196 patches. Linearly project each patch to a vector. Add positional embeddings. Feed the sequence of 196 patch vectors into a standard

Transformer.

That is a Vision Transformer, ViT. It is the same architecture as a language model. The only thing that changes is what gets fed in.

Two things made this work, both not obvious at the time. The first is that linear projection of pixel patches is a fine embedding. You might think you need convolutional layers to extract features, the way the previous decade of vision models did. ViT showed you did not. The patches contain all the information; the

Transformer learns whatever features it needs as it goes. Convolutional inductive bias was helpful when models were small and data was scarce. With enough data and enough compute, the bias was not needed; the model figured out spatial structure from scratch.

The second is that scaling worked the same way it did for language. Train ViT on enough images, with enough parameters, and the loss falls. Capability rises. The same scaling laws that governed language models governed vision models, with similar exponents. This is not a coincidence. The Transformer is a universal compute primitive in some pre-theoretic sense, and what scales is the primitive itself, not the modality.

ViT changed vision research overnight.

Within a year, the field's strongest models on image classification, object detection, and segmentation were all Transformer-based. The convolutional architectures that had dominated since AlexNet in 2012 were, by 2022, niche. Some specialized convolutional architectures survive in particular domains — medical imaging, edge deployment — but the frontier is

Transformers.

The relevant under-mentioned point is that ViT is the enabling technology for the entire multimodal era. Once images and text use the same architecture, you can mix them in the same model. You can attend across modalities. You can train on paired image-text data. You can build a vision encoder and a language decoder with the same component, glued together.

Acts on multimodal everything that follows — CLIP, VLMs, multimodal foundation models — all rest on the fact that ViT showed images could be tokenized and processed by Transformers.

The thing nobody mentions: there is an open architectural question of what the right "patch size" is for ViT. 16×16 was chosen by the original paper somewhat arbitrarily, and it has stuck. But for high-resolution images — say a 4K photograph or a satellite image — 16×16 patches mean tens of thousands of tokens, which is unwieldy. Various techniques (Swin

Transformer's hierarchical windows, perceiver-style cross-attention, downsampled patches) have been proposed. None has fully won. For your work on Insta360 360° street imagery, where images are very high-resolution, the patch-size question is a real engineering decision with no obvious right answer.



## Chapter 38


### CLIP and Multimodal Embeddings
Wake a vision encoder — a ViT, say. It produces a vector representation of an image. Take a text encoder — also a

Transformer. It produces a vector representation of a sentence. These two vectors live in different spaces. The image embedding does not "talk to" the text embedding; they are unrelated.

What if we trained them to live in the same space?

In 2021, OpenAI published CLIP —

Contrastive Language-Image Pre-training.

The setup is simple. Collect a dataset of (image, caption) pairs from the internet.

For each pair, compute the image embedding via the vision encoder and the text embedding via the text encoder. The training objective: make the dot product of correctly-paired image and caption embeddings large, and the dot product of mismatched image and caption embeddings small. This is contrastive learning — the model learns to pull positive pairs together and push negative pairs apart.

After training, you have two encoders that produce vectors in a shared space. An image's embedding is close, in this space, to the embedding of a caption that describes it. They speak the same language, geometrically.

This unlocks something that had been impossible before. Zero-shot classification.

Take an image. Compute its embedding.

Compute the embedding of "a photo of a cat," "a photo of a dog," "a photo of a car."

Measure which is closest. That's the classifier. No fine-tuning. No labeled training data for the specific classes. Just embedding everything in the shared space and reading off distances. Performance on standard benchmarks like ImageNet, with this zero-shot approach, was within striking distance of fully supervised models. This was unprecedented.

The reason CLIP mattered so much, beyond zero-shot classification, is that it provided a bridge between vision and language. Once you can map any image to a vector, and any text to a vector, in the same space, you can do all kinds of things you could not do before. You can search for images by text query. You can retrieve text by image. You can score whether an image matches a description. You can use

CLIP as a guide for image generation, telling a generator how close its output is to a target description. Stable Diffusion uses CLIP. Most multimodal systems built between 2021 and 2024 had a CLIP-like model somewhere in their stack.

The training data is interesting. CLIP was trained on 400 million image-text pairs scraped from the internet. This was, at the time, a vast dataset. The data is noisy — most internet captions are not literal descriptions of the image, and many are nonsense. CLIP does not need them to be clean. The contrastive objective is robust to label noise; what matters is that on average, the captions are more related to their images than to other random images.

Internet data clears that bar with margin.

The thing nobody mentions: CLIP's quality depends enormously on the training data, and OpenAI's specific data was never released. The open replication,

OpenCLIP, used the LAION-5B dataset and produced a respectable CLIP-class model, but the original OpenAI CLIP had a small but real advantage that has been hard to fully reproduce. Most of what makes CLIP-class models good or bad is the data, not the architecture or training recipe. The same lesson keeps showing up everywhere in this book: the architecture is increasingly a commodity; the data is the moat.



## Chapter 39


### Vision-Language Models


LIP gives you matched embeddings. It does not give you a chatbot that can look at an image. For that, we need a different setup.

A Vision-Language Model (VLM) is a model that can take an image as input and produce text as output. The standard architecture, by 2024, looks like this. Take a pre-trained vision encoder — typically a

ViT, often initialized from a CLIP-style training. Take a pre-trained language model, fully aligned, ready to deploy.

Insert a small projector network between them: usually a multilayer perceptron, sometimes an attention-based bridge. The projector takes the vision encoder's output (a sequence of patch embeddings) and maps it into the language model's embedding space.

Training proceeds in two phases. First, alignment: freeze the language model and the vision encoder, and train only the projector to map image embeddings into something the language model can use.

The objective is next-token prediction on caption data — given the projected image features, predict the caption. This is fast because most parameters are frozen.

Second, instruction tuning: unfreeze (selectively) the language model and the projector, and train on multimodal instruction data — images paired with question-answer pairs about them. This is the same SFT mechanism from Act IV, just applied to multimodal inputs. The model learns to follow instructions about images:

describe this, count the people, identify the objects, transcribe the text, locate the dog.

After training, the VLM can take an image and a text prompt as input, and produce a text response. The image patches occupy some prefix of the input sequence; the text prompt follows; the model generates from there. From the language model's perspective, it is processing a sequence of embeddings, some of which happen to come from an image. The architecture makes no distinction.

This is the standard recipe, and it is remarkable how well it works. GPT-4V,

Claude 3 with vision, Gemini, Qwen2-VL,

LLaVA, all use variations of this pattern.

The capabilities are broad: visual question answering, document understanding, chart interpretation, OCR, scene description, basic spatial reasoning. The quality, by 2026, is good enough for many production use cases.

There are limits. VLMs are weak at counting beyond a few items, struggle with fine spatial relationships, and can be fooled by adversarial framing. Their reasoning about image content is not perfect. They sometimes hallucinate objects that are not in the image, especially when the prompt suggests those objects. Most of these failure modes trace back to the same source: the vision encoder produces a bag of features, the projector compresses it, and information is lost. A model that can't see clearly cannot reason clearly about what it sees.

Frontier work in 2025-2026 is focused on tighter integration: native multimodal models that train vision and language jointly from scratch, rather than gluing pre-trained pieces together. Gemini was an early example; subsequent frontier models are increasingly native. The bet is that a model that has always been multimodal will be better at multimodal tasks than one that learned them post-hoc. The early evidence is consistent with this, though the gap is narrower than the architecture-first marketing suggests.

The thing nobody mentions: VLM training data is a quiet industrial process that almost no one talks about publicly. To train a good VLM, you need millions of high-quality image-instruction pairs, written by humans, often by paid annotators across many countries. Some of this data is purchased; some is annotated in-house at frontier labs; some is generated by other VLMs in a synthetic-data flywheel. The labor under VLM training — the actual human work of writing instructions and grading outputs — is a substantial fraction of the cost. For your work on POI extraction with

Insta360 imagery, the analogy is direct:

your MapOps annotators on Label Studio are doing the same kind of work, at smaller scale, that the frontier labs do at industrial scale. The bottleneck on quality is usually the data, not the model.



## Chapter 40


### Segmentation: Open-Vocabulary and Promptable
Segmentation — labeling each pixel of an image with the object it belongs to — is one of the oldest tasks in computer vision. For a long time, segmentation models were closed-vocabulary: you trained them on a fixed set of classes (cars, pedestrians, trees), and they could only segment those classes. Adding a new class meant collecting labeled data and retraining.

Two paradigm shifts changed this in the 2022-2023 window.

The first was open-vocabulary segmentation. The idea: combine a strong segmentation model with CLIP-style text embeddings, so that you can segment any class you can describe in natural language.

"Segment the cardboard boxes." "Segment the man in a red jacket." "Segment the broken tiles." The model has not been trained on these specific classes; it figures them out by mapping the text query through CLIP and matching against image regions. Models like ODISE and OpenSeg are open-vocabulary in this sense. The vocabulary is whatever your text encoder can describe, which is essentially everything.

The second was promptable segmentation, which came from Meta's

Segment Anything Model (SAM) in 2023.

SAM is trained on a billion masks across eleven million images, generated through a clever self-bootstrapping pipeline. The output is a model that takes an image and a prompt — a click point, a bounding box, a rough mask, a text description — and produces a segmentation mask for whatever the prompt indicated. You point at a chair; you get the chair's mask. You draw a box around a person; you get the person's mask.

SAM was a watershed for two reasons.

First, it was task-general: a single model could replace dozens of specialized segmentation systems. Second, it was promptable: the user interface was the natural one for segmentation tasks. Click and get a mask. Drag a box and refine the mask. The prompt-based interaction model from language (give a prompt, get a response) transferred cleanly to vision.

By 2024-2025, SAM-2 and SAM-3 had extended this to videos and to text-prompted segmentation, and most production segmentation systems were built on top of SAM-class models. The closed-vocabulary segmentation tradition still survives in specialized domains (medical imaging, semiconductor inspection) where the vocabulary is fixed and the cost of fine-tuning is amortized over millions of inferences. For everything else, promptable plus open-vocabulary has eaten the world.

This matters for your work. POI extraction from street imagery involves a lot of segmentation: identifying signs, storefronts, building facades, and so on.

The traditional approach would be to train a closed-vocabulary segmenter on each class you care about. The modern approach is to use SAM-class models with text prompts, accepting some quality cost in exchange for vastly more flexibility. The right choice depends on how stable your class set is and how much annotation budget you have. For POI extraction, where the classes are reasonably stable but the visual variation is enormous (every

Indonesian street sign is different), open-vocabulary plus targeted fine-tuning is usually the right architecture.

The thing nobody mentions: SAM works astonishingly well for things, and surprisingly poorly for stuff. "Things" are countable objects with clear boundaries — cars, people, signs. "Stuff" is uncountable extent — sky, road, water, vegetation. SAM segments things beautifully and stuff inconsistently. This split is built into how segmentation has historically been formulated, and SAM inherited it. For your kind of work, this matters: if you are segmenting "the road" or "the sky" in street imagery, SAM may not be the right tool. Specialized stuff segmenters or panoptic models still beat SAM at extent-segmentation tasks.



## Chapter 41


### Diffusion Models


So far this act has been about understanding — making sense of inputs in non-text modalities. Now we come to generation. How do you make a model that produces a high-quality image, video, or audio from a prompt?

The dominant answer, for the last few years, has been diffusion. The story of diffusion is mathematically elegant, computationally heavy, and surprisingly different from how language models generate text. Worth slowing down for.

The setup: take any image. Define a process that adds Gaussian noise to it, gradually, in many small steps. After enough steps, the original image is unrecognizable — pure noise. This is the forward process: data → noise.

Now train a neural network to reverse this process. Given a noisy image at step t, predict the slightly less noisy image at step t-1. This is the denoising objective.

Train on millions of (noisy image, slightly less noisy image) pairs, derived from running the forward process on a dataset and pairing adjacent steps.

After training, you have a network that, given a noisy image, can produce a slightly less noisy version of it. To generate a new image, start with pure Gaussian noise.

Apply the trained network repeatedly. At each step, the noise becomes less random, more structured. After hundreds of steps, what comes out is a coherent image — drawn from the same distribution as the training data.

That is diffusion. The forward process is fixed and analytical — you do not learn it.

The reverse process is learned. Generation runs the reverse process from noise to data.

Two things make diffusion practical at scale.

The first is latent diffusion. Doing diffusion in pixel space is expensive — every step has to process millions of pixels. Stable Diffusion in 2022 introduced a key trick: first, train a VAE (variational autoencoder) that compresses images into a smaller latent space — say, 64×64×4 instead of 512×512×3. Then run diffusion in the latent space, which is much cheaper.

Decode the final latent through the VAE to get a pixel image. This makes diffusion tractable on consumer hardware and is how almost all modern image generation works.

The second is conditioning. To generate a specific image — say, "a photograph of a cat in a hat" — you need to condition the denoising process on the prompt. The standard mechanism is cross-attention.

The denoising network is a U-Net (or, increasingly, a Transformer), and at each step it attends to a text embedding of the prompt. The text guides the denoising.

With CLIP-style text embeddings, prompts in natural language steer the generation toward the described image.

The mechanism works astonishingly well — Stable Diffusion's text-to-image quality came almost entirely from this combination of latent diffusion plus CLIP-conditioned cross-attention.

What is lovely about diffusion is that it sidesteps a problem that plagues other generative approaches. Earlier generative models — GANs, VAEs, autoregressive image models — each had failure modes.

GANs had unstable training. VAEs produced blurry samples. Autoregressive models were slow to sample and had quality limits. Diffusion has none of these.

Training is stable. Sampling is slower than a single forward pass but faster than autoregressive token-by-token generation. Quality is excellent. The mathematical framework is clean: a probabilistic story of noising and denoising, with all the steps formally specified.

The economics of diffusion are different from language models. Generation requires many denoising steps — typically 20 to 100 — to produce one image. Each step is roughly the cost of one forward pass through a U-Net or DiT (Diffusion

Transformer). Total generation cost is therefore higher per output than language generation, but each output is much richer (a full image, not a token). The cost per image has fallen dramatically with techniques like consistency models and flow matching that reduce the number of denoising steps without quality loss.

Frontier image generators in 2026 produce high-quality images in one or two steps in some cases.

Diffusion has spread beyond images.

Video generation is diffusion in space and time, with U-Nets or Transformers attending across spatial and temporal axes. Audio generation, 3D structure generation, even some forms of sequence generation are now diffusion-based. The conceptual framework — "learn the reverse of a noising process" — is unreasonably general.

The thing nobody mentions: language models do not use diffusion. There have been many attempts (Diffusion-LM, SEDD, etc.), and they have not displaced autoregressive generation for text. The reason is partly that text is discrete (diffusion is most natural for continuous data), and partly that language models have a strong evaluation criterion (next-token prediction loss) that diffusion doesn't share. The two paradigms have settled into different niches: diffusion for continuous modalities, autoregressive for discrete ones. Whether this is a permanent split or a current local optimum is unclear. Some recent work on "diffusion language models" is interesting, but autoregressive LLMs are not in serious danger of being replaced soon.



## Chapter 42


### Video Generation


Video is, in the most literal sense, a sequence of images over time.

Generating realistic video means generating spatially coherent images that are also temporally coherent — objects persist, motion is plausible, lighting flows naturally. This is much harder than generating a single image.

The dominant approach in 2024-2025 has been to extend diffusion to the temporal dimension. Instead of denoising a single image, the model denoises a short video clip — a tensor with spatial dimensions plus a time axis. The architecture is a Diffusion Transformer (DiT) with attention that operates across both spatial and temporal axes. Training data is paired (video clip, caption) pairs, scraped from the internet, with substantial filtering. Models like Sora, Veo, and Kling are this kind of system.

The challenges are severe and well-known. Temporal coherence is hard: an object's identity should persist across frames, but small errors compound. Long-horizon planning is hard: a model that generates two seconds well can degrade catastrophically over thirty. Physics is hard: gravity, momentum, fluid dynamics emerge as patterns in the training data, but they emerge imperfectly, and models routinely violate physical laws in subtle ways. Causality is hard: in real videos, events have causes; in generated videos, they often don't. A glass falls, but does not break the way physics demands.

The evaluation criteria for video generation are also unsettled. We do not have a principled metric for "is this video physically plausible." Human evaluators rate videos, and the ratings are noisy. The benchmarks are weak. This makes the field move differently from language modeling:

a lot of the progress is anecdotal, demonstrated by curated examples, hard to benchmark systematically. Major releases (Sora's announcement, Veo's demos) rely heavily on hand-picked outputs to convey capability.

Despite all this, video generation in 2026 is good enough to be commercially useful for short clips, illustrative material, and stylized content. It is not yet good enough for serious film production, but the gap is closing on a timescale of years rather than decades. The capability surface is moving forward each quarter.

The under-mentioned point relevant to your work: video generation and video understanding are different problems, and the field has spent more compute on the former. Video understanding — taking a video as input and reasoning about what happens — is increasingly within VLM scope, but the inference cost scales with video length in ways that are economically painful. For applications that involve hours of street imagery or driving footage, the cost structure of video VLM inference is the binding constraint, not the model quality. This is the same lesson as Act V:

serving economics determines what is practical.



## Chapter 43


### AlphaFold


Iwant to close this act with a different kind of system, because the language acts of this book leave one important thing unsaid: the apparatus we have built also works for science.

Protein folding is the problem of predicting a protein's three-dimensional structure from its amino acid sequence.

The structure determines the function, and the function determines whether a protein causes a disease, breaks down a toxin, or carries oxygen. Understanding structures is the foundation of biology. For decades, structures were determined experimentally — X-ray crystallography, cryo-electron microscopy — at enormous cost and slow pace.

In 2018 DeepMind entered the CASP competition (the long-running biennial blind benchmark for structure prediction) with a model called AlphaFold. It performed well. In 2020 they entered

AlphaFold 2, which performed catastrophically well — its predictions, on average, were within experimental error of the true structures. Structural biology was, overnight, in some sense a solved problem. Subsequent versions extended the technique to protein-protein interactions, drug-target binding, and arbitrary biomolecules.

The architecture is interesting.

AlphaFold 2 is built around a custom

Transformer-style block called the

Evoformer. It takes two inputs: a multiple sequence alignment (MSA) — many evolutionary related versions of the target protein, capturing how amino acids covary across species — and a pair representation — an evolving prediction of which amino acids are spatially close to which others.

The Evoformer attends across both, refining both representations through dozens of layers. The final pair representation is decoded into 3D coordinates by a structure module.

The Evoformer is not exactly the

Transformer we built in Act II. It has bespoke attention patterns — row attention, column attention, triangular attention — that exploit the symmetries of the problem. The MSA and pair representations interact through specialized message-passing operations.

This is an architecture designed for structural biology, not borrowed from elsewhere. But the underlying primitives — attention, residual connections, layer norms — are the same primitives we have spent this book describing. The

Transformer family extends to scientific problems with substantial customization but no foundational change.

What AlphaFold demonstrates, and what makes it the right way to close this act, is that the apparatus we have built is not a language tool. It is a general inference architecture. Given a problem with a structured input, a structured output, and enough training data to learn the mapping, the Transformer family can be specialized for it. Language was the first domain because the data was vast and the structure was clean. Vision followed once it was tokenized. Biology followed when the right input representation was found.

Materials science, chemistry, climate modeling, neuroscience — each is now a domain where Transformer-class architectures are producing results that surprised the previous generation of specialists.

The bet underlying this, at the deepest level, is that intelligence is substrate-independent. The same apparatus that learns language can learn vision, can learn proteins, can learn anything where we can pose the right problem and supply the right data. This is a strong claim. It might be wrong. The current evidence suggests it is right, or at least closer to right than any alternative.

The thing nobody mentions: AlphaFold's success was, in significant part, a data success. Protein sequences and structures have been collected for decades; the

Protein Data Bank had hundreds of thousands of structures by 2020. The training set was small by ML standards (~170,000 structures) but the information density was enormous — every example carried more information than a sentence does. Domains where this kind of high-information-density data exists are the next places where Transformer-class models will produce step-change capability. Domains where it does not — most of the social sciences, much of medicine — will need different approaches, or will need someone to build the missing dataset first.

Closing: The Same Apparatus, Bent

We have completed the multimodal extension. Vision, video, audio, biology, segmentation, generation — all built on the same Transformer architecture, with task-specific adaptations. The recurring lesson is that the architecture is general; what changes between modalities is the input representation, the training data, and the loss function.

Consider what this means in aggregate.

The book began with attention as a soft database lookup. Six acts later, the same primitive — soft, content-addressable attention with learned queries, keys, and values — is what makes language models reason, what makes vision models see, what makes diffusion models generate, what makes AlphaFold fold proteins. One mechanism, scaled, is doing all of this. We did not need a different architecture for language than for vision than for biology.

We needed the same architecture, more data, more compute, and the right input representation.

This is the deepest claim of the book, restated: the field rhymes because the apparatus is universal. Every act has been an answer to a constraint introduced by a previous act, but the apparatus answering the constraints has, since 2017, been the same apparatus. The Transformer block, the attention mechanism, the residual stream, the next-token-prediction objective, the scaling laws, the reinforcement learning from preferences — these are not specific to language. They are specific to learning patterns from large datasets, which turns out to be most of intelligence.

Where the apparatus does not yet apply, two things are usually true. The data does not exist in the right form, or the problem is one where averaging over a distribution is the wrong answer. There are tasks — judgment, taste, creativity at the highest level, scientific theory-building — where it is not obvious that more compute and more data will get us there, because the task is not "find the most likely next thing"

but "find the right next thing in a domain where there is no clear ground truth." For these, we may need different approaches.

We may not. The next decade will tell us.

This is where the book ends. Not because there is nothing more to say — the field is moving fast and there will be new acts to write within a few years — but because the structural arc is complete. We started with neurons and gradient descent and ended with proteins and diffusion. We covered, with reasonable density, the apparatus that produces almost all of modern AI. If you have followed the arc, you should now be able to walk into any conversation about machine learning, with anyone, and explain how the pieces fit together. Not memorize. Explain. With reasons.

What you do with that is up to you.

End of Act VII. End of the book.