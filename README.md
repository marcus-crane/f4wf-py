# F4W Forwarder - Python Edition

It's a Python version of the original [F4WForwarder](https://github.com/marcus-crane/f4wforwarder) that I built in Javascript.

# What is it for?

Wrestling Observer Radio (WOR) is a near-daily podcast/radio show from [Dave Meltzer](https://twitter.com/davemeltzerWON) and [Bryan Alvarez](https://twitter.com/bryanalvarez).

The actual show itself requires a paid account to access the audio files. While the content is worth it, you're outta luck when it comes to accessing it with the majority of podcast clients. A lot of them, including general fan-favourite [Pocket Casts](https://www.shiftyjelly.com/pocketcasts/), don't support feeds requiring authentication.

Personally, the tradeoff in having to use ugly UI alone was enough motivation to figure out how to make the feed accessible using Pocket Casts.

# Whoa, so it's public now? Like piracy?!

Not at all!

The current iteration of this script generates a publically accessible RSS feed, however the actual stream is authenticated by the server using legitimate credentials. My personal feed is only for myself.

The main reason for having the feed publically accessible was just so I didn't have to think about credentials getting caught in server logs should they be sent part of a query but ideally, it might be preferrable than the current setup which is essentially security through obscurity.

# Does it work?

Pretty seamlessly! I have it set to automatically download the latest episodes and it works perfectly. The only downside is that it breaks support for scrubbing to a certain point if you're streaming, as opposed to downloading.

I wonder if that's due to the script not explicitly forwarding the content length? Maybe I'll look into it one day but I rarely, if ever, stream this podcast.

# How are you hosting it?

Personally, I'm using [Gunicorn](http://gunicorn.org/) on a small Linux VPS I run all of my sites off and it uses systemd to keep it running. I've only just figured out how to actually deploy Python scripts properly thanks to this project so I might actually write about it sometime.

# Give me a fun fact

I wrote part of the script while wearing a [Bullet Club](https://en.wikipedia.org/wiki/Bullet_Club) shirt funnily enough.

# I have a question about a thing

I'm still somewhat new to Python but feel free to send me a message on [Twitter](https://twitter.com/sentreh).