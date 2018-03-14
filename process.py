import cgi
fm = cgi.FieldStorage()
choice = fm.getvalue("choice")

str="Content-type: text/html"
print(str)
print()

import html5function
omarkup = html5function.opening_markup('Order Process','Galactic Trade Market', 'style.css')
cmarkup = html5function.closing_markup()
print(omarkup)
markup = """
<nav>
	<a href="Home.html">Home</a>
	<a href="Form.html">Arsenal</a>
	<a href="Form.html">Links</a>
	<a href="Form.html">Contact Us</a>
</nav>
<br/>
<main>
"""

if (choice == 'Cancel'): 
    markup += """
<p> You have cancelled your order </p>
<form action="Home.html">
<p>
<input type="submit" name="action" value="Click here to the front page" autofocus>
</p>
</form>
<br/>
</main>
"""
else:
    markup += """
<p> Thank you </p>
<form action="Home.html">
<p>
<input type="submit" name="action" value="Click here to the front page" autofocus>
</p>
</form>
<br/>
</main>
"""
print(markup)
print(cmarkup)
