import sublime, sublime_plugin, webbrowser, subprocess, os

class MarkdownPreviewCommand(sublime_plugin.TextCommand):
	"""This command is a simple bit of code that utilizes MultiMarkdown to convert a markdown script to an html file. The file will then be opened in 
	a new tab or window, depending on the browser 
	"""



	def convert(self, orig_file_name, view, format="html"):

		has_html = self.has_html_header( view )
		if( has_html ):
			file_name = orig_file_name
		else:
			file_name = self.wrap_content_in_temp_file(orig_file_name)
		
		temp_html_name = file_name[0:file_name.rfind(".")]+".html"
		final_html_name = orig_file_name[0:orig_file_name.rfind(".")] +".html"
		settings = sublime.load_settings(__name__ + '.sublime-settings')
		subprocess.call([settings.get("mmd_path"), "--to="+str(format), file_name])

		if(not has_html):			
			os.rename(temp_html_name, final_html_name)
			#aaaand cleanup the temp file
			#careful...
			os.remove(file_name)


		


	def wrap_content_in_temp_file(self, orig_file_name):
		"""In case the buffer does not contain an opening html tag, will populate a temp file
		"""
		
		current_path = orig_file_name[0:orig_file_name.rfind("/")]
		tmp_file_name = current_path+"/MMDTmp.md"

		#create temporary file, wrap the contents in it, and save. Then return the name
		tmp_file = open(tmp_file_name, 'w')
		original = open(orig_file_name, 'r')

		tmp_file.write(self.header)
		tmp_file.write(original.read())
		tmp_file.write(self.footer)
		tmp_file.close()
		original.close()


		return tmp_file_name

		

	def has_html_header(self, view ):
		"""Returns true if the first 50 characters contains an opening html node ('<html>')"""
		text = view.substr(sublime.Region(0,50))
		found = False
		if(text.find("<html>") > -1):
			found = True
		return found

	def open_in_browser(self, base_file_name):
		url = "file://"+str(base_file_name)
		url = str(url[0:int(url.rfind("."))]) +".html"
		webbrowser.open(url,new=2)

	def run(self, edit):
		"""Currently only converts to HTML"""
		file_name = self.view.file_name()
		self.convert( file_name, self.view )
		self.open_in_browser( file_name )


	header = """<html>
		<head>
			<title>MultiMarkdown Preview</title>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		</head>
		<body>
	"""
	
	footer = """</body>
	</html>"""


		
		
		

