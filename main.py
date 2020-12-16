import webbrowser
webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        
def open(link_format):
    webbrowser.get('chrome').open(link_format)
open('youtube.com')
def test():
  open('https://github.com/Saad-py')
test()
