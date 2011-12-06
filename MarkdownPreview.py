import sublime, sublime_plugin, webbrowser, subprocess

class MarkdownPreviewCommand(sublime_plugin.TextCommand):
	"""This command is a simple bit of code that utilizes MultiMarkdown to convert a markdown script to 

	"""
	def run(self, edit):
		settings = sublime.load_settings(__name__ + '.sublime-settings')
		subprocess.call([settings.get("mmd_path"),self.view.file_name()])
		url = "file://"+str(self.view.file_name())
		url = str(url[0:int(url.rfind("."))]) +".html"
		webbrowser.open(url,new=2)
		
		

