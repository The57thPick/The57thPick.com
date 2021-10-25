---
title: "COVID-19 and SIR: An introduction to the mathematics of epidemics"
date: 2020-03-23T17:16:18-07:00

author: "jdkato"
authorLink: "https://github.com/jdkato"

summary: |
  A summary of SIR modeling, one of the simplest ways to model the
  human-to-human transmission of an infectious disease.

tags: ["differential equations"]
categories: ["mathematics"]

math: true
---

While the novel coronavirus (COVID-19) itself needs no introduction, its
emergence into the national spotlight presents an unique opportunity to discuss
the mathematics behind the modeling of infectious diseases.

More specifically, in this post, we'll be exploring one of the simplest  ways
to model the human-to-human transmission of an infectious disease&mdash;an
[SIR model][1]:

> An SIR model is an epidemiological model that computes the theoretical number
> of people infected with a contagious illness in a closed population over
> time. The name of this class of models derives from the fact that they
> involve coupled equations relating the number of susceptible people $S(t)$,
> number of people infected $I(t)$, and number of people who have recovered
> $R(t)$.

This post shouldn't require a background in mathematics to understand, but some
familiarity with [ordinary differential equations][2] would be helpful.

## Understanding the model

The Susceptible-Infected-Recovered (SIR) model takes the total size ($N$) of a
particular *closed population* (the world, a country, a town, etc.) and divides
them into three "compartments":

- **Susceptibles or $S(t)$**: All people capable of becoming (but are not yet)
  infected by the particular disease.

- **Infected or $I(t)$**: All people currently infected by the particular
  disease.

- **Recovered or $R(t)$**: All people who have recovered from being infected by
  the particular disease.

As implied by the $f(t)$ notation, the size of each compartment may fluctuate
over time due to various rates of change:

{{< img src="img/sir.svg" >}}

Ignoring natural birth and death rates (for now), the SIR model can be
represented by the following system of ordinary differential equations (ODEs):

$$
\begin{align*}
\frac{dS}{dt} & = - \beta SI \textrm{, }~ S(0) = S_0 \newline
\frac{dI}{dt} & = \beta SI - \gamma I \textrm{, }~ I(0) = I_0 \newline
\frac{dR}{dt} & = \gamma I \textrm{, }~ R(0) = R_0
\end{align*}
$$

Where $\beta$ (infection rate) and $\gamma$ (recovery rate) are system
parameters, and $S(t) + I(t) + R(t) = N$. To get a better idea of what this
looks like, let's do some plotting with Python.

{{< datapane id="jdkato/reports/O7vZXl7/us-sir-system/embed/" >}}

As you can see, the relationship between the ODEs is pretty intuitive: we
assume our entire population is susceptible at the beginning but, over time,
the number of susceptibles decrease by $\beta SI$. This quantity is then added
to the total number of infected, which loses $\gamma I$ to the total number of
recovered.

## The basic reproduction number ($R_0$)

Now that we have a basic understanding of the model, we can take a closer look
at its system parameters. For starters, we're going to focus on the second of
our equations:

$$
\frac{dI}{dt} = \beta SI - \gamma I
$$

When we first encounter a novel infectious disease, this equation helps us
determine what the potential for an epidemic is&mdash;in other words, we want
to examine the equation at time $t = 0$:

$$
\frac{dI}{dt} \Bigr\rvert_{t = 0} = \beta S_0 I_0 - \gamma I_0
$$

The driving question then becomes is $\beta S_0 I_0 - \gamma I_0 > 0$? To make
our analysis easier, let's simplify our equation a little bit:

$$
\begin{align*}
\beta S_0 I_0 - \gamma I_0 & > 0 \newline
\beta S_0 - \gamma & > 0 \newline
\beta S_0 & > \gamma \newline
\frac{\beta S_0}{\gamma} & > 1 \newline
\frac{\beta}{\gamma} S_0 & > 1 \newline
\end{align*}
$$

The ratio $\frac{\beta}{\gamma}$ is known as $R_0$ ("R-nought") or the
[basic reproduction number][3].

{{< img src="img/r-0.jpg" w="50%" caption="A scene from *Contagion* (2011) depicting various R-nought values.">}}

This is the idea: If $R_0 \ge 1$ (the $\Delta$ of infected with respect to $t$)
, then the rate of infection is *increasing* and&mdash;without
intervention&mdash;we'll face an epidemic. If, on the other hand, $R_0 < 1$
then people are recovering *faster* than they're becoming infected and we
aren't dealing with an epidemic.

## "Flattening the curve": A call to action

I'm sure you've heard the phrase "flattening the curve" as a call to action to
slow the spread of COVID-19. But what does this *really* mean?

Well, let's first take a look at what could happen if no interventive measures
are enacted in the U.S.

To estimate the values of $\beta$ and $\gamma$, we'll use the technique
outlined by [Penn Medicine][4]: Since the CDC is recommending 14 days of
self-quarantine, we'll use $\gamma = \frac{1}{14}$, which means
$\beta = (\textrm{g} + \frac{1}{14})$ where $g = 2^{(1/T_d)} - 1$. Using Penn's
cited doubling time ($T_d$) of $8.5$ days, we have $\beta = 0.156392$.

Thus, our estimated $R_0$ for COVID-19 is 2.189.

Now, using the U.S. data as of March 23rd from [Worldometer][5], let's look at
what *could* happen if we let COVID-19 spread unchecked.

{{< datapane id="jdkato/reports/W3DzdKk/us-sir-curve/embed/" >}}

This is the now-infamous "curve" and is very likely similar to models being
shown to elected officials around the country. And the conclusion is clear:
**we must act and we must act now**. In a mere 60 days from today (March 23rd,
2020), the U.S. could have over **6 million** cases of COVID-19&mdash;a number
that would completely overwhelm the [healthcare infrastructure capacity][6].

So, now that we know *why* we must act, what *exactly* can be done?

To answer this question, we must return to our motivating inequality:
$\frac{\beta}{\gamma} S_0 > 1$? In an attempt to make this inequality false,
there are two steps that can be taken:

- We can *decrease* the infection rate, $\beta$, by taking preventive measures.
  This is the goal of the many now-implemented "shelter-in-place" ordinances
  and the measures are outlined in the World Health Organization's
  "Do the Five" campaign.

- We can *decrease* the susceptible population, $S_0$, through the
  administration of a vaccine.

In any case, it's clear that we're in a largely unprecedented situation.

[1]: https://mathworld.wolfram.com/SIRModel.html
[2]: https://en.wikipedia.org/wiki/Ordinary_differential_equation
[3]: https://en.wikipedia.org/wiki/Basic_reproduction_number
[4]: https://penn-chime.phl.io/
[5]: https://www.worldometers.info/coronavirus/#countries
[6]: https://khn.org/news/as-coronavirus-spreads-widely-millions-of-older-americans-live-in-counties-with-no-icu-beds/