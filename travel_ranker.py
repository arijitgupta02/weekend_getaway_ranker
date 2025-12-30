import pandas as pd

def rank_destinations(source_city):
    df = pd.read_csv("travel_dataset.csv")

    city_data = df[df["NearestMajorCity"].str.lower() == source_city.lower()]

    if city_data.empty:
        print("No destinations found for this city.")
        return
    city_data = city_data.copy()
    city_data.loc[:, "Score"] = (
        (200 - city_data["Distance_km"]) * 0.4 +  
        city_data["Rating"] * 10 * 0.3 +
        city_data["PopularityScore"] * 0.3
    )


    ranked = city_data.sort_values(by="Score", ascending=False)

    print(f"\nTop Weekend Destinations from {source_city}:\n")
    print(ranked[["City", "State", "Distance_km", "Rating", "PopularityScore", "Score"]])

rank_destinations("Delhi")
rank_destinations("Mumbai")
rank_destinations("Bengaluru")
