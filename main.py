#Kelli Jo Pape

import cgi
import webapp2
import os
import logging
import jinja2


# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 


start = """
<!DOCTYPE html>
<html lang = "en">
<head>
	<meta charset = "UTF-8">
	<title> ICC Payment Plan Form </title>

  <link type="text/css" rel="stylesheet" href="static/style.css">	

	<img src= "/static/paymentplanheader.jpg" align="middle">
	<p> <h3> Welcome to the new online ICC payment plan form.  This will be automatically sent to members of the Finance Committee for review.  </h3> </p>

</head>

<body>

<script>
    function addNewPaymentSource() {
    var table = document.getElementById("myTable");
    var lastRow = table.rows.length;
    var row = table.insertRow(lastRow);
  }
</script>

<form action="cgi-bin/main.py method="post" id="daForm">

  <fieldset id="General">

    <legend> <h2> General Info </h2> </legend>

    <iframe src="http://www.icc.coop/current/finance/documents/ICCFinancialAidFAQ.pdf"></iframe>

    <fieldset>
      <legend> Last name: </legend>
      <input type="text" name="lastname">
    </fieldset>
    <fieldset>
      <legend> First name: </legend>
      <input type="text" name="firstname">
    </fieldset>
    <fieldset>
      <legend> E-mail address: </legend>
      <input type="email" name="email">
    </fieldset>
    <fieldset>
      <legend> Please select your house: </legend>
      <select name="house">
      <option value="Baker Graduate">Baker Graduate</option>
      <option value="Black Elk">Black Elk</option>
      <option value="Debs">Debs</option>
      <option value="Escher">Escher</option>
      <option value="Gregory">Gregory</option>
      <option value="King">King</option>
      <option value="Lester">Lester</option>
      <option value="Linder">Linder</option>
      <option value="Luther">Luther</option>
      <option value="Michigan">Michigan</option>
      <option value="Minnie's">Minnie's</option>
      <option value="Nakamura">Nakamura</option>
      <option value="Osterweil">Osterweil</option>
      <option value="Owen">Owen</option>
      <option value="Ruths'">Ruths'</option>
      <option value="Truth">Truth</option>
      <option value="Vail">Vail</option>
      </select>
    </fieldset> <br>

</fieldset>

<fieldset id="Balance">
<legend><h2> Account Balance </h2></legend>
<fieldset>
  <legend>Debt as of Today:</legend>
  <input type="text" name="debttoday"> <br></fieldset>
<fieldset>
  <legend>Next month's charges:</legend>
  <input type="text" name="nextmonth"> <br></fieldset>
<fieldset>
  <legend>Following month's charges:</legend>
  <input type="text" name="follmonth"> <br>
</fieldset>
<fieldset>

<legend>Calendar:</legend> <input type="date" name="date">
</fieldset>
</fieldset>

<fieldset>
<legend><h2>Action Plan:</h2></legend>
<fieldset>
<legend>Schedule of Payments</legend>
<p>I agree to pay the following amounts by the dates listed below.</p>
<p>This amount must include ALL charges from the months covered by this plan.  50% of the total must be paid in 4 weeks, and 100% must be paid in 8 weeks.  All payment plans must be paid in full by the end of the contract period.</p>

<table id="myTable">
  <tr>
    <td>Amount Due</td>
    <td>Date Due</td>
  </tr>
  <tr>
    <td><input type="text" placeholder="Amount Due" name="due1"></td>
    <td><input type="date" placeholder="Date Due" name="due2"></td>
  </tr>
</table>
<br>

<button onclick="addNewPaymentSource()">Add Another</button>


</fieldset>
<fieldset id="Payment">
<legend>Sources of Payment</legend>
<p>In order to be approved for a payment plan, the member must demonstrate their source(s) of monies to cover the necessary debt in accordance with the payment schedule above.
<p>Please fill in the following:</p>

<table id="myTable">
  <tr>
    <th>Source of Income</th>
    <th>Date Available</th>
    <th>Amount Available</th>
    <th>Attach Documentation*</th>
  </tr>
  <tr>
    <td><input type="text" placeholder="Source of Income" name="source"></td>
    <td><input type="date" placeholder="Date Available" name="davail"></td>
    <td><input type="text" placeholder="Amt. Available" name="aavail"></td>
    <td><input type="text" placeholder="Documentation" name="doc"></td>
  </tr>
</table>
<p> *Acceptable types of documentation may include:  documents from the Financial Aid Office, paystubs, etc. </p>
<br>

<button onclick="addNewPaymentSource()">Add Another</button>


</fieldset>
</fieldset>

<fieldset id="Agree">
<legend><h2>Terms of Agreement</h2></legend>
<fieldset>
<p><input type="checkbox" name="understood">I understand that if I miss a payment, I will be fined $20 and eviction proceedings will be started against me.  To stop the eviction process at that point, the outstanding balance due must be paid in full.  I also understand that I will be charged for any costs arising out of the eviction process, including attorney fees, office fees, and court costs.</p>
</fieldset>
<fieldset>
<p>If you or anyone in your house has any questions about this process, please have them contact the ICC Finance Office at iccfinanceoffice@gmail.com or 734-662-4414 ext. 108.  We will be more than happy to assist you.</p>
<p>Any additional comments or concerns, or special background information we should consider in our decision, about this process are welcome here.</p>
<p><textarea name="comments" cols="30" rows="5" class="html-text-box"></textarea>
<input type="reset" value="Reset" class="html-text-box"></p>
</fieldset>

<fieldset>
<input type="submit" value="Submit" align="middle">
</fieldset>
</fieldset>

</form> 

</body>
<footer>Copyright &copy Kelli Pape 2016.</footer>
</html>
"""


class FormHandler(webapp2.RequestHandler):
    #This function creates the start page
    def get(self):

    	logging.info("GET")
		#logging.info(self.request.path)
    	path = 'templates' + self.request.path
	
	temp = os.path.join(os.path.dirname(__file__), path)

	if not os.path.isfile(temp):
		temp = os.path.join(os.path.dirname(__file__), 'templates/general.html')
		path = 'templates/general.html'
		
	#self.response.write(path + '<br />')
	template = JINJA_ENVIRONMENT.get_template(path)

	self.response.write(template.render())


    #This generates every succeeding page and prints
    #the previous page's input as their guess
    #def post(self):
        #logging.info("POST")
        #logging.info("this is just for testing")
        #debttoday2 = self.request.get("debttoday")
        #nextmonth2 = self.request.get("nextmonth")
        #follmonth2 = self.request.get("follmonth")
"""
  	#tries to typecast data into an integer
  	try:
  	    #guess = int(data)
  	    debttoday3 = float(debttoday2)
  	    #nextmonth = float(nextmonth2)
  	    #follmonth = float(follmonth2)

  	    #answer = 42

  	    if debttoday3 <= 0.00:
  	        msg = "You have no debt.  Wut r u doin here."	
  	    elif debttoday3 < 200.00:
  	        msg = "This plan is not required 4 u but thx 4 coming neway"
  	    elif debttoday3 < 1000.00:
  	        msg = "Your debt is below 1000"
  	    else:
  		      msg = "You are in danger of being evicted ... call the ICC NOW!"
  	    # "%d" takes guess as an integer only
  	    self.response.write("<html><p>Your current debt: %d</p></html>" %debttoday3)
  	    self.response.write("%s</p></html>" %msg)

  	#if it can't, then it prints it as a string instead!
  	except:
  	    debttoday3 = debttoday2
  	    msg = "Please provide a numerical answer to 'current debt'"
  	    # "%s" takes guess for w/e it is, converts to string
  	    self.response.write("<html><p>Guess: %s</p></html>" %debttoday3)
  	    #notice I wrote a new line here to stay in scope
  	    self.response.write("<html><p>%s</p></html>" %msg)
"""
  	#this is what makes the process eternal!"""
  	#self.response.write(start)

app = webapp2.WSGIApplication([
	('/.*', FormHandler)
], debug = True)
