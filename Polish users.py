# Create good script to create new list, which only contains users from Poland. Try to do it
# with List Comprehension.
users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name":
                                                                                          "Yeti"}]

polish_users = [user for user in users if user.get('country') and user["country"] == "Poland"]

print(polish_users)
