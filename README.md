<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/images/logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">CSE 6242 Team 85 Project</h3>

  <p align="center">
    Inflation's impact on Sponsored Ads
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Projected Description

Many digital advertisers are concerned about how inflation in our current economic environment is impacting the overall performance of their digital advertisements. Advertisers care because they want to be able to properly allocate their budgets into advertising mediums that will drive revenue and ultimately get consumers to buy their product. It is well known that inflation impacts consumer purchasing behavior at the microeconomic level; therefore, it is imperative that advertisers want to know exactly how much inflation is impacting their digital advertisements across different types of products and media. It has also been established that inflation rose during the pandemic which resulted in a surprising decrease in product variety. The goal of this study is to isolate the effect of inflation on common advertising KPI’s (such as Conversion Rate) using logarithmic regression across different product taxonomies and digital advertisement formats using publicly available datasets.  

This repo is designed to be a support tool for the results of this study and is designed to showcase the final results and outputs of our findings. It is built via Python and Streamlit and includes graphs from Plotly. We approached this study by using quantitative data of digital ad performace on a retailer and collecting our own qualitative survey data on the hesitatancy of consumers to buy digital goods. With this tool you will be able to review our data documentation for both datasources as well as interact and view the results of our study. Its divided into a few different sections:
* Data Documentation
* Model Results
* Model Visualizations
* Survey Documentation
* Survey Results

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![python]][python-url] [![streamlit]][streamlit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps:

### Prerequisites

<B>Python 3.7</B>

Clone the repo:
```
*Make Sure You change director to git folder locally /DataVizProject
git clone https://github.com/jhkratoz/DataVizProject.git
```

Install Deps (within project folder)
```
pip install -e .

Some Windows Users:
pip install -e . --user
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
<div>Installation Video:</div>
[!(https://i9.ytimg.com/vi/0drj7pyjIRA/mqdefault.jpg?sqp=CPjlj5wG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGEsgWShlMA8=&rs=AOn4CLDMpjD2mvpBLK1u9w37uXLKRxpGXw)](https://www.youtube.com/watch?v=0drj7pyjIRA)

## Usage

Run the app:
```
streamlit run main.py
```

Now navigate to your browser and open up the following url: ```http://localhost:8501/```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[python]: https://img.shields.io/badge/Python-v3.7-brightgreen
[python-url]: https://www.python.org
[streamlit]: https://img.shields.io/badge/Streamlit-v1.12.2-red
[streamlit-url]: https://streamlit.io
