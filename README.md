### Liine Take Home 

__Python is preferred, but if you feel unable to complete it using python, use whatever programming language you feel most comfortable in.__

Build an API with an endpoint which takes a single parameter, a datetime string, and returns a list of restaurant names which are open on that date and time. You are provided a dataset in the form of a CSV file of restaurant names and a human-readable, string-formatted list of open hours. Store this data in whatever way you think is best. Optimized solutions are great, but correct solutions are more important. Make sure whatever solution you come up with can account for restaurants with hours not included in the examples given in the CSV. Please include all tests you think are needed.

### Assumptions:
* If a day of the week is not listed, the restaurant is closed on that day
* All times are local — don’t worry about timezone-awareness
* The CSV file will be well-formed, assume all names and hours are correct

### Want bonus points? Here are a few things we would really like to see:
1. A Dockerfile and the ability to run this in a container
3. Using the python standard library as much as possible.
4. Testing

If you have any questions, let me know. Use git to track your progress, and push your solution to a github repository (public or if private just give me access @sharpmoose)

--------

# Write Up Below


### Initial Thoughts
The feature seems pretty straight forward, I will start by laying out the steps I plan to take.
1. Setup git, pycharm, pytest, python 3.8, Postman, and pipeline for code version-control (~30 minutes)
2. Setup up documentation to keep track of thoughts, setup, and procedure for feature. ( ~5 minutes)
3. Start by getting data into python and analyzing data for setting up data digestion (~30 minutes) 
4. Digest data into standard data format, and Test for unknowns and Test for edge cases (~1.5 hour)
5. Setup and Test back-end business logic for handling date-time and generating restaurants open during that date-time. ( ~1 hour)
6. Setup Flask to implement REST API access to business logic. (10 minutes)
7. Test with Postman (20 minutes)

After these steps are satisfied, I will attempt to finish bonus criteria.
8. Setup a Dockerfile for the back-end API, and business logic.
9. Using the Python standard library. (This should be done by default)
10.  Testing (This will be down during development)

-------
### Questions & Anwsers
Why Python 3.8?
> It is what I have installed, and would rather have something newer then 3.5 at least.

Why setup documentation at the beginning?
> This makes it easier to keep track of task, and the best documentation comes while the actions are still fresh in my mind.

Why spend so much time on analysis the data and validating / testing it?
> I feel this appropriate whenever I receive data that I am unfamiliar with. Unfamiliar with the process to collect the data. 
Then I will assert what I know about the data so far. If any malformed data is passed later the outcome will NOT be undefined.
I will re-format all the data to be consistent, this is done after the step to check for malformed data. 
This last step to re-format the data for consistency is really for the future developers and consideration for teammates.
This takes more time but in my experience is always worth it.

Why Flask for the REST API?
>Well it is not as robust as Django, but Flask is quicker to setup and is more appropriate for small projects that consist of one contributor.



