---
layout: mendokusai
author: Jonny Spicer
title: Web Accessibility
tags: [ Software development ]
---
The most striking thing about accessibility on the web is that it is *terrible*. As an example, if you run [Google Flights](https://google.com/flights){:target="_blank"} through Lighthouse (Google's own tool!!), it only scores 81/100 for accessibility. Lighthouse's accessibility audit is also far from
comprehensive, and really only checks for the absolute minimum standards a site should achieve. If Google, a company with
infinite expertise and resources, can't make their own web properties fully accessible, then I think that serves as a pretty
clear indicator as to the state of the rest of the web.

There's quite a few reasons for these issues. Firstly, the [WCAG standards](https://www.w3.org/WAI/standards-guidelines/wcag/){:target="_blank"} are quite strict, especially the AA and AAA standards. There is no point in saying that your site is partially
WCAG-compliant, and so many developers simply don't try to adhere to any of the guidelines. Plenty of developers are scared of
ARIA attributes... for some reason.

Making a website accessible will of course mean its development takes more time, in turn costing more money. In my brief
experience with web agencies, most clients are always trying to drive the price of their site down, and very few are willing
to pay extra to have their site meet WCAG standards (or even Lighthouse audit standards).

It's not really taught - at no point during the time I learned HTML do I remember learning anything about ARIA attributes. You're
taught that semantic HTML is good, but never really why - again I have no recollection of it being tied into accessibility at all.

And of course the biggest and most obvious reason - the collective attitude. Accessibility isn't talked about anywhere near enough, very few people shout about it, the vast majority of developers just don't think it's important. If they do, then
they think it's boring additional work, the outcome of which won't affect them anyway. If nobody is going to hold them account,
then why should they make things accessible?

There's a lot of virtue-signalling in the developer community, or at least parts of it. As performative changes are flying around
across the internet, a focus on accessibility could be a change that had a genuinely positive effect on people's lives, people
who don't share the same privilege as most developers.

I also need to work on making what I build more acccessible. This site gets 100/100 on Lighthouse, but I haven't checked it
against the WCAG specification, and I would be very surprised if it even made single A standard, and it's the same with the new
[GAD site.](https://gad.gg){:target="_blank"} I've only recently gotten over my own fear of ARIA tags and started using them.

In the future, the web needs to be accessible by default, not as an afterthought. That includes my corners of it too.
