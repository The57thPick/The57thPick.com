---
title: "OpenNBAVoting: An on-going analysis of NBA regular-season awards"
date: 2020-08-30T21:57:40+08:00
draft: false

summary: |
    An analysis of (and open-source dataset for) the NBA's media-voted awards.

author: jdkato
authorLink: https://github.com/jdkato

tags: ["datasets", "data-analysis"]
categories: ["nba"]
---

<!-- https://www.pdf2go.com/ -->

The voting process for the NBA's most prestigious awards&mdash;such as *MVP*,
*DPOY*, and its *All-NBA Teams*&mdash;has always been fairly ill-defined
in terms of both *who* votes and *how* they voted. The rules have
[changed drastically][1] over the years and the full voting results weren't
even published until the 2015 season.

Since that 2015 season, the NBA has released the results as [PDF-formatted][3]
documents tabulated by Ernst &amp; Young LLP. And while this was certainly
a major step forward in transparency, the format isn't very useful for data
analysis.

I'm working on changing that.

## Why is this important?

In 2016, the NBA players and Board of Governors ratified a new
[Collective Bargaining Agreement][5]. This agreement included a
"designated player" exception that allows a team to sign one of its own
players to a five-year maximum contract extension, according to the
[following criteria][7]:

> 1. He makes one of the three all-NBA teams or is named either
        defensive player of the year or most valuable player the previous
        season.
> 2. He has made one of the three all-NBA teams or has been named
    defensive player of the year in two of the prior three seasons or
    the league’s most valuable player in one of the three prior
    seasons.

This exception comes in addition to the well-known
"[Derrick Rose Rule][6]," which incentivizes making All-NBA teams
during a player's first four years. In response to the heightened
stakes of its media-based awards, the NBA also made a [few changes][4]
to its voter-selection process:

> 1. Decreased the number of eligible voters for each award from 130 to 100.
> 2. Limited the selection pool to "independent" media members (no
    radio/television broadcasters or writers associated with a
    particular team).
> 3. Required at least one voter per NBA market.

In total, the NBA's media-based awards have more meaning than ever and
understanding the process has become all the more important.

## Exploring the data

The NBA has 9 distinct media-chosen awards, each with its own number
of placements and scoring system (more on that later). The table below
summarizes each voter's ballot for a given award&mdash;Most Valuable
Player (`MVP`), Coach of the Year (`COY`), Rookie of the Year (`ROY`),
Defensive Player of the Year (`DPOY`), Most Improved Player (`MIP`),
6th Man of the Year (`6th`), All-NBA (`All-NBA`), All-Defense
(`All-Defensive`), and All-Rookie (`All-Rookie`).

{{< datapane id="jdkato/reports/R70BBgA/nba-awards-explore/embed/" >}}

[1]: https://hoopshype.com/2020/07/11/media-nba-awards-vote/
[2]: http://grantland.com/the-triangle/unanimous-animus-the-lebron-james-mvp-vote-and-debunking-the-myths-of-value/
[3]: https://pr.nba.com/voting-results-2020-21-nba-regular-season-awards/
[4]: https://www.yahoo.com/news/nba-alters-voting-process-for-end-of-season-awards-in-quest-for-objectivity-190532014.html
[5]: https://twitter.com/NBA/status/812446292878102528?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E812446292878102528%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fbleacherreport.com%2Farticles%2F2681705-nba-nbpa-agree-on-new-cba-latest-details-comments-reaction
[6]: http://sports.yahoo.com/news/the-rose-rule--why-it-needs-to-change-150439168.html
[7]: https://www.washingtonpost.com/news/sports/wp/2016/12/15/a-deeper-look-inside-the-nbas-new-collective-bargaining-agreement/?utm_term=.2497bf5a6a21
