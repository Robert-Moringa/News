# News

## This app is called [News](https://github.com/Robert-Moringa/Password-Locker.git).

### **This project was done using Python 3.8** 

# DESCRIPTION

This is a **News** application application that will help  list and preview news articles from various sources.   

The user will be able to:

* See various news sources on the homepage of the application.
* Select a news source and see all news articles from the selected news source in the application.
* See the image, description and the time a news article was created.
* Read fully of an article clicked.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

### Prerequisites

The following are required to start working on the project from your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.8
-Flask
-Pip
-virtualenv
-Visual Studio
```

## Getting Started

* Clone this repo to your local computer.
* Have python3.8 installed in your computer.
* Navigate to the cloned project folder from the terminal.
* Create a virtual environment and access the folder via your virtual machine.
* Visit https://newsapi.org/ and register for an API key.
* Create start.sh file and in it write the following lines:
```
 export NEWS_API_KEY='<Your-Api-Key>'
 python3.8 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* Alternatively the application can be accessed by visiting 

## Technologies Used

* Python v3.8
* Boostrap
* Flask

## License

MIT License

Copyright (c) 2021 Robert Maina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.