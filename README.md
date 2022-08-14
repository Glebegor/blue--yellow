<h1>How to launch Blue&Yellow</h1>

<h3>To launch this project you must change:<br> <b>settings, service_account123.json, goods.views(connect to the google sheets)</b> and set anower <b>Email</b> for sending messanges.</h3>

<h2>For the first Install libraries:</h2>
<p>You can use requirements-txt library</p>
<code>pip install to-requirements.txt</code>
and
<code>requirements-txt setup</code>
<br>or<br>
<code>pip install -r requirements.txt</code>

<h2>Change SECRET_KEY in settings.py(line 7)</h2>
<code>SECRET_KEY = 'Your key'</code>

<h2>Change email and password</h2>
<p>In setting.py you must change name of email on line 99, and change app password of email on line 101</p>

<code>EMAIL_HOST_USER = "Your email"</code><br>
<code>EMAIL_HOST_PASSWORD = "Your pass"</code>


<h2>Change service_account123.json</h2>
<p>You must download key of google cloud account after add it to service_account123.json </p>

<h2>Change goods.views Google spreadsheet</h2>
Change path to json key(line 9)<br>
<code>sba = gspread.service_account(filename="goods/service_account123.json")
</code><br>
Change name of spreadsheet(line 11)<br>
<code>sba = sbh = sba.open("Name of spreadsheet")
</code><br>
Change name of spreadsheet(line 13)<br>
<code>wbks = sbh.worksheet("Name of sheet")
</code><br>

<h2>Migrate database.</h2>
<code>python manage.py makemigration</code>
<code>python manage.py migration</code>

<h2>And write in console</h2>
<code>python manage.py runserver</code>


<h1>About Project</h1>

Hi, ma name is Gleb! And this web-site was create for Blue&Yellow corporation. 
On this site you can order consignment of leather products and anower products.
To have contact with Blue&Yellow corporation you can check footer.
Admins can add, delete and change goods with some forms. 


