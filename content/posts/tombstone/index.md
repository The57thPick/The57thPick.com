---
weight: 4
title: "Tombstone.js: A Propositional Logic Library"
date: 2016-09-09T21:57:40+08:00
draft: false

author: "jdkato"
authorLink: "https://github.com/jdkato"

summary: |
  An open-source, MIT-licensed JavaScript for propositional logic library.

tags: ["JavaScript"]
categories: ["programming", "logic"]

math: true
---

Propositional logic (or propositional calculus) is,
[according to Wikipedia][1], "a branch of mathematical logic concerned with the
study of propositions (whether they are true or false) that are formed by other
propositions with the use of logical connectives, and how their value depends
on the truth value of their components."

I was introduced to this topic during my third-year of college in a course
titled *Introduction to Formal Logic*. I did not have high expectations going
in (my primary motivation was avoiding more writing-intensive electives), but
it turned out to be one of my favorite courses. One aspect that I found
particularly intriguing about the course was that much of the material seemed
to lend itself nicely to automation&mdash;whether it be the construction of
truth tables or even the analysis of proofs. Indeed, there are a number of
existing online tools such as:

- The [Logic Daemon][2] by Texas A&M University, which "checks proofs and can
  provide hints for students attempting to construct proofs in a natural
  deduction system for sentential (propositional) and first-order predicate
  (quantifier) logic";

- truth table generators by [Michael Rieppel][3], [Jamie Wong][4] or
  [Lawrence Turner][5] (among others); and

- the various utilities developed by [Logictools][6].

I intend to re-implement (and, where possible, try to improve upon) much of the
functionality mentioned above with the goals of gaining a more thorough
understanding of the topic and releasing a full-featured, open-source library
named [Tombstone.js][7] (if you're wondering why I chose the name "Tombstone,"
it was inspired by the [typographical symbol][8]).

## Evaluating Well-Formed Formulas

The first step was to implement the ability to evaluate arbitrary
[well-formed formulas][9] (WFFs). This requires a definition of our vocabulary,
which consists of sentence variables ($\\{A,B, \dots, Z\\}$), parentheses and
connectives.

<table class="table">
   <caption>Logical Connectives (descending order of precedence)</caption>
   <thead>
      <tr>
         <th>Symbol</th>
         <th>Name</th>
         <th>Example</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>~</td>
         <td>negation</td>
         <td>~P ("not P")</td>
      </tr>
      <tr>
         <td>&amp;</td>
         <td>conjunction</td>
         <td>P &amp; Q ("P and Q")</td>
      </tr>
      <tr>
         <td>||</td>
         <td>disjunction</td>
         <td>P || Q ("P or Q")</td>
      </tr>
      <tr>
         <td>-></td>
         <td>implication</td>
         <td>P -> Q ("If P, then Q")</td>
      </tr>
      <tr>
         <td><-></td>
         <td>equivalence</td>
         <td>P <-> Q ("P if and only if Q")</td>
      </tr>
   </tbody>
</table>

A formula is considered well-formed according to the following conditions:

1. All sentence variables are WFFs.

2. If $\phi$ is a WFF, then ~$\phi$ is also a WFF.

3. If $\phi$ and $\psi$ are WFFs, then ($\phi$ & $\psi$), ($\phi$ \|\| $\psi$),
   ($\phi$ -> $\psi$) and ($\phi$ <-> $\psi$) are WFFs.

4. Nothing else is a WFF.

From here, I decided to use the [shunting-yard algorithm][10] to convert WFFs
to [Reverse Polish notation][11] (RPN) for evaluation. In RPN, every operator
follows its operands&mdash;for example, `P & Q` becomes `P Q &`. This parsing
strategy is more commonly associated with mathematical expressions but it seems
to work well for logic too. You can see the algorithm in action below.

<iframe height="300" style="width: 100%;" scrolling="no" title="" src="https://codepen.io/jdkato/embed/NWgoZrG?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/jdkato/pen/NWgoZrG">
  </a> by Joseph Kato (<a href="https://codepen.io/jdkato">@jdkato</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Once in RPN, we can easily evaluate the expression or construct a graphical
representation of the formula's structure (known as a [parse tree][12]) as seen
below.

<iframe height="300" style="width: 100%;" scrolling="no" title="Viz" src="https://codepen.io/jdkato/embed/XWgOLZE?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/jdkato/pen/XWgOLZE">
  Viz</a> by Joseph Kato (<a href="https://codepen.io/jdkato">@jdkato</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## Truth Tables

Now that we can evaluate arbitrary WFFs, generating truth tables is just a
matter of evaluating an expression at all of its variable combinations.

<iframe height="300" style="width: 100%;" scrolling="no" title="" src="https://codepen.io/jdkato/embed/PojVrEw?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/jdkato/pen/PojVrEw">
  </a> by Joseph Kato (<a href="https://codepen.io/jdkato">@jdkato</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## Conclusion

While Tombstone.js is still in its early stages of development, I think this is
a promising start. An approximate roadmap for future development is as follows.

- Extend truth table generation to allow for copying in HTML, Markdown,
  $\LaTeX$, reStructuredText or plain text;

- add the ability to analyze proofs; and

- create a website to showcase Tombstone.js.

I am also considering re-writing the project (that is, the two files it
currently contains) in [TypeScript](https://www.typescriptlang.org/). This
seems like it would offer a number of interesting features without sacrificing
browser support, which is something I would like to keep as high as possible.

Check back for future updates!

## References

- Allen, Colin and Michael Hand. *Logic Primer*. Cambridge, Mass.:
  MIT Press, 2001. Print.

[1]: https://en.wikipedia.org/wiki/Propositional_calculus
[2]: http://logic.tamu.edu/daemon.html
[3]: http://mrieppel.net/prog/truthtable.html
[4]: http://jamie-wong.com/experiments/truthtabler/SLR1/
[5]: http://turner.faculty.swau.edu/mathematics/materialslibrary/truth/
[6]: http://logictools.org/index.html
[7]: https://github.com/jdkato/Tombstone.js
[8]: https://en.wikipedia.org/wiki/Tombstone_(typography)
[9]: https://en.wikipedia.org/wiki/Well-formed_formula
[10]: https://en.wikipedia.org/wiki/Shunting-yard_algorithm
[11]: https://en.wikipedia.org/wiki/Reverse_Polish_notation
[12]: https://en.wikipedia.org/wiki/Parse_tree
