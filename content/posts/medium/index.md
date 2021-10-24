---
title: "An automated workflow for scientific writing on Medium"
date: 2021-10-23T17:16:18-07:00

author: "jdkato"
authorLink: "https://github.com/jdkato"

summary: |
  How to upload Markdown files to Medium while maintaining tables,
  syntax-highlighted code, math typesetting, and footnotes.

tags: ["markdown", "medium"]
categories: ["technical writing"]

math: true

draft: true
---

[Medium][1] is an excellent platform for blogging and it has increasingly
become a go-to source of knowledge on data science and other technical topics.

Unfortunately, though, the writing experience on Medium for scientific topics
isn't great: there's no support for tables, code syntax highlighting, math
typesetting, or footnotes&mdash;all pretty essential elements for many posts.

I'm not the first person to run into this issue, either. A few searches for
keyword phrases like "medium math formula" demonstrate how widespread the
issue really is:

- [How to write mathematics on Medium][14],
  [Writing Math (LaTeX) Formulas in Medium][15], and
  [How to Embed Beautiful Math equations in Medium][16] all describe multi-step
  workflows for including math typesetting. Essentially, you write your
  equations in other software, convert them to images, and then copy the images
  into your post.

- [Undocumented Medium Formatting Tricks][17] describes an even more convoluted
  process for including internally-linked footnotes: you have to inspect the
  HTML source of a post, copy `name` attributes, and then manually create each
  link.

- [5 Tips for Embedding Tables in Your Medium Posts][18] and
  [How to Share Beautiful Tables on your Medium Articles][19] describe having
  to copy-and-paste tables into code blocks, include screenshots of your
  tables, or use third-party "embed" functionality.

While these are all useful articles in their own right, none of the proposed
solutions were particularly appealing to me.

What if I want to write a typical Markdown post *once* and have it "just work"
on Medium?

Well, now you can.

# Introducing `pb`, an open-source CLI tool

[`pb`][2] is an open-source, command-line tool designed to facilitate a
multi-platform, scientific publishing workflow.

The idea is pretty simple: you write your post locally using your favorite
Markdown editor, such as [VS Code][3] or [Typora][4], and then use `pb` to
upload it to Medium. This has the added benefit of allowing you to easily
cross-post content between Medium and other sites (such as a personal blog).

![A demo of uploading content to Medium](/img/medium-upload.gif)

The tool works by treating Medium's [supported Markdown dialect][5] as an
*output* format rather than an *input* format. In other words, you write your
posts using common Markdown syntax (more on that below) and `pb` converts it
to a format that Medium can understand.

(To learn more about the tool, including how to install and use it, please
visit the [GitHub repository][2]. The remainder of this post is dedicated to
a high-level explanation of its use case.)

## Tables

Tables are supported through the common GitHub-Flavored Markdown syntax:

| Header | Column 1 | Column 2 | Column 3  |
|:------:|:--------:|:--------:|:---------:|
| tables | are      | very     | useful    |
| for    | showing  | certain  | data      |

You simply create your table in your favorite editor and, when published
to Medium, it shows up as a Markdown-formatted table inside of a code block.

This allows you to make use of Markdown's readable nature to avoid having to
upload your tabular data to a third-party embed service.

## Source code

Although Medium already supports code blocks natively, they don't support
syntax-highlighting. This can be pretty jarring for those of us used to
working with nicely-highlighted code.

You can get around this issue by embedding a GitHub Gist for each code block
(indeed, there are [tools to automate][7] that very process), but doing so has
a few subjective drawbacks:

1. It can quickly clutter your collection of GitHub Gists with largely
   meaningless entries (a personal pet peeve of mine).

2. The colors don't automatically change to match Medium's light/dark mode
   setting.

3. It requires uploading your content to a third-party, which goes against
   `pb`'s theme of only working with Medium's supported Markdown elements.

Fortunately, there's another option: Medium supports `<strong>` tags (bold)
inside of their code blocks. Making use of this allows us to achieve a classic
minimalist syntax-highlighting look:

```python
def fib(n):
    """A code snippet taken from https://www.python.org/.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
```

Under the hood, `pb` uses a [Pygments][8]-based lexer to apply `strong` tags to
all keywords. Thanks to Pygments, a wide [selection of languages][9] are
supported.

## Math typesetting

As with tables, Medium has no out-of-the-box support for math equations and
symbols. However, going back Tyler Neylon's aforementioned post[^1], there are
possible solutions.

`pb` performs two types of automated conversions: `inline` and `block`. The
syntax for both follows the well-known [MathJax][10]-style (`$ ... $` and
`$$ ... $$`).

For *inline*-level math, `pb` substitutes unicode characters wherever possible
and then italicizes the statement. Here are a few examples:

- $i+j = n/4$

- $x_{i+1}$ and $2^{32}$

- $\zeta(s) = \sum 1/n^{s}$

For `block`-level math, `pb` uses the [`math-api`][11] project to convert block
statements into an SVG image. It then uses the free, cross-platform, and
open-source [Inkscape][12] application to perform a local conversion to PNG
which is uploaded to Medium. Here's an example:

$$
\iiint_V \mu(u,v,w) \,du\,dv\,dw
$$

## Footnotes

> **Note**: In order for automated footnote-linking to work currently, the
> references (e.g., `[^1]`) must appear within a flat paragraph (`<p>`) tag.
> In other words, you currently can't add footnotes to list items or
> blockquotes.

While Medium *technically* supports a footnote-like syntax with its superscript
operator (`6^7`), there are still a few problems.

First, if you simply use Medium's superscript syntax, you won't have
working internal links. In other words, you can *indicate* that there's a
footnote but you can't actually *navigate* to and from it.

Second, if you want working links (as discussed in Antyal Tennyson's post[^2]),
you need to individually create each link by inspecting Medium's generated
HTML. That's both a lot of work and entirely Medium-specific; what if we're
also posting to another source?

With `pb`, you don't have either of these problems&mdash;it supports the
[Markdown Extra-style][13] footnote implementation. This style is commonly
supported in static site generators (Jekyll, Hugo, ...) and other platforms
(GitHub, Discourse, ...), which means that your content will be very
compatible with other hosts.

# Conclusion

As you probably guessed, this entire post was generated from a local Markdown
file using `pb`. There was no copying-and-pasting from other services,
no manual link creation, no HTML inspection; just one command:

```
$ pb -d /<..>/static/img /<..>/content/posts/medium/index.md
```

I think this is a great step forward in terms of making Medium more
user-friendly for scientific writers.

As the tool develops, I'm planning on offering more configuration options for
choosing how to display content. For example, being able to specify that you'd
actually like to embed GitHub Gists instead of using the default code block.
I'm sure that there are a lot of interesting opportunities to explore.

If you want to help the project out, feel free to stop by its [GitHub
repository][2] to open and issue, submit a PR, or simply give us a star!

[1]: https://medium.com/
[2]: https://github.com/jdkato/pb
[3]: https://code.visualstudio.com/
[4]: https://typora.io/
[5]: https://help.medium.com/hc/en-us/articles/215194537-Using-the-story-editor
[6]: https://github.github.com/gfm/
[7]: https://markdowntomedium.com/
[8]: https://pygments.org/
[9]: https://pygments.org/languages/
[10]: https://www.mathjax.org/
[11]: https://github.com/uetchy/math-api
[12]: https://inkscape.org/
[13]: https://michelf.ca/projects/php-markdown/extra/#footnotes
[14]: https://medium.com/@tylerneylon/how-to-write-mathematics-on-medium-f89aa45c42a0
[15]: https://matteocapitani.medium.com/writing-math-latex-formulas-in-medium-4987a2be60d6
[16]: https://medium.com/@kiranachyutuni/how-to-embed-beautiful-math-equations-in-medium-a041a64dd4e3
[17]: https://medium.com/@AntyalT/undocumented-medium-formatting-tricks-c827510c1409#f0ef
[18]: https://medium.com/@mesirii/5-tips-for-embedding-tables-in-your-medium-posts-8722f3fc5bf5
[19]: https://medium.com/geekculture/how-to-share-beautiful-tables-on-your-medium-articles-bd579738e33f

[^1]: [How to write mathematics on Medium][14], Tyler Neylon, 2016
[^2]: [Undocumented Medium Formatting Tricks][17], Antyal Tennyson, 2017
