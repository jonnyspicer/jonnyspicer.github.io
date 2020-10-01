---
layout: mendokusai
author: Jonny Spicer
title: A Monster Is Born
tags: [ Computer Science, Blogging ]
---
After yesterday's talk of endless disco, today I am happy to be able to share some of my first artifically generated blog posts - I am not yet ready to label them as "art", but I think
they're pretty interesting nonetheless. The model I used was gpt-2-simple and I followed the process described in [this blog post by Max Woolf,](https://minimaxir.com/2019/09/howto-gpt2/){:target="_blank"} and the dataset used was the posts on this very site, which I extracted and cleaned using [this python script.](https://github.com/jonnyspicer/jonnyspicer.github.io/blob/master/data_collection.py){:target="_blank"} GPT-2 produces such convincing results that [its creators decided not to release the full version,](https://www.technologyreview.com/2019/08/29/133218/openai-released-its-fake-news-ai-gpt-2/){:target="_blank"} lest it be used for evil, hence the "simple", and I used the 355 million parameter
version, seemingly the biggest possible without requiring specialised hardware (GPT-3 has 175 billion parameters, for reference). For the first run I did 15000 steps, although this
isn't really necessary, for my dataset of ~215k tokens it appeared to reach convergence after around 4000 steps.

And if you didn't care about any of that, here are some of the edited highlights from my trial run with the model. Bearing in mind I think there is room for meaningful finetuning
and improvement, how plausible do you think it is that I penned these myself (or alternately myself after several pints)?

> I’ve been doing a fair bit of this aforementioned searching this week, and I found this article,
> which mentioned that the tournament in question had already been
>announced. It was the 32nd largest tournament in history, so of course
> it had an equal or greater prize purse than the men’s event, and that's what made it
> so special.
> I felt a sense of fraternity with my teammates, a feeling that we are all brothers
> and this tournament meant a lot to me. It was a great bonding experience, one
> that I would highly recommend.

> One of the most talked about downsides to prolonged success is that it requires the user to continually re-learn how the system works, so it is difficult
> to overcome. Lazy loading means absorbing data before it has been expended, a skill that will have a meaningful crossover to other
> language family units at some point. For instance, in C#, you can imagine how frustrating this can be - luckily there is a
> very obvious way around it, but there are several competing philosophies to consider, and many people have
> embraced the fact that skill builds into the language rather than be trapped in a cycle of dependency.

> I laughed a lot, and I don't think this characterisation of
> the character of the film is one I would normally ally myself with. She is not
> a selfish take on the character of an archetypal 1950s suburbanite - instead,
> she is a take on the character of an adult woman who
> has had sex with another man, and it has permanently changed her life.
> The novel's thesis is that modern feminism has displaced
> the men she has had sex with, and given rise to their modern
> offspring. She has tried to distance herself from these men, she doesn't want
> to be associated with them, because she doesn't want them to hurt her,
> they should be contributing to the wider community rather than being existential
> monsters.

> I think a lot of people probably experience something similar to me, and are occasionally referred to as "lucky". I personally always seem to set the bar very, very low for myself in terms of expectations
> and self esteem, and believe that anyone who set a goal in that direction is extremely likely to be disappointed.
> While I have never set or maintained a meaningful expectation of success, it seems reasonable to assume that I would not be disappointed by
> anyone who set themselves the challenge and achieved what I set out to do. As we all know, setting lofty, impossible-to-revise goals is a recipe for failure.

> The point is, I am not into music per se, I mostly listen to bands who make music because
> they make fun, or because they have some kind of social media following. I am
> not into the whole EDM (electronic dance music) thing, or even EDM (edm,
> emo etc). I am into ASMR (anthro, borderline autistic sexual fetish) or whatever-the-fuck-its-called
> instead.

> I am kinda selfish about a lot of things. I don't tell people I have borderline personality disorder because
> I'm worried that people will confuse it with dissociative identity disorder, think I am somehow
> normal, and then treat me completely differently. I don't tell people I have borderline because
> I'm worried that people will confuse it with dissociative identity disorder, think I am
> somehow too emotional to express myself. I don't tell people I have borderline because
> I'm worried that people will confuse it with dissociative identity disorder, think I am
> too much of an emotional child to express myself.

> Because I have struggled with anxiety for so long, I know that in the end, it will be OK, and that it's something worth
> fighting for. I know that every step of the way is going to make me feel something, and that feeling is going to lead to
> something. But I also know that if I don't fight for it, it's not going to happen, and what's more likely is that it'll become a
> negative feeling and spiral into nothingness.

The good news if you like these is that I can generate infinitely more of them - and I'm sure I'll post some more here soon.
