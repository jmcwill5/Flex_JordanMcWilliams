**Flex: Build your own Exercise Plan**

Flex is an app that provides exercises for specific targeted muscle groups. First, you have the option to filter exercises by difficulty level. Second, you can use a visual of the human muscular system and click particular muscle buttons to see a list of exercises by muscle and difficulty level. This project will be useful to those who are new to exercising or need ideas to develop fitness plans based on their particular preferences and goals. You can develop a plan targeting as many muscles as you would like at whatever difficulty level you need. This plan can be printed or exported for later use. 

**Getting Started**
1. Download Python 3
2. Clone the repository
3. pip install flask pandas
4. Run the file called "run_main.py"
      - python run_main.py (if using terminal)
6. Open "http://127.0.0:5000" in your browser
   <img width="1444" height="220" alt="Screenshot 2025-08-05 at 10 49 44 PM" src="https://github.com/user-attachments/assets/92259a25-8001-4dbf-99e0-d53771f806ba" /> 

**Using the App**
1. Home Page
   - Select a difficulty level
   - Click a button on the muscle image to search
   <img width="1697" height="674" alt="Screenshot 2025-08-05 at 10 45 57 PM" src="https://github.com/user-attachments/assets/bf353138-308e-4c89-b11c-fe0f33adca7d" />
  
2. Results Page
   - Displays a list of results based on your chosen difficulty   level and muscle
   - "Add to My Exercise Plan" button allows you to add any exercises you would like to your own personal exercise plan
   - "View My Exercise Plan" button takes you to My Exercise Plan Page
   - "Resume Search" link takes you back to the home page to search for more exercises
   <img width="1705" height="836" alt="Screenshot 2025-08-05 at 10 46 45 PM" src="https://github.com/user-attachments/assets/988ac63b-7176-4bce-aab4-ad417dc4b7bb" />

     
3. My Exercise Plan Page
   -  Displays all of the exercises you have added to your exercise plan
   - "Delete" button allows you to remove exercises from your exercise plan
   - "Go to Home Page" link takes you back to the home page to search for more exercises
   - "Print or Save My Exercise Plan" button allows you to print or download a pdf of your exercise plan
   <img width="1707" height="632" alt="Screenshot 2025-08-05 at 10 46 53 PM" src="https://github.com/user-attachments/assets/3c8d7176-9290-4b83-ad4c-dc54cf97721c" />
  

**Possible errors or limitations**
- Clicking the "Add to My Exercise Plan" button does not consistently provide feedback that the exercise has been added to your plan. If you are not sure, please click the "View My Exercise Plan" button on the Results Page to check for missing exercises.
- You cannot view your exercise plan from the home page. To remedy this, click any muscle button to get to the results page. On the results page, you are able to scroll to the bottom and click the "View My Exercise Plan" button without adding any additional exercises to your exercise plan. 
- You can add the same exercise more than once. You can review your exercise plan through the results page to check for duplicates.
- "No exercises found for [muscle] at the [level] difficulty" means that there is no data on the csv for that particular muscle aat that particular difficulty. Click the "Resume Search" link to try different filters.
  <img width="1702" height="295" alt="Screenshot 2025-08-05 at 10 48 39 PM" src="https://github.com/user-attachments/assets/31f6a06f-ff82-483e-a0b1-79e7e251b57c" />
- Your exercise plan is only stored temporarily. Please make sure to print your plan or save a pdf copy before closing the app.
