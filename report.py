output = "<p></p>"
optionsMessage = ""
def setOptions(options):
	global optionsMessage
	print options
	optionsMessage = "<div> Detecting: ";
	if options.sql != False:
		optionsMessage += "<span class='label label-warning'>SQL Injection</span>"
	if options.xss != False:
		optionsMessage += "<span class='label label-info'>XSS Attacks</span>"
	if options.bsql != False:
		optionsMessage += "<span class='label label-success'>Blind SQL Injection</span>"
	if options.include != False:
		optionsMessage += "<span class='label label-danger'>File Injection</span>"
	optionsMessage+= "</div>"

def generateHeader(url , isFinal=False):
	meta = '<meta http-equiv="refresh" content="2">'
	processing = showProcessing()
	if isFinal == True:
		meta = ""
		processing = ""

	if "Completed" in url:
		url = """<div class='label label-success'>"""+ url +"""</div>"""
	else:
		url = """Processing <div class='label label-primary'>"""+ url +"""</div>"""
	header = """<html>
		<head>"""+meta+"""
			<script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
			<link rel="stylesheet" type="text/css" href='http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css'>
			<script src='http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js'></script>	
			<style>
				.glyphicon-refresh-animate {
				    -animation: spin .7s infinite linear;
				    -ms-animation: spin .7s infinite linear;
				    -webkit-animation: spinw .7s infinite linear;
				    -moz-animation: spinm .7s infinite linear;
				}
				 
				@keyframes spin {
				    from { transform: scale(1) rotate(0deg);}
				    to { transform: scale(1) rotate(360deg);}
				}
				  
				@-webkit-keyframes spinw {
				    from { -webkit-transform: rotate(0deg);}
				    to { -webkit-transform: rotate(360deg);}
				}
				 
				@-moz-keyframes spinm {
				    from { -moz-transform: rotate(0deg);}
				    to { -moz-transform: rotate(360deg);}
				}
				span.label {
					margin: 0 5px;
				}

				.label a {
					color: white !important
				}


			</style>
		</head>
		<body>
		<div class="container">
		<div class="jumbotron">
			<h1 class='h1'>Grabber Report</h1>
			<hr/>
			<h2>"""+ url +"""
			"""+ processing +"""
			</h2><h3>"""+ optionsMessage +"""</h3>
		</div>
		<div class="panel-group" id="accordion">"""
	return header

def generateReport(url, isFinal=False):
	try:
		f = open("results/report.html", 'w')
		header = generateHeader(url, isFinal)

		body = header + """
		"""+ output +"""</div></div></body>
		</html>"""

		f.write(body)
		f.close()

	except IOError:
		print "Failed to create report file"
		sys.exit(1)

def appendToReport(url, message, isFinal=False):
	global output
	output += message
	generateReport(url, isFinal)


def showProcessing():
	message = '<span class="label label-warning"><span class="glyphicon glyphicon-refresh glyphicon-refresh-animate"></span></span>'
	return message