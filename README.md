Weekend Getaway Ranker
-----------------------

A beginner-friendly Data Engineering project that recommends the best weekend travel destinations in India based on:

- Distance from source city
- Tourist Rating  
- Popularity Score  

The script ranks places and returns the **top destinations to visit from a given city**.


Features
-----------
- Reads data from CSV using **Pandas**
- Calculates ranking score based on weighted formula
- Displays top destinations for:
  - Delhi
  - Mumbai
  - Bengaluru
- Fully customizable dataset — add more cities & places if needed

Project Structure
---------------------------

- weekend_getaway_ranker/
  - travel_ranker.py # Main script
  - travel_dataset.csv # Travel data
  - sample_output.txt # Output examples
  - requirements.txt # Dependencies
  - README.md # Project documentation


Technologies Used
-------------------

- Python
- Pandas

Installation & Usage
----------------------

1. Clone the repository -

   git clone https://github.com/
   arijitgupta02/weekend_getaway_ranker.git
   cd weekend_getaway_ranker

3. Install dependencies -

   pip install -r requirements.txt

5. Run the script -

   python travel_ranker.py


This will display the top destinations from each major city listed in the dataset.


Sample Output
---------------

- Top Weekend Destinations from Delhi:

  1. Agra
  
  2. Jaipur
  
  3. Manali

- Top Weekend Destinations from Mumbai:

  1. Lonavala
  
  2. Alibaug
  
  3. Mahabaleshwar

- Top Weekend Destinations from Bengaluru:

  1. Mysore
  
  2. Coorg
  
  3. Ooty


Notes
-------

- You can add more cities/places in **travel_dataset.csv**
- Adjust scoring formula if you want different ranking weight



If you like this project
Give the repo a star — it motivates to build more projects!


