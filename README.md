Flex: Build your own Exercise Plan

Flex is an app that provides exercises for specific targeted muscle groups. First, you have the option to filter exercises by difficulty level. Second, you can use a visual of the human muscular system and click particular muscle buttons to see a list of exercises by muscle and difficulty level. This project will be useful to those who are new to exercising or need ideas to develop fitness plans based on their particular preferences and goals. You can develop a plan targeting as many muscles as you would like at whatever difficulty level you need. This plan can be printed or exported for later use. 

Getting Started
1. Download Python 3
2. Clone the repository
3. pip install flask pandas
4. Run the file called "run_main.py" and open "http://127.0.0:5000" in your browser

Using the App
1. Home Page
   - Select a difficulty level
   - Click a button on the muscle image to search
2. Results Page
   - Displays a list of results based on your chosen difficulty   level and muscle
   - "Add to My Exercise Plan" button allows you to add any exercises you would like to your own personal exercise plan
   - "View My Exercise Plan" button takes you to My Exercise Plan Page
   - "Resume Search" link takes you back to the home page to search for more exercises
3. My Exercise Plan Page
   -  Displays all of the exercises you have added to your exercise plan
   - "Delete" button allows you to remove exercises from your exercise plan
   - "Go to Home Page" link takes you back to the home page to search for more exercises
   - "Print or Save My Exercise Plan" button allows you to print or download a pdf of your exercise plan

Possible errors or limitations
- "No exercises found for [muscle] at the [level] difficulty" means that there is no data on the csv for that particular muscle aat that particular difficulty. Click the "Resume Search" link to try different filters.
- Clicking the "Add to My Exercise Plan" button does not consistently provide feedback that the exercise has been added to your plan. If you are not sure, please click the "View My Exercise Plan" button on the Results Page to check for missing exercises.
- You cannot view your exercise plan from the home page. To remedy this, click any muscle button to get to the results page. On the results page, you are able to scroll to the bottom and click the "View My Exercise Plan" button without adding any additional exercises to your exercise plan. 
- You can add the same exercise more than once. You can review your exercise plan through the results page to check for duplicates.
- Your exercise plan is only stored temporarily. Please make sure to print your plan or save a pdf copy before closing the app.