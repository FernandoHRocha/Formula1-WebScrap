# Formula1_WebScrap

A web scrap to get information about the championship higher level racing, from the link below.
https://www.formula1.com/en/results.html/2021/drivers.html

The challenge here is:
GET DATA FROM A WEB TABLE INTO A EXCEL FILE

CONFIGURATION STEP:
    Import Selenium modules
    Import xlrd library
    Configure WebDrive to open in hidden mode

FIRST STEP - Get data of table:
    Save header information in an array;
        This header have empty elements, then we need to clean them;
    Line by line of the table body, to the information that we need;
        This table have first name and second name of each driver in different WebElements;
        To join the entire name of the driver in a single element of the array, we need to access the both information;
        First name is hidden (class name is defined as "hide-for-tablet"), then is necessary to use the WebElement.get_atribute('textContent') instead of WebElement.text, to get the information in a string format;

SECOND STEP - Save the data in excel file: