import sublime, sublime_plugin, webbrowser, subprocess

class MarkdownPreviewCommand(sublime_plugin.TextCommand):
	"""This command is a simple bit of code that utilizes MultiMarkdown to convert a markdown script to an html file. The file will then be opened in 
	a new tab or window, depending on the browser 
	"""

	def convert(self, file_name, format="html"):
		settings = sublime.load_settings(__name__ + '.sublime-settings')
		subprocess.call([settings.get("mmd_path"), "--to="+str(format), file_name ])

	def open_in_browser(self, base_file_name):
		url = "file://"+str(base_file_name)
		url = str(url[0:int(url.rfind("."))]) +".html"
		webbrowser.open(url,new=2)

	def run(self, edit):
		"""Currently only converts to HTML"""
		file_name = self.view.file_name()
		self.convert( file_name )
		self.open_in_browser( file_name )
		
		
		

