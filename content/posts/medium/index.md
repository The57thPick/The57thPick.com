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

- *How to write mathematics on Medium*[^1],
  *Writing Math (LaTeX) Formulas in Medium*[^2], and
  *How to Embed Beautiful Math equations in Medium*[^3] all describe multi-step
  workflows for including math typesetting. Essentially, you write your
  equations in other software, convert them to images, and then copy the images
  into your post.

- *Undocumented Medium Formatting Tricks*[^4] describes an even more convoluted
  process for including internally-linked footnotes: you have to inspect the
  HTML source of a post, copy `name` attributes, and then manually create each
  link.

- *5 Tips for Embedding Tables in Your Medium Posts*[^5] and
  *How to Share Beautiful Tables on your Medium Articles*[^6] describe having
  to copy-and-paste tables into code blocks, include screenshots of your
  tables, or use third-party "embed" functionality.

While these are all useful articles in their own right, none of the proposed
solutions were particularly appealing to me.

What if I want to write a typical Markdown post *once* and have it "just work"
on Medium?

Well, now you can.

## Introducing `pb`, an open-source CLI tool

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

### Tables

Tables are supported through the common GitHub-Flavored Markdown syntax:

| Header | Column 1 | Column 2 | Column 3  |
|:------:|:--------:|:--------:|:---------:|
| tables | are      | very     | useful    |
| for    | showing  | certain  | data      |

You simply create your table in your favorite editor and, when published
to Medium, it shows up as a Markdown-formatted table inside of a code block.

This allows you to make use of Markdown's readable nature to avoid having to
upload your tabular data to a third-party embed service.

[1]: https://medium.com/
[2]: https://github.com/jdkato/pb
[3]: https://code.visualstudio.com/
[4]: https://typora.io/
[5]: https://help.medium.com/hc/en-us/articles/215194537-Using-the-story-editor
[6]: https://github.github.com/gfm/

[^1]: https://medium.com/@tylerneylon/how-to-write-mathematics-on-medium-f89aa45c42a0
[^2]: https://matteocapitani.medium.com/writing-math-latex-formulas-in-medium-4987a2be60d6
[^3]: https://medium.com/@kiranachyutuni/how-to-embed-beautiful-math-equations-in-medium-a041a64dd4e3
[^4]: https://medium.com/@AntyalT/undocumented-medium-formatting-tricks-c827510c1409#f0ef
[^5]: https://medium.com/@mesirii/5-tips-for-embedding-tables-in-your-medium-posts-8722f3fc5bf5
[^6]: https://medium.com/geekculture/how-to-share-beautiful-tables-on-your-medium-articles-bd579738e33f
