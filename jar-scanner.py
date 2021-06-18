import re
from datetime import datetime
import os
import webbrowser
import main

# Check if report directory is available or not

report_dir = os.path.join(main.current_dir, "Report")
if os.path.exists(report_dir):
    os.chdir(report_dir)
else:
    os.chdir(main.current_dir)
    os.mkdir("Report")
    os.chdir(report_dir)

# Percentage of Licensed JARs in Project
Percentage = int(((len(set(main.third_party))-len(set(main.final_new_jars)))*100)/(len(set(main.third_party))))
ThirdParty_Per = int((len(set(main.third_party))*100)/(len(set(main.all_jars))))
NonComplaint_Per = int(((len(set(main.final_new_jars)))*100)/(len(set(main.third_party))))
Revised_Per = int((len(set(main.my_dict))*100)/(len(set(main.third_party))))
Deprecated_Per = int((len(set(main.unutilized_jars))*100)/(len(set(main.license_jar))))


# To check current date and time
date_str = datetime.now().strftime("%B %d, %Y %H:%M:%S")

third_party = ""
for element in sorted(main.third_party):
    name = re.split(r"-+\d.+", element)
    nameOfJar = name[0]
    a = element.split(nameOfJar + "-")
    b = a[1].split(".jar")
    new_version = b[0]
    third_party += f""" <tr><td>{nameOfJar}</a></td>
                   <td align="center">{new_version}</td></tr>"""

non_compliant = ""
for element in sorted(main.final_new_jars):
    name = re.split(r"-+\d.+", element)
    nameOfJar = name[0]
    a = element.split(nameOfJar + "-")
    b = a[1].split(".jar")
    new_version = b[0]
    non_compliant += f""" <tr><td><div class="jar-list">{nameOfJar}</div></a></td>
                   <td align="center">{new_version}</td></tr>"""

revised_jars = ""
for element in main.my_dict:
    revised_jars += f""" <tr><td>{element}</a></td>
                   <td align="center">{main.my_dict[element]}</td></tr>"""

deprecated_jars = ""
for element in sorted(main.unutilized_jars):
    name = re.split(r"-+\d.+", element)
    nameOfJar = name[0]
    a = element.split(nameOfJar + "-")
    b = a[1].split(".jar")
    new_version = b[0]
    deprecated_jars += f""" <tr><td>{nameOfJar}</a></td>
                   <td align="center">{new_version}</td></tr>"""


# HTML Template to generate the report
html_text = f"""<html>
<head>
<title>JAR Scanning Report</title>
<style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      text-decoration: none;
      list-style: none;
      font-family: ui-sans-serif;
    }}

    .max-width {{
      max-width: 1300px;
      padding: 0 80px;
      margin: auto;
    }}

    .navbar {{
      z-index: 10;
      position: fixed;
      width: 100%;
      padding: 15px, 0;
      background: cadetblue;
    }}

    .navbar .max-width {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin: .5rem auto;
    }}

    .navbar .name {{
      color: #fff;
      font-size: 35px;
      font-weight: 600;
      margin-left: -74px;
    }}

   .box{{
display: flex;
justify-content: center;
align-items: center;
flex-direction: column;
background: #fff;
padding-top: 35px;
}}
.box .percentage{{
position: relative;
width: 150px;
height: 150px;
}}
.box .percentage svg{{
position: relative;
width: 150px;
height: 150px;
}}
.box .percentage svg circle{{
width: 150px;
height: 150px;
fill: none;
stroke-width: 10;
stroke: #000;
transform: translate(5px,5px);
stroke-dasharray: 440;
stroke-dashoffset: 440;
stroke-linecap: round;
}}
.box .percentage svg circle:nth-child(1){{
stroke-dashoffset: 0;
stroke: #f3f3f3;
}}
.box .percentage svg circle{{
stroke-dashoffset: calc(440 - (440 * {ThirdParty_Per}) / 100);
stroke: #00e6e6;
}}

.box .percentage .number{{
position: absolute;
top: 0;
left: 5px;
width: 100%;
height: 100%;
display: flex;
justify-content: center;
align-items: center;
color: #999;
}}
.box .percentage .number h2{{
font-size: 48px; 
}}
.box .percentage .number h2 span{{
font-size: 24px; 
}}
.box .text{{
padding: 10px 0 0;
color: #999;
font-weight: 700;
letter-spacing: 1px;
}}

    h1 {{
      margin-left: 51px;
      text-align: left;
      font-weight: bold;
      font-size: 32px;
    }}

    h3 {{
      margin-left: 239px;
      margin-top: 31px;
      margin-bottom: -175px;
      color: #999;
      font-size: 25px;
    }}
   
    td {{
      text-align: center;
      background: white;
      padding : 0.25rem;
    }}

    td,
    th {{
      word-break: break-word;
      border: 1px solid #dddddd;
    }}
    .body tr:nth-child(even) td{{
        background-color: #dddddd;
    }}
    th {{
      font-weight: bold;
      background: white;
    }}
    
    .summary th {{
      color: black;
    }}

    .dashboard {{
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      margin: 1rem 3.5rem;
    }}

    .dashboard .list {{
      display: flex;
      flex-direction: column;
      margin: .5rem 1rem;
      width: 25%;
      box-shadow: 0 0 3px #c4c4c4;
      background-color: cadetblue;
      border-radius: .25rem;
    }}

    .dashboard .list .element {{
      padding: 1.0rem 1.25rem;
      color: #fff;
      font-weight: 1000;
      font-size: 1.2rem;
      border-bottom: 2px solid aliceblue;
      cursor: pointer;
      
      
      
    }}

    .dashboard .list .element.active {{
      background-color: #00B3B3;
    }}

    .dashboard .list .element:last-child {{
      border: none;
    }}

    .dashboard .list .element.active:first-child {{
      border-radius: .25rem .25rem 0 0;
    }}

    .dashboard .list .element.active:last-child {{
      border-radius: 0 0 .25rem .25rem;
    }}

    .dashboard .info-box {{
      display: flex;
      flex-direction: column;
      width: 70%;
      margin: .5rem 0;
    }}

    .dashboard .info-box .header {{
      padding: .5rem 1rem;
      color: #fff;
      font-weight: 1000;
      font-size: 1.2rem;
      border-bottom: 2px solid;
      background-color: #00B3B3;
    }}

    .dashboard .info-box .body {{
	  font-size: 1.0rem;
	  font-weight: 400;
      padding: .5rem 1rem;
      box-shadow: 50px 50px 100px #c4c4c4;
      height: 70vh;
      overflow-y: auto;
    }}
  </style>
</head>
<body>
  <nav class="navbar">
    <div class="max-width">
      <div class="name">JAR-Scanner Report<span>.</span></a></div>
    </div>
  </nav>
  <h2 align="right" style="color:black; padding-top: 65px;">Generated on {date_str}</h2>
    <p style="font-size: 11px; padding: 62px; padding-top: 14px; padding-bottom:0px">JAR-Scanner version 1.0 is a python based tool performing the analysis of all the JARs which are bundled as part of the product release. The main objective of this tool is to find the 3rd party JARs in the project and check if the license has been procured or not. It is done by comparing all the jars with the existing License & Attribution document which contains the list JARs with already procured licenses. The tool will also project the JARs which have been removed from the project</p>
   <div class="dashboard">
    <div class="list">
      <div class="element" id="sum">Summary</div>
      <div class="element" id="thr">3rd Party JARs</div>
      <div class="element" id="ncj">New JARs</div>
      <div class="element" id="rev">Upgraded JARs</div>
      <div class="element" id="dep">Unutilized JARs</div>
      
      <div class = "box">
<div class = "percentage">
<svg>
<circle class="percircle" cx="70" cy="70" r ="70"></circle>
<circle class="percircle" cx="70" cy="70" r ="70"></circle>
</svg>
<div class="number">
<h2 class='sumPer'>{Percentage}<span>%</span></h2>
<h2 class= 'thrPer'>{ThirdParty_Per}<span>%</span></h2>
<h2 class= 'ncjPer'>{NonComplaint_Per}<span>%</span></h2>
<h2 class= 'revPer'>{Revised_Per}<span>%</span></h2>
<h2 class= 'depPer'>{Deprecated_Per}<span>%</span></h2>
</div>
</div>
<h2 class="sumPer">Licensed JARs</h2>
<h2 class="thrPer">3rd Party JARs</h2>
<h2 class="ncjPer">New JARs</h2>
<h2 class="revPer">Upgraded JARs</h2>
<h2 class="depPer">Unutilized JARs</h2>
</div>
      
      
      
    </div>
  
    <div class="info-box" id="summary">
      <div class="header">Summary</div>
      <div class="body" style="padding-top: 131px;">
        <table width="100%" class="summary" align="left"">
          <tr><th width="50%" height="24">JAR Type</th><th width="50%" align="center">Count</th></tr>     
          <tr><td>Total JARs</a></td><td align="center">{len(set(main.all_jars))}</td></tr>
          <tr><td>Proprietary JARs</a></td><td align="center">{len(set(main.suppression_jar))-1}</td></tr>
          <tr><td>3rd Party JARs</a></td><td align="center">{len(set(main.third_party))}</td></tr>
          <tr><td>New JARs</a></td><td align="center">{len(set(main.final_new_jars))}</td></tr>
          <tr><td>Upgraded JARs</a></td><td align="center">{len(set(main.my_dict))}</td></tr>
          <tr><td>Unutilized JARs</a></td><td align="center">{len(set(main.unutilized_jars))}</td></tr>
        </table>
     </div>
  </div>
     <div class="info-box" id="third_party">
        <div class="header">
            <span id='text-left'>3rd Party JARs <span style="float: right"> Count:{len(set(main.third_party))}</div>
            <div class="body">
              <table width="100%" class="summary">
              <p><br/>All the 3rd party JARs which are currently part of the project are listed below.</p><br/>
              <tr><th width="50%" height="24">JAR Name</th><th width="50%" align="center">JAR Version</th></tr> 
               {third_party}
                </table>
            </div>
      </div>
      <div class="info-box" id="non_compliant">
        <div class="header">New JARs <span style="float: right"> Count:{len(set(main.final_new_jars))}</div>
            <div class="body">
             <table width="100%" class="summary">
              <p><br/>All the JARs which have been newly added to the project and are not part of the Suppression or License JAR list are listed below.</p><br/>
              <tr><th width="50%" height="24">JAR Name</th><th width="50%" align="center">JAR Version</th></tr> 
               {non_compliant} 
                </table>
            </div>
      </div>
      <div class="info-box" id="revised_jars">
        <div class="header">Upgraded JARs <span style="float: right"> Count:{len(set(main.my_dict))}</div>
            <div class="body">
               <table width="100%" class="summary">
               <p><br/>All the 3rd party JARs which are part of the project but the JAR version has been upgraded are listed below.</p><br/>
              <tr><th width="50%" height="24">JAR Name</th><th width="50%" align="center">JAR Version</th></tr> 
               {revised_jars} 
                </table>
            </div>
      </div>
      <div class="info-box" id="deprecated_jars">
        <div class="header">Unutilized JARs <span style="float: right"> Count:{len(set(main.unutilized_jars))}</div>
            <div class="body">
                <table width="100%" class="summary">
                <p><br/>All the 3rd party jars which are part of the License document but are not being utilized in the project currently are listed below.</p><br/>
              <tr><th width="50%" height="24">JAR Name</th><th width="50%" align="center">JAR Version</th></tr> 
               {deprecated_jars} 
                </table>
            </div>
      </div>
</div>

<script>
   var list_id = [ "sum" ,  "thr" , "dep" , "ncj" , "rev"];
   var coll = document.getElementsByClassName("element");
   var info_id = ["summary" , "third_party" , "deprecated_jars", "non_compliant" , "revised_jars"];
   var per_id = [ "sumPer" ,  "thrPer" , "depPer" , "ncjPer" , "revPer"];
   
   var val="summary";
   var k;
   var perVal = "sumPer"
    document.getElementById("sum").classList.add("active")
        for (k = 0; k < info_id.length; k++) {{
            if(val == info_id[k]){{
              document.getElementById(val).style.display = 'block';
              var x = document.getElementsByClassName(perVal);
              console.log(perVal);
              calCircle(perVal);      
              var y;
              for (y = 0; y < x.length; y++) {{
              x[y].style.display = 'block';
             }}
            }}
            else{{
              document.getElementById(info_id[k]).style.display = 'none';
              var x = document.getElementsByClassName(per_id[k]);
                var y;
                    for (y = 0; y < x.length; y++) {{
                     x[y].style.display = 'none';
                 }}
            }}

        }}   

   //on click event
   var i;
   for (i = 0; i < coll.length; i++) {{
   
      coll[i].addEventListener("click", function() {{
      
        var id1 = this.id;
        var value;
        var perValue
        if(id1 == "sum") {{ value = "summary";  perValue = "sumPer" ; }}
        if(id1 == "thr") {{ value = "third_party"; perValue = "thrPer" ; }}
        if(id1 == "dep") {{ value = "deprecated_jars"; perValue = "depPer" ; }}
        if(id1 == "ncj") {{ value = "non_compliant"; perValue = "ncjPer" ; }}
        if(id1 == "rev") {{ value = "revised_jars"; perValue = "revPer" ; }}
        var j;
        for (j = 0; j < info_id.length; j++) {{
            if(value == info_id[j]){{
              document.getElementById(value).style.display = 'block';
             var x = document.getElementsByClassName(perValue);   
             calCircle(perValue);      
               var y;
              for (y = 0; y < x.length; y++) {{
              x[y].style.display = 'block';
             }}
            }}
            else{{
              document.getElementById(info_id[j]).style.display = 'none';
               var x = document.getElementsByClassName(per_id[j]);
               var y;
                    for (y = 0; y < x.length; y++) {{
                     x[y].style.display = 'none';
                 }}
            }}
        }}   

        for (j = 0; j < list_id.length; j++) {{
            if(id1 == list_id[j]){{
              document.getElementById(id1).classList.add("active")
            }}
            else{{
              document.getElementById(list_id[j]).classList.remove("active")
            }}
        }}   

     }});
   }}


function calCircle(perValue) {{
var val;
 if(perValue == "sumPer"){{
 val = {Percentage};
 }}
 
 if(perValue == "thrPer"){{
 val = {ThirdParty_Per};
 }}
 
 if(perValue == "depPer"){{
  val = {Deprecated_Per};
 }}
 
 if(perValue == "ncjPer"){{
 val = {NonComplaint_Per};
 }}
 
 if(perValue == "revPer"){{
  val = {Revised_Per};
 }}
  val = (440 - (440* val ) / 100);
  document.getElementsByTagName("circle")[1].style['stroke-dashoffset'] = val;

}}
</script>
</body>
</html>"""

with open('jar_scanner_report.html', 'w') as f:
    f.write(html_text)

webbrowser.open_new_tab('jar_scanner_report.html')