<head>
	<title>MarkdownPreview Readme</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>

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

If your MultiMarkdown path is not '/usr/local/bin/mmd', adjust the path for the 'mmd_path' variable in your Sublime configuration.

## Usage ##
To generate a preview, view your saved markdown file (currently a valid saved file is required to pass into Multi Markdown) and press cmd+M (cmd+shift+m). A converted html version of your markdown file should appear in your default browser. These keystrokes can be updated/set in the keybindings.

Alternatively, execute the "Markdown Preview:HTML" command from the Command Palette.

## UTF-8 Special Characters ##

In order for this module to process UTF-8 characters (e.g. 'ö' or 'è') correctly, you should include a meta tag deonoting that the document is UTF-8. At a minimum, this will look like:

	<head>
		<title>Some Title</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	</head>

With the above included in your document, 

## Notes ##
Since this was developed for Mac OS X, there's been no testing for windows / linux. The default key binding is also only set for Mac OSX

[mmd]: http://fletcherpenney.net/multimarkdown/

[subl]: http://www.sublimetext.com/2