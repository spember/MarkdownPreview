# MarkdownPreview #
### A MultiMarkdown package for [SublimeText 2][subl] ###

## Overview ##
There were multiple motivations for this package:

* I've been using [SublimeText 2][subl] quite a lot lately
* I'm using Markdown for a few projects, and wanted a quick way to view them
* I couldn't find a method for previewing Markdown within subl
* I wanted to learn about packages, plugins, commands, etc

So, I downloaded [MultiMarkdown][mmd] and threw this quickly together. I've been finding it useful, and thought I'd through it up on github for others to find.


## Requirements ##
*	MultiMarkdown required. The package has the path to mmd set up in a setting called 'mmd_path'. This defaults to '/usr/local/bin/mmd' and should be overwritten in a User setting if your path differs


## Installation ##
Clone this repo into your Packages folder. To execute the preview, you can use the command palette to execute the preview (Markdown Preview: HTML) or the default key binding of cmd-shift-m.

## Notes ##
Since this was developed for Mac OS X, there's been no testing for windows / linux. The default key binding is also only set for Mac OSX

[mmd]: http://fletcherpenney.net/multimarkdown/

[subl]: http://www.sublimetext.com/2