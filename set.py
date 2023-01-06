s1 = {1, 2, 4, 5, 6};
s2 = {3, 6, 7};

print(s1.union(s2));
print(s1.intersection(s2));
print(s1.update(s2));
print(s1);

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"};
print(cities1.symmetric_difference(cities2));
print(cities1.difference(cities2));
print(cities1.isdisjoint(cities2));
print(cities1.issuperset(cities2));
print(cities1.issubset(cities2));
cities1.add("Viena");
print(cities1);
cities1.remove("Madrid");
print(cities1);
cities1.discard("Tokyo");
print(cities1);
print(cities1.pop());
# del cities1;
# print(cities1);
# cities1.clear();
# print(cities1);
print("Delhi" in cities1);