reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
]
#Task 1
for i in range(len(reviews)):
        review = reviews[i].lower().replace('good', 'GOOD').replace('excellent', 'EXCELLENT').replace('bad', 'BAD').replace('poor', 'POOR').replace('average', 'AVERAGE')
        print(review)

# Task 2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for i in range(len(reviews)):
        reviews[i] = reviews[i].lower().replace(",", "").replace(".", "").replace("!", "").split()
        counter = 0
        for word in reviews[i]:
                if word in positive_words or word in negative_words:
                        counter +=1
        print(f"Review index {i} has {counter} words from list")

reviews_copy = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
]
#Task 3
review_edit = reviews_copy[0][0:32]
print(review_edit + "...")
review_edit = reviews_copy[1][0:31]
print(review_edit + "...")
review_edit = reviews_copy[2][0:32]
print(review_edit + "...")
review_edit = reviews_copy[3][0:30]
print(review_edit + "...")
review_edit = reviews_copy[4][0:32]
print(review_edit + "...")