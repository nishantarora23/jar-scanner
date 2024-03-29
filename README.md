<!-- LICENSE -->
![](https://img.shields.io/badge/version-1.0-green.svg) ![](https://img.shields.io/badge/License-MIT-orange.svg)


<br />
<p align="center">
  <h2 align="center">JAR-Scanner</h2>

  <p align="center">
    Be compliant with the licenses of your 3rd Party JARs.
    <br />
    <a href="https://github.com/nishantarora94/jar-scanner/issues">Report Bug</a>
    ·
    <a href="https://github.com/nishantarora94/jar-scanner/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
  * [OS Compatibility](#os-compatibility)
* [Getting Started](#getting-started)
* [JAR-Scanner Configuration](#jar-scanner-configuration)
* [Run Scan](#run-scan)
* [Sample JAR-Scanner Report](#sample-jar-scanner-report)
* [JAR-Scanner v1.0 Demo](#jar-scanner-v1.0-demo)
* [Contribution](#contribution)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

<b>JAR-Scanner v1.0</b> is a python CLI based tool performing the analysis of all the JARs which are bundled as part of the product release. The main objective of this tool is to find the 3rd party JARs in the project and check if the license has been procured or not. It is done by comparing all the jars with the existing License document which contains the list JARs with already procured licenses. The tool will also project the JARs which are no longer used in the project.




### Built With
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a><a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/></a><a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/></a><a href="https://www.w3schools.com/js/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" alt="js" width="40" height="40"/></a>

### OS Compatibility

* Windows
* Linux (x64)


<!-- GETTING STARTED -->
## Getting Started

To get this project in your system, follow the below steps:

1. Clone the repo
```sh
git clone https://github.com/nishantarora94/jar-scanner.git
```
2. You are good to go.

<!-- JAR-SCANNER CONFIGURATION -->
## JAR-Scanner Configuration

<b>Bucket</b> – Folder for all the WAR, EAR, ZIP files extracted by the tool.<br/>
<b>Requisite</b> – Folder for CSV files containing list of proprietary JARs and 3rd party pre-approved JARs.<br/>
<b>License.csv</b> – The list of 3rd party JARs which are part of the product release and for which license has been procured.<br/>
<b>suppression_jars.csv</b> – The list of proprietary JARs which are suppressed during the scan.<br/>
<b>Report</b> – Folder for output report.<br/>
<b>venv</b> – To keep dependencies separate and creating python virtual environment.<br/><br/>


<!-- RUN SCAN -->
## Run Scan

Run the below command to initiate the command:

```sh
python jar-scanner.py
```


<!--SAMPLE REPORT-->
## Sample JAR-Scanner Report

![](https://github.com/nishantarora94/jar-scanner/blob/master/Demo/jar_scanner_report.JPG)

<h3> What are the tabs in the report all about? </h3><br/>
<b>3rd Party Jars</b>: All the 3rd party JARs which are currently part of the scanned project.<br/>
<b>New Jars</b>: All the JARs which have been newly added to the project and are not part of the suppression_jars CSVor License CSV list.<br/>
<b>Upgraded Jars</b>: All the 3rd party JARs which are part of the License CSV document but the JAR version has been upgraded.<br/>
<b>Unutilized Jars</b>: All the 3rd party jars which are part of the License CSV document but are not being utilized in the scanned project currently.<br/><br/>

<!--JAR-SCANNER v1.0 DEMO-->
## JAR-Scanner v1.0 Demo

![](https://github.com/nishantarora94/jar-scanner/blob/master/Demo/jar-scanner-v1.0-demo.gif)

<!--CONTRIBUTION-->
## Contribution
Your contribution can make a huge difference. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/<Branch_Name>`)
3. Commit your Changes (`git commit -m 'ADD COMMIT MESSAGE`)
4. Push to the Branch (`git push origin feature/<Branch_Name>`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Nishant Arora - [LinkedIn](https://linkedin.com/nishantarora94/) - aroranish23@gmail.com

Project Link: [https://github.com/nishantarora94/jar-scanner](https://github.com/nishantarora94/jar-scanner)
