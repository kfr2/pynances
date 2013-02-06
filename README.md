# PyNances
PyNances is a Flask-based[0] (mobile) web application for tracking and analyzing
spending habits.

## Goals
1. Allow the user to easily record expenses. An expense contains the amount of
   money spent, a list of user-defined categories, and (optionally) the GPS
   coordinates of the location at which the user records the expense. It may
   furthermore be interesting to allow the user to upload an attachment -- photos
   of the receipt or the good purchased -- to the expense.
2. Allow the user to establish budgets for various categories. For instance, the
   user may desire to set a food budget of $50 per week. The user should have
   easy access to budgets and the amount of money remaining in each for the
   specified time period.
3. Provide an analysis of the user's spending habits to enlighten her. For
   example, the user may desire to know she has spent $100 in the last week on
   comic books. This analysis should help enlighten the user to her actual
   spending habits versus her proposed budgets. This analysis will likely make
   use of data manipulation libraries like D3.js.

## (Some of the) Technologies and Ideas to Explore for this Project
* Heroku[1] or other PaaS-based hosting
* Amazon S3 -- for asset and user upload storage
* libraries like D3.js[2] and Piety[3] -- for creating easy-to-understand graphs
* Modest Maps[4] -- for creating a "heatmap" of the user's purchase locations
* HTML5 local storage -- for allowing the entry of expenses when the user does
  not have a connection to the Internet

## License
The MIT License
Copyright (c) 2013 Kevin Richardson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.


[0]: http://flask.pocoo.org/
[1]: http://heroku.com
[2]: http://d3js.org/
[3]: http://benpickles.github.com/peity/
[4]: http://modestmaps.com/
[0]: http://modestmaps.com/