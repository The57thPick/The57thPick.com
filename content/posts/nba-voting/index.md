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

## Analyzing the data

The ultimate goal of this project is to provide a means of assessing
the *quality* of a given ballot. A common complaint with the
existing process is that voters are somehow "biased" or are actively
supporting a certain "narrative." Unfortunately, although it's
straightforward to describe the perceived problem, it's much harder to
actually identify it in practice.

For example, one of the most high-profile cases in recent times was
[Gary Washburn's decision][9] to select Carmelo Anthony over LeBron
James as the 2013 MVP, effectively robbing him of the chance to become
the NBA's first *unanimous* choice (a feat Stephen Curry would later
accomplish in 2016).

> "I was heated," James told Chris Haynes, then of Cleveland.com.
> "But I knew all along [I wasn't getting a unanimous vote]. I just
> knew it, man."
>
> -- [A brief history of LeBron James disagreeing with awards voters][10]

While you might be tempted to say that identifying *unusual*
ballots (such as Washburn's) is a good indication of poor choices, it's
really not that simple&mdash;indeed, what if it's the consensus
*itself* that's "wrong"?

This was exactly the case in 2021, [according to Jayson Tatum][8]:

> “I know I should have made it with the season I had,” Tatum told host
> Ashley Nevel. “I mean $33 million on the line. Obviously, that would
> make anyone feel some type of way. And I wasn’t necessarily upset
> about losing the money. I think I just felt like the way I was
> playing, everything I did, I thought it should have been a
> no-brainer. I think I was just more frustrated with that.”

However, even if it may not be possible to derive objective conclusions
from an inherently subjective process, we can still perform some
interesting data analysis.

### The Washburn Index

The first type of analysis we'll perform is pretty standard in the
fields of data science and statistics: the search for outliers in our
data set.

But what exactly constitutes an *outlier*?

To answer this question, we must first understand the two types of
ballots: there are *ranked lists* (MVP, COY, DPOY, ...) and *team
selections* (All-NBA, All-Rookie, and All-defense).

For ranked-list awards, we define outliers as ballots that are the most
dissimilar to the final result (the consensus). To help us do this,
we're going to use the [Rank-Biased Overlap (RBO)][11] metric.

{{< img src="images/rbo.png" caption="Example RBO values for the 2021 COY award; a lower value implies a more dissimilar result.">}}

The RBO metric is a bounded (`[0, 1]`) similarity measure that includes
top-weightedness: (dis)agreements at the top of two lists will
weigh more heavily than the same (dis)agreements towards the bottom
of the lists.

Below is a visualization of all RBO values for each ranked award.

{{< datapane id="jdkato/reports/n3RGGD7/nba-awards-rbo/embed/" >}}

### The Tatum Indicator

During the [same interview][8] in which Jayson Tatum expressed his
displeasure with the 2020-21 All-NBA 3rd Team voting results, he also
alluded to the need for a more objective criteria for making these All-NBA
teams:

> “I think what they do need to change is – it’s kind of
> opinion-based,” he explained. “100 media members have the vote, and
> what’s the criteria, right? Is there a certain amount of games you
> need to play. Should you be in playoff contention?
> ...”

While the NBA is unlikely to implement such a criteria any time soon,
the idea leads to an interesting question: Is there an implicit
criteria that the media follows? We can begin to answer this by
constructing a profile of what it takes&mdash;*historically*&mdash;to
make an All-NBA team.

{{< datapane id="jdkato/reports/O7vrrL7/nba-awards-leaders/embed/" >}}

The chart above summarizes where each All-NBA team selection ranked in
a particular stat category. For example, the median rank of players to
be named to the All-NBA 1st, 2nd, or 3rd team for FTA (free-throws
attempted) is 12th, while it's only 31st for an All-NBA Defensive
selection and 101st for an All-Rookie selection.

## Conclusion

The analysis here is really just the beginning; there's a lot more to
be explored and this page will be updated with new metrics over time.
If you'd like to performed your own analysis, feel free to download a
copy of the data from the sidebar.

[1]: https://hoopshype.com/2020/07/11/media-nba-awards-vote/
[2]: http://grantland.com/the-triangle/unanimous-animus-the-lebron-james-mvp-vote-and-debunking-the-myths-of-value/
[3]: https://pr.nba.com/voting-results-2020-21-nba-regular-season-awards/
[4]: https://www.yahoo.com/news/nba-alters-voting-process-for-end-of-season-awards-in-quest-for-objectivity-190532014.html
[5]: https://twitter.com/NBA/status/812446292878102528?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E812446292878102528%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fbleacherreport.com%2Farticles%2F2681705-nba-nbpa-agree-on-new-cba-latest-details-comments-reaction
[6]: http://sports.yahoo.com/news/the-rose-rule--why-it-needs-to-change-150439168.html
[7]: https://www.washingtonpost.com/news/sports/wp/2016/12/15/a-deeper-look-inside-the-nbas-new-collective-bargaining-agreement/?utm_term=.2497bf5a6a21
[8]: https://www.masslive.com/celtics/2021/06/jayson-tatum-wants-changes-to-all-nba-voting-criteria-after-costly-snub-during-career-year.html
[9]: http://grantland.com/the-triangle/unanimous-animus-the-lebron-james-mvp-vote-and-debunking-the-myths-of-value/
[10]: https://www.cbssports.com/nba/news/a-brief-history-of-lebron-james-disagreeing-with-awards-voters-usually-he-has-a-point/
[11]: https://github.com/changyaochen/rbo
