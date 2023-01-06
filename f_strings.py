intro1 = "Hi, my name is {} and I live at {}.";
intro2 = "I live at {1} and my name is {0}.";
name = "Ashutosh Gupta";
place = "Kanpur";
print(intro1.format(name, place));
print(intro2.format(name, place));
print(f"Hi, my name is {name} and I live at {place}.");
print(f"Hi, my name is {{name}} and I live at {{place}}.");

price = 23.3245;
print(f"This pen costs {price: .2f}");