import pandas as pd

# Movies rated by users
data = {
    "User1": [5, 4, None, None], 
    "User2": [None, 5, 4, None],
    "User3": [None, None, 5, 4]
}
df = pd.DataFrame(data, index=["kgf", "bahubali", "rrr", "pushpa"])

def recommend_collaborative(df, target_user):
    # Find movies not rated yet by the target user
    unrated = df[target_user][df[target_user].isnull()].index
    # Find users most similar to target
    similar_users = [col for col in df.columns if col != target_user]
    recommendations = []
    for movie in unrated:
        # Average rating from other users
        avg_rating = df.loc[movie, similar_users].mean()
        if avg_rating >= 4:  # only strong recommendations
            recommendations.append(movie)
    return recommendations

print("Collaborative recommendations:", recommend_collaborative(df, "User1"))
